import numpy as np

class conv3x3:
    def __init__(self, num_filters):
        self.num_filters = num_filters
        self.filters = np.random.randn(num_filters, 3, 3)/9

    def getRegions(self, input):
        
        h, w = input.shape

        for i in range(h-2):
            for j in range(w-2):
                image = input[i:i+3, j:j+3]
                yield i, j, image

    def feedForwards(self, input):
        h, w = input.shape
        self.last_input = input
        output = np.zeros((h-2, w-2, self.num_filters))
        for i, j, image in self.getRegions(input):
            image = np.array(image)
            output[i, j] = np.sum(image*self.filters, axis=(1, 2))
        return output
    
    def backprop(self, gradient, lr=0.005):
        grad= np.zeros((8,3,3))
        image = self.last_input
        h, w = image.shape
        h1, w1, l = gradient.shape
        
        for i, j, region in self.getRegions(self.last_input):
            for a in range(8):
                grad[a] += gradient[i,j,a]*region
                
        self.filters -= lr*grad
        return None


        
    

    