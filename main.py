import matplotlib.pyplot as plt
import os
from flask import Flask, render_template
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/run')
def run_model():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(BASE_DIR, 'data')

    red_before = np.load(os.path.join(data_path, 'red_before.npy'))
    nir_before = np.load(os.path.join(data_path, 'nir_before.npy'))
    red_after = np.load(os.path.join(data_path, 'red_after.npy'))
    nir_after = np.load(os.path.join(data_path, 'nir_after.npy'))

    ndvi_before = (nir_before - red_before) / (nir_before + red_before + 1e-5)
    ndvi_after = (nir_after - red_after) / (nir_after + red_after + 1e-5)

    damage = ndvi_before - ndvi_after
    damage_percent = (np.sum(damage > 0.2) / damage.size) * 100

    return f"Damage Detected: {damage_percent:.2f}%"

# Create static folder if not exists
static_path = os.path.join(BASE_DIR, 'app', 'static')
os.makedirs(static_path, exist_ok=True)

# Save NDVI before
plt.imshow(ndvi_before, cmap='RdYlGn')
plt.colorbar()
plt.title("NDVI Before")
plt.savefig(os.path.join(static_path, 'ndvi_before.png'))
plt.close()

# Save NDVI after
plt.imshow(ndvi_after, cmap='RdYlGn')
plt.colorbar()
plt.title("NDVI After")
plt.savefig(os.path.join(static_path, 'ndvi_after.png'))
plt.close()

# Save damage map
plt.imshow(damage, cmap='coolwarm')
plt.colorbar()
plt.title("Damage Map")
plt.savefig(os.path.join(static_path, 'damage.png'))
plt.close()

if __name__ == "__main__":
    app.run(debug=True)