import torch 
class RNNDecoder(torch.nn.Module):
    def __init__(self, vocabSize, nEmbed, nHidden, nLayers):
        super(RNNDecoder, self).__init__()

        ## Implement this. You  must use. 
        # 1. Embedding layer
        # 2. RNN layer
        # 3. A decoder to generate predictions
        

    def forward(self, X, hidden):
        ## Forward pass returns prediction and hidden

        ## Implement this
        pass

    def init_hidden(self, batchSize):
        return torch.zeros((self.nLayers, batchSize, self.nHidden), dtype=torch.float)
        

    def loss(self, y_hat, y):
        ## Using pytorch cross-entropy loss
        criterion = torch.nn.CrossEntropyLoss()
        return criterion(y_hat, y)
