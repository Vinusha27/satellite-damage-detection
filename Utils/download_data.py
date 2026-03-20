import numpy as np
import matplotlib.pyplot as plt
import os

# Create data folder
os.makedirs("data", exist_ok=True)

# Create fake Red & NIR bands (simulation)
red = np.random.randint(50, 150, (200, 200)).astype(float)
nir = np.random.randint(100, 200, (200, 200)).astype(float)

# Save as numpy files
np.save("data/B4.npy", red)
np.save("data/B8.npy", nir)

print("Sample data created successfully!")