import torch 
from torch.utils.data import DataLoader

def train(args, model, device, train_loader, val_loader, optimizer, scheduler):
    model.train()
    for epoch in range(args.epochs):
        epoch_loss = 0
        batch_idx = 0

        for X,y in train_loader:
            batch_idx+=1
            X,y = X.to(device), y.to(device)
            
            ## Write code here



            if batch_idx % args.log_interval == 0:
                print(f"Batch {batch_idx}:\t Avg Train Loss: {round(epoch_loss/batch_idx,5)}")

        val_loss = round(compute_loss(model, device, val_loader), 5)
        print(f"Epoch {epoch+1}:\t Avg Train Loss: {round(epoch_loss/batch_idx,5)}\t Avg Val Loss: {val_loss}")
        scheduler.step()

@torch.no_grad()
def compute_loss(model, device, data_loader):
    pass
    