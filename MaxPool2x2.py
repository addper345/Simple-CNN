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
        h, w = image.shape
        h = h//2
        w = w//2
        output = np.zeroes(h,w)
        for i, j, region in self.getRegions(image):
            output[i, j] = np.amax(region, axis=(0,1))

        return output