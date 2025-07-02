
# dft2ml_formatter

[![CI](https://github.com/naveen-dandu/dft2ml_formatter_full/actions/workflows/python-package.yml/badge.svg)](https://github.com/naveen-dandu/dft2ml_formatter_full/actions/workflows/python-package.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**dft2ml_formatter** is a lightweight Python package that extracts and formats key physical and chemical properties from **DFT output files** (VASP, CP2K, ORCA, Gaussian) into **ML-ready JSON or CSV** formats. It facilitates seamless downstream machine learning workflows in materials science and chemistry.

## 🚀 Why this tool?

Preparing datasets from quantum chemistry calculations is often a tedious and manual task. `dft2ml_formatter` bridges that gap by:

- Parsing complex outputs from various quantum chemistry codes
- Extracting key properties: energy, band gap, Fermi level, atom types, basis sets, and more
- Saving results in a consistent and machine-readable format
- Enabling large-scale ML dataset curation in a unified pipeline

## 📦 Installation

```bash
pip install dft2ml-formatter
```

Or install from source:

```bash
git clone https://github.com/naveen-dandu/dft2ml_formatter_full
cd dft2ml_formatter_full
pip install .
```

---

## Launch Demo Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/naveen-dandu/dft2ml_formatter_full/blob/main/notebooks/DFT2ML_Demo.ipynb)

---

## 🧠 Features

- ✅ VASP: extract Fermi energy, total energy, band gap, atom types
- ✅ Gaussian: extract energies, basis sets, convergence, charges
- ✅ ORCA: extract SCF energies, atom types, spin multiplicities
- ✅ CP2K: extract geometry, charge/multiplicity, band gap
- ✅ Output format: JSON, CSV (structured)
- ✅ CLI and notebook usage support
- ✅ Modular and extendable for future codes

## 🧪 Example Usage

```python
from dft2ml_formatter import parse_outcar

# Example: Parse VASP OUTCAR
result = parse_outcar("examples/vasp/OUTCAR")
print(result['num_atoms'], result['fermi_energy'], result['total_energy'])
```

See full [example notebook](notebooks/DFT2ML_Demo.ipynb).

## 📂 Parsers Overview

| Code      | File Type(s)            | Supported Outputs                                  |
|-----------|-------------------------|----------------------------------------------------|
| **VASP**  | OUTCAR, DOSCAR, POSCAR  | `bandgap`, `total_energy`, `num_atoms`, `E-fermi` |
| **CP2K**  | `.log`, `.xyz`, `.ener` | `total_energy`, `charge`, `multiplicity`, `gap`   |
| **Gaussian** | `.log`               | `Energies`, `charges`, `multiplicity`, `convergence` |
| **ORCA**  | `.out`                  | `SCF Energy`, `atoms`, `charge`, `multiplicity`   |

See [`docs/parsers.md`](docs/parsers.md) for details.

## 📘 Documentation

MkDocs-generated documentation is available [here](https://naveen-dandu.github.io/dft2ml_formatter_full).

- 📄 [Usage Guide](docs/usage.md)
- 🧩 [Parser Details](docs/parsers.md)

## ✅ Contributing

We welcome contributions for additional parser modules or output formats.

1. Fork this repo
2. Create a feature branch
3. Add new parser under `dft2ml_formatter/`
4. Include a test under `tests/`
5. Submit a PR

## 📄 License

MIT License. See `LICENSE` for details.


## 📊 Citation (optional)

If you find this tool useful, please cite it or reference the GitHub repository in your work:

```
@software{dft2ml_formatter,
  author = {Naveen Dandu},
  title = {dft2ml_formatter: A tool for parsing and formatting DFT outputs for ML},
  year = 2025,
  url = {https://github.com/naveen-dandu/dft2ml_formatter_full}
}
```

## 🌟 Star this repo to support development!
