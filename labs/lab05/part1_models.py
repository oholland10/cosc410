import torch

class Perceptron(torch.nn.Module):
    """
    Single layer perceptron with no hidden layers

    """
    def __init__(self, num_inputs, num_classes):
        super().__init__() # ensures base nn is correctly initialized

        ## Implement this
        pass
        

    def forward(self, X):
        ## Implement this
        pass

    def loss(self, y_hat, y):
        ## Implement this. 
        pass

class FNN_1layer(torch.nn.Module):
    """
    FNN with one hidden layer and non-linear activation function

    """

    def __init__(self, num_inputs,  num_classes, activation_function, num_hidden):
        super().__init__() # ensures base nn is correctly initialized

        ## Implement this
        pass
        

    def forward(self, X):
        ## Implement this
        pass

    def loss(self, y_hat, y):
        ## Implement this.
        pass

class FNN_1layer_linear(torch.nn.Module):
    """
    FNN with one hidden layer and linear activation function

    """

    def __init__(self, num_inputs, num_classes, activation_function, num_hidden):
        super().__init__() # ensures base nn is correctly initialized

        ## Implement this
        pass
        

    def forward(self, X):
        ## Implement this
        pass

    def loss(self, y_hat, y):
        ## Implement this.
        pass
