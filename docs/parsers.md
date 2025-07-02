# Supported Parsers

This package includes lightweight parsers to extract key physical quantities from quantum chemistry outputs.

---

## 1. VASP

**Module**: `vasp_parser.py`

**Parsed files**:
- `OUTCAR`: total energy, number of atoms, Fermi level
- `DOSCAR`: band gap (from total DOS)

**Function**:
```python
extract_vasp_features(outcar_path, doscar_path)
```

---

## 2. Gaussian

**Module**: `gaussian_parser.py`

**Parsed files**:
- `.log` or `.out`: HOMO-LUMO gap, total energy, atom list

*Function to be implemented soon.*

---

## 3. ORCA

**Module**: `orca_parser.py`

**Parsed files**:
- `.out`: total energy, HOMO-LUMO, atom list

*Function to be implemented soon.*

---

## 4. CP2K

**Module**: `cp2k_parser.py`

**Parsed files**:
- `.log`: final energy, atom list
- `.xyz`: structure

*Function to be implemented soon.*

---

## Utilities

**Module**: `utils.py`

Shared functions:
- Unit conversions (Ha → eV, Å → Bohr)
- Line search
- Sanitization helpers

---

### Contributions Welcome

If you’d like to add new features or file formats, please see [CONTRIBUTING.md](contributing.md) or open a pull request!
