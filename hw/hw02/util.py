import torch

def batched_train(model, data, batch_size):
    """
    Function to train model in mini-batches of batch_size. 
    """

    pass


def predict(model, data): 
    """
    Generate predictions from a model given some data

    """

    pass


def create_classification_data(weights:torch.tensor, bias:torch.tensor, noise_scale:float, num_samples:float) -> dict:
    """
    Generate synthetic data given a multinomial regression model's weight, bias, and scale for noise
    
    For some sampled noise x, the noise for that sample would be x*noise_scale
    """

    pass