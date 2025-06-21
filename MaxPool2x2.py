import numpy as np

class MaxPool2x2:
    def getRegions(self, image):
        h,w,_= image.shape

        h = h//2
        w = w//2

        for i in range(h):
            for j in range(w):
                im_region = image[(2*i):(2*i+2), (2*j):(2*j+2)]
                yield i, j, im_region

    def feedForward(self, image):
        self.last_input = image
        self.last_input_shape = image.shape
        h, w, l= image.shape
        h = h//2
        w = w//2
        output = np.zeros((h,w,l))
        for i, j, region in self.getRegions(image):
            output[i, j] = np.amax(region, axis=(0,1))

        return output
    
    def backprop(self, gradient):
        grad = np.zeros(self.last_input_shape)

        for i, j, region in self.getRegions(self.last_input):
            amax = np.amax(region, axis=(0,1))
            h, w, l = region.shape

            for a in range(l):
                for b in range(h):
                    for c in range(w):
                        if amax[a] == region[b, c, a]:
                            grad[2*i+b, 2*j+c, a] = gradient[i, j, a]

        return grad
