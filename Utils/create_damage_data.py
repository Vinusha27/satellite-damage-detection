import numpy as np
import os

os.makedirs("data", exist_ok=True)

red_before = np.random.randint(50, 120, (200, 200)).astype(float)
nir_before = np.random.randint(150, 220, (200, 200)).astype(float)

red_after = red_before + np.random.randint(0, 50, (200, 200))
nir_after = nir_before - np.random.randint(0, 80, (200, 200))

np.save("data/red_before.npy", red_before)
np.save("data/nir_before.npy", nir_before)
np.save("data/red_after.npy", red_after)
np.save("data/nir_after.npy", nir_after)

print("Dataset created")