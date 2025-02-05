## Parts of this code was adapted from Prof. Forrest Davis

import torch


def train(model, data): 
    """
    Function to train model on data
    """
    X = data["X"]
    y = data["y"]

    optimizer = torch.optim.SGD(model.parameters(), lr=0.3, momentum=0.9)
    for t in range(30):
        y_pred = model(X)
        loss = model.loss(y_pred, y)
        if t % 10 == 0:
            print(t, loss.item())
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

def batched_train(model, data, batch_size):
    """
    Function to train model in mini-batches of batch_size. 
    """
    ## Implement this
    pass

def evaluate(model, data): 
    """
    Compare model's prediction to true output and return MSE
    """
    pass


def create_regression_data(weights:torch.tensor, bias:float, noise_scale:float, num_samples:float) -> dict:
    """
    Generate synthetic data given a regression model's weight, bias, and scale for noise
    For some sampled noise x, the noise for that sample would be x*noise_scale
    """

    # Create torch.tensor X with random input values

    # Create torch.tensor noise with one noise value per sample (scaled by the noise_scale float)


    # Create torch.tensor y that combines X, w, b and noise. 


    data = {"X": X, "y": y}

    return data

