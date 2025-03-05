import torch


def batch_train(model, train_loader, valid_loader, num_epochs, lr=0.1):
    optimizer = torch.optim.SGD(model.parameters(), lr=lr, momentum=0.9)

    for epoch in range(num_epochs):
        epoch_loss = 0
        num_batches = 0

        for X,y in train_loader:
            ## Complete this loop

            ## Hint: You might have to reshape y_pred and flatten y. https://pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html


            optimizer.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 0.25) #helps with exploding gradient
            optimizer.step()
            epoch_loss += loss.item()

        val_loss = round(compute_loss(model, valid_loader), 5)
        if epoch%5 == 0:
            print(f"Epoch {epoch+1}:\t Avg Train Loss: {round(epoch_loss/num_batches,5)}\t Avg Val Loss: {val_loss}")



@torch.no_grad()  ## ensures gradient not computed for this function. 
def compute_loss(model, data_loader):
    """
    Returns avg loss of the model on the data
    """
    total_loss = 0
    for i, datapoint in enumerate(data_loader):
        ## Implement this loop
       continue 

    return total_loss/(i+1)