from __future__ import print_function
import argparse
import torch
import torch.optim as optim
from torchvision import datasets, transforms
from torch.optim.lr_scheduler import StepLR
import util
import CNN

def load_args():
    parser = argparse.ArgumentParser(description='PyTorch MNIST Example')
    parser.add_argument('--batch-size', type=int, default=64, metavar='N',
                        help='input batch size for training (default: 64)')
    parser.add_argument('--test-batch-size', type=int, default=1000, metavar='N',
                        help='input batch size for testing (default: 1000)')
    parser.add_argument('--epochs', type=int, default=14, metavar='N',
                        help='number of epochs to train (default: 14)')
    parser.add_argument('--lr', type=float, default=1.0, metavar='LR',
                        help='learning rate (default: 1.0)')
    parser.add_argument('--gamma', type=float, default=0.7, metavar='M',
                        help='Learning rate step gamma (default: 0.7)')
    parser.add_argument('--no-cuda', action='store_true', default=False,
                        help='disables CUDA training')
    parser.add_argument('--no-mps', action='store_true', default=False,
                        help='disables macOS GPU training')
    parser.add_argument('--dry-run', action='store_true', default=False,
                        help='quickly check a single pass')
    parser.add_argument('--seed', type=int, default=1, metavar='S',
                        help='random seed (default: 1)')
    parser.add_argument('--log-interval', type=int, default=10, metavar='N',
                        help='how many batches to wait before logging training status')
    parser.add_argument('--save-model', type=str, default='',
                        help='Model name and filepath for saving model.')
    parser.add_argument('--model-type', type=str, default='net1',
                        help='net1, net2, net3, net4')

    return parser.parse_args()

def get_device(args):
    use_cuda = not args.no_cuda and torch.cuda.is_available()
    use_mps = not args.no_mps and torch.backends.mps.is_available()

    torch.manual_seed(args.seed)

    if use_cuda:
        device = torch.device("cuda")
    elif use_mps:
        device = torch.device("mps")
    else:
        device = torch.device("cpu")

    return use_cuda, device


def get_dataloaders(train_kwargs, test_kwargs):
    transform=transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
        ])

    train_data = datasets.FashionMNIST('../data', train=True, download=True,
                       transform=transform)

    train_data, val_data = torch.utils.data.random_split(train_data, [0.8, 0.2])


    test_data = datasets.FashionMNIST('../data', train=False,
                       transform=transform)

    train_loader = torch.utils.data.DataLoader(train_data,**train_kwargs)

    val_loader = torch.utils.data.DataLoader(val_data, **test_kwargs)

    test_loader = torch.utils.data.DataLoader(test_data, **test_kwargs)


    return train_loader, val_loader, test_loader


def main():
    args = load_args()
    use_cuda, device = get_device(args)

    train_kwargs = {'batch_size': args.batch_size}
    test_kwargs = {'batch_size': args.test_batch_size}

    if use_cuda:
        cuda_kwargs = {'num_workers': 1,
                       'pin_memory': True,
                       'shuffle': True}
        train_kwargs.update(cuda_kwargs)
        test_kwargs.update(cuda_kwargs)

    print("Getting data")
    train_loader, val_loader, test_loader = get_dataloaders(train_kwargs, test_kwargs)

    ## Get model 
    if args.model_type == 'net1':
        model = CNN.Net1().to(device)
    elif args.model_type == 'net2':
        model = CNN.Net2().to(device)
    elif args.model_type == 'net3':
        model = CNN.Net3().to(device)
    elif args.model_type == 'net4':
        model = CNN.Net4().to(device)
    else:
        print("Please enter valid model type: net1, net2, net3, net4")
        exit()

    optimizer = optim.Adadelta(model.parameters(), lr=args.lr)

    scheduler = StepLR(optimizer, step_size=1, gamma=args.gamma)

    print("Starting train")
    util.train(args, model, device, train_loader, val_loader, optimizer, scheduler)

    
    if len(args.save_model)>0:
        print("Saving model")
        torch.save(model.state_dict(), args.save_model)

    print("Starting evaluate")
    util.evaluate(model, device, args, test_loader)

   


if __name__ == '__main__':
    main()

    









    

