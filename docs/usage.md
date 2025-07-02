# Usage Guide

This page shows how to use `dft2ml_formatter` to extract useful features from quantum chemistry output files (VASP, Gaussian, ORCA, CP2K) and convert them into ML-ready formats (e.g., JSON, CSV).

---

## Installation

You can install the package using:

```bash
pip install dft2ml_formatter
```

Or clone the repo and install locally:

```bash
git clone https://github.com/naveen-dandu/dft2ml_formatter_full
cd dft2ml_formatter_full
pip install -e .
```

---

## Basic Example (VASP)

Assume you have an `OUTCAR` and `DOSCAR` in `examples/vasp/`. You can extract features like bandgap, number of atoms, total energy, and Fermi level using:

```python
from dft2ml_formatter.vasp_parser import extract_vasp_features

features = extract_vasp_features(
    outcar_path="examples/vasp/OUTCAR",
    doscar_path="examples/vasp/DOSCAR"
)

print(features)
```

This will output a dictionary:

```python
{
    "num_atoms": 108,
    "total_energy": -315.72,
    "fermi_energy": -4.45,
    "bandgap": 1.73
}
```

---

## Output Formats

You can save to JSON/CSV using:

```python
import json
import pandas as pd

with open("vasp_features.json", "w") as f:
    json.dump(features, f)

pd.DataFrame([features]).to_csv("vasp_features.csv", index=False)
```

---

## End-to-End Demo

See [`notebooks/DFT2ML_Demo.ipynb`](https://github.com/naveen-dandu/dft2ml_formatter_full/blob/main/notebooks/DFT2ML_Demo.ipynb) for a full walkthrough.
