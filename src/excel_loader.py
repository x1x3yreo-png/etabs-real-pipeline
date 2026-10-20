from __future__ import annotations

from pathlib import Path
import pandas as pd

from src.config import INPUT_DIR
from src.validators import validate_data


class ExcelLoader:
    def __init__(self, input_dir: str | Path | None = None):
        self.input_dir = Path(input_dir) if input_dir is not None else INPUT_DIR

    def read_sheet(self, file_name: str, sheet_name: str = "Sheet1"):
        file_path = self.input_dir / file_name
        if not file_path.exists():
            raise FileNotFoundError(f"No existe el archivo: {file_path}")

        df = pd.read_excel(file_path, sheet_name=sheet_name)
        return df

    def load_all(self) -> dict:
        data = {
            "materials": self.read_sheet("materials.xlsx", "materials"),
            "sections": self.read_sheet("sections.xlsx", "sections"),
            "stories": self.read_sheet("stories.xlsx", "stories"),
            "grids": self.read_sheet("grids.xlsx", "grids"),
            "frames": self.read_sheet("frames.xlsx", "frames"),
            "loads": self.read_sheet("loads.xlsx", "loads"),
            "combos": self.read_sheet("combos.xlsx", "combos"),
        }

        validate_data(data)
        return data