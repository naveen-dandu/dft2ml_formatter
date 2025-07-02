import re

def parse_outcar(outcar_path):
    """
    Parses number of atoms, total energy, and Fermi level from OUTCAR.
    """
    num_atoms = None
    total_energy = None
    fermi_level = None

    with open(outcar_path, "r") as f:
        for line in f:
            if "NIONS" in line:
                try:
                    num_atoms = int(line.strip().split()[-1])
                except Exception:
                    pass

            if "E-fermi" in line and fermi_level is None:
                try:
                    fermi_level = float(line.strip().split()[2])
                except Exception:
                    pass

            if "free  energy   TOTEN" in line:
                try:
                    total_energy = float(line.strip().split()[4])
                except Exception:
                    pass

    return {
        "num_atoms": num_atoms,
        "fermi_energy": fermi_level,
        "total_energy_eV": total_energy
    }


def extract_bandgap_from_doscar(doscar_path, fermi_energy=None):
    """
    Extracts the band gap from a DOSCAR file (spin-unpolarized).
    """
    with open(doscar_path, "r") as f:
        lines = f.readlines()

    header_lines = 6
    try:
        nedos = int(lines[5].split()[2])
    except Exception:
        raise ValueError("Could not extract NEDOS from DOSCAR header")

    energy_data = []
    for line in lines[header_lines:header_lines + nedos]:
        tokens = line.strip().split()
        if len(tokens) >= 2:
            energy = float(tokens[0])
            total_dos = float(tokens[1])
            energy_data.append((energy, total_dos))

    # Extract Fermi energy from DOSCAR if not provided
    if fermi_energy is None:
        for line in lines:
            if "E-fermi" in line:
                fermi_energy = float(line.split()[2])
                break
        if fermi_energy is None:
            raise ValueError("Fermi energy not found.")

    occupied = [e for e, d in energy_data if e <= fermi_energy and d > 1e-4]
    unoccupied = [e for e, d in energy_data if e > fermi_energy and d > 1e-4]

    if not occupied or not unoccupied:
        return 0.0  # Metallic or invalid

    vbm = max(occupied)
    cbm = min(unoccupied)
    return max(cbm - vbm, 0.0)


def parse_vasp_outputs(outcar_path="OUTCAR", doscar_path="DOSCAR"):
    """
    Combines OUTCAR and DOSCAR parsing into a single report.
    """
    outcar_info = parse_outcar(outcar_path)
    bandgap = extract_bandgap_from_doscar(doscar_path, fermi_energy=outcar_info.get("fermi_energy"))
    outcar_info["bandgap_eV"] = bandgap
    return outcar_info


# For testing/demo:
if __name__ == "__main__":
    data = parse_vasp_outputs("examples/vasp/OUTCAR", "examples/vasp/DOSCAR")
    print("Parsed VASP Data:\n", data)
