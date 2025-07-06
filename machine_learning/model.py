import torch
from torch import nn
class ImprovedBoson(nn.Module):
    def __init__(self, input_shape: int, hidden_units: int, output_shape: int):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(input_shape, hidden_units),
            nn.BatchNorm1d(hidden_units),
            nn.LeakyReLU(),
            nn.Dropout(0.3),

            nn.Linear(hidden_units, hidden_units),
            nn.BatchNorm1d(hidden_units),
            nn.LeakyReLU(),
            nn.Dropout(0.3),

            nn.Linear(hidden_units, hidden_units),
            nn.BatchNorm1d(hidden_units),
            nn.LeakyReLU(),
            nn.Dropout(0.3),

            nn.Linear(hidden_units, output_shape)
        )
    def forward(self, x):
        return self.model(x)
