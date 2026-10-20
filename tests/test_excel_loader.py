from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
sys.path.append(str(SRC))

from excel_loader import ExcelLoader

def test_loader_loads_all():
    loader = ExcelLoader(str(ROOT / "data" / "input"))
    data = loader.load_all()
    assert "materials" in data
    assert "sections" in data
    assert "stories" in data
    assert "grids" in data
    assert "frames" in data
    assert "loads" in data
    assert "combos" in data