import os
from dft2ml_formatter.vasp_parser import parse_outcar

def test_parse_outcar():
    outcar_path = os.path.join(os.path.dirname(__file__), "../examples/vasp/OUTCAR")
    result = parse_outcar(outcar_path)
    assert isinstance(result, dict)


