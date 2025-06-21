import numpy as np

def readMNIST(amount):
    
    try:
        images = open('training_data\\train-images.idx3-ubyte', 'rb')
        labels = open('training_data\\train-labels.idx1-ubyte', 'rb')

        #skipping past headers
        images.read(16)
        labels.read(8)

        for i in range(amount):
            label = labels.read(1)
            label = int.from_bytes(label, byteorder='big')
            image = []
            for j in range(784):
                number = int.from_bytes(images.read(1), byteorder='big')
                image.append(number)
            image = np.array(image)
            image = image.reshape((28,28))
            yield i, label, image
    finally:
        images.close()
        labels.close()