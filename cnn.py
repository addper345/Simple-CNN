import numpy as np
import Conv3x3
import MaxPool2x2
import Softmax
conv = Conv3x3.conv3x3(8)
pool = MaxPool2x2.MaxPool2x2()
soft = Softmax.Softmax(13*13*8, 10)
def forward(input, label):
    out = conv.feedForwards(input)
    out = pool.feedForward(out)
    guess = soft.forward(out)

    loss = -np.log(guess[label])
    acc = 1 if np.argmax(guess) == label else 0

    gradient = np.zeros(10)
    gradient[label] = -1/guess[label]

    return guess, loss, acc


def train(im, label, lr=0.005):
    out, loss, acc = forward(im, label)

    gradient = np.zeros(10)
    gradient[label] = -1/out[label]

    gradient = soft.backprop(gradient, lr)

    return loss, acc
