import os
import pytest
from dft2ml_formatter.vasp_parser import parse_outcar

TEST_OUTCAR_PATH = os.path.join(os.path.dirname(__file__), "..", "examples", "vasp", "OUTCAR")

@pytest.mark.skipif(not os.path.exists(TEST_OUTCAR_PATH), reason="OUTCAR file not found")
def test_vasp_outcar_parsing():
    parsed = parse_outcar(TEST_OUTCAR_PATH)
    assert isinstance(parsed, dict), "Parsed result should be a dictionary"
    assert "energy" in parsed, "Energy key should be present in parsed data"
    assert isinstance(parsed["energy"], float), "Energy value should be a float"

