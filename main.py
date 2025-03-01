import wandb
import torch
from NeuralNetwork import NeuralNetwork

wandb.login()

run = wandb.init(
    # Set the project where this run will be logged
    project="BaseballWeatherAnalysis",
    # Track hyperparameters and run metadata
    config={
        "Eps_start": Eps_start,
        "Eps_end": Eps_end,
        "Eps_decay": Eps_decay,
        "episodes": num_episodes,
        "lr": lr,
        "name": name,
    },
    # mode="disabled",
)

device = torch.device("mps")

def train(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset)
    model.train()
    for batch, (X, y) in enumerate(dataloader):
        X, y = X.to(device), y.to(device)

        # Compute prediction error
        pred = model(X)
        loss = loss_fn(pred, y)

        # Backpropagation
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

        if batch % 100 == 0:
            loss, current = loss.item(), (batch + 1) * len(X)
            print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")