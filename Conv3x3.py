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
        

    