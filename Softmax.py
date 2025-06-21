import numpy as np


class Softmax:
    def __init__(self, input_len, nodes):
        self.weights = np.random.randn(input_len, nodes)/input_len
        self.biases = np.zeros(nodes)

    def forward(self, input):
        #input.shape = (13,13,8)
        self.last_input_shape = input.shape
        input = input.flatten()
        self.last_input = input

        #totals.shape = (1,nodes)
        totals = np.dot(input, self.weights) + self.biases
        self.last_input_totals = totals
        exp = np.exp(totals)
        return exp/np.sum(exp)
    
    def backprop(self, grad_output, learn_rate):
        for i, gradient in enumerate(grad_output):
            if gradient == 0:
                continue
            totals = self.last_input_totals
            t_exp = np.exp(totals)
    

            S = np.sum(t_exp)

            grad_totals = -t_exp[i]*t_exp/(S**2)
            grad_totals[i] = t_exp[i]*(S-t_exp[i])/(S**2)
            
            #grad_weights.shape = (input_len,)
            grad_weights = self.last_input
            grad_biases = 1
            #grad_input.shape = (input_len, nodes) 
            grad_input = self.weights
            grad_loss_totals = gradient*grad_totals

            #(input_len, 1) * (1, nodes) = (input_len, nodes)
            grad_loss_weights = grad_weights[np.newaxis].T @ grad_loss_totals[np.newaxis]
            grad_loss_biases = grad_loss_totals
            #(input_len,nodes)*(nodes,1) = (input_len,1)?
            grad_loss_inputs = grad_input @ grad_loss_totals

            self.weights -= learn_rate*grad_loss_weights
            self.biases -= learn_rate*grad_loss_biases

            return grad_loss_inputs.reshape(self.last_input_shape)