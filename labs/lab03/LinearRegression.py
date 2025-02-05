import torch

class LinearRegression(torch.nn.Module): 
    """ Class for linear regression
    """
    def __init__(self, num_inputs):
        super().__init__() # ensures base nn is correctly initialized

        ## Initialize a linear layer
        

    def forward(self, X):
        ## Implement this
        pass

    def loss(self, y_hat, y):
        ## Implement this. Use Loss function in 3.1.1.2 from the textbook (https://d2l.ai/index.html)

        pass
