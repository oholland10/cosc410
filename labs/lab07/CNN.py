import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

class Net1(nn.Module):
    """
    Conv1 -> ReLU -> Conv2 -> ReLU -> MaxPool -> Dropout -> FullyConnected -> LogSoftmax output.

    - Conv1: 16 filters, 3x3 convolutional kernel, stride 1
    - Conv2: 32 filters, 3x3 convolutional kernel, stride 1
    - MaxPool: Kernel size 2; everything else default. 
    - FullyConnected: as many units as output
    """
    def __init__(self):
        super(Net1, self).__init__()
        self.dropout = nn.Dropout(0.25)
        ## Write code here
        

    def forward(self, x):
        ## Write code here
        pass

    def lostt(self, pred, y):
        pass


class Net2(nn.Module):
    """
    Conv1 -> ReLU -> Conv2 -> ReLU -> MaxPool -> Conv3 -> ReLU -> MaxPool -> Dropout -> FullyConnected -> ReLU -> LogSoftmax output.

    - Conv1: 32 filters, 3x3 convolutional kernel, stride 1
    - Conv2: 64 filters, 3x3 convolutional kernel, stride 1
    - Conv3: 16 filters, 3x3 convolutional kernel, stride 1
    - MaxPool: Kernel size 2; everything else default. 
    - FullyConnected: as many units as output
    """
    def __init__(self):
        super(Net2, self).__init__()
        self.dropout = nn.Dropout(0.25)
        ## Write code here
        

    def forward(self, x):
        ## Write code here

        pass

    def lostt(self, pred, y):
        pass



class Net3(nn.Module):
    """
    Conv1 -> ReLU -> Conv2 -> ReLU -> MaxPool -> Conv3 -> ReLU -> MaxPool -> Dropout1 -> FullyConnected1 -> ReLU -> Dropout2 -> FullyConnected2 -> LogSoftmax output.

    - Conv1: 32 filters, 3x3 convolutional kernel, stride 1
    - Conv2: 64 filters, 5x5 convolutional kernel, stride 1
    - Conv3: 16 filters, 2x2 convolutional kernel, stride 1
    - MaxPool: Kernel size 2; everything else default. 
    - FullyConnected1: 57 hidden units
    - FullyConnected2: as many units as output
    """
    def __init__(self):
        super(Net3, self).__init__()
        self.dropout = nn.Dropout(0.25)
        ## Write code here
        pass
        

    def forward(self, x):
        ## Write code here

        pass

    def lostt(self, pred, y):
        pass

