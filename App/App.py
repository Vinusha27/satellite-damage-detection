import os
from flask import Flask, render_template
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/run')
def run_model():
    # Get base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Build correct path
    data_path = os.path.join(BASE_DIR, 'data')

    # Load data
    red_before = np.load(os.path.join(data_path, 'red_before.npy'))
    nir_before = np.load(os.path.join(data_path, 'nir_before.npy'))
    red_after = np.load(os.path.join(data_path, 'red_after.npy'))
    nir_after = np.load(os.path.join(data_path, 'nir_after.npy'))

    # NDVI calculation
    ndvi_before = (nir_before - red_before) / (nir_before + red_before + 1e-5)
    ndvi_after = (nir_after - red_after) / (nir_after + red_after + 1e-5)

    # Damage calculation
    damage = ndvi_before - ndvi_after

    # Damage %
    damage_percent = (np.sum(damage > 0.2) / damage.size) * 100

    return render_template("index.html", result=f"Damage Detected: {damage_percent:.2f}%")

if __name__ == "__main__":
    app.run(debug=True)