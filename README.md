# Trame / Jupyter tutorial

The goal of this directory is to go over trame in the context of Jupyter for interactive VTK visualization.
This tutorial aims to be done over a 30 minutes period.

## Environment setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

Don't forget to allow extension and unlock it

```bash
jupyter labextension list
jupyter labextension enable trame-jupyter-extension
jupyter labextension unlock trame-jupyter-extension:plugin
```

## Getting started with PyVista and Trame

PyVista makes it trivial to do VTK visualization but also provides a nice and already built-in viewer.
Let's start with the basic and then we'll build up your understanding of trame to go beyond what PyVista give you for free.

Launch the environment by running: `jupyter lab`

```python
import pyvista as pv
from pyvista import examples

dataset = examples.download_lucy()
dataset.plot(smooth_shading=True, color='white')
```

Then you can switch between **Remote Rendering** and **Local rendering**


## Additional steps for 03_WASM_rendering.ipynb

Deactivate existing python virtual environment and restart Jupyter with the TRAME_INJECT_HEADER environment variable defined

```bash
python3 -m venv .venv_next
source .venv/bin/activate
pip install -U pip
pip install -r requirements_next.txt
export TRAME_INJECT_HEADER=1
jupyter lab
```