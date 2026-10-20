from __future__ import annotations

from pathlib import Path
import pandas as pd

from etabs_automation.domain.models import (
    Material,
    Section,
    Story,
    Grid,
    Frame,
    LoadCase,
    LoadCombo,
    StructuralModel,
)
from etabs_automation.domain.validation import validate_model


class ExcelLoader:
    def __init__(self, input_dir: str | Path):
        self.input_dir = Path(input_dir)

    def read_excel_table(self, file_name: str, sheet_name: str):
        file_path = self.input_dir / file_name
        if not file_path.exists():
            raise FileNotFoundError(f"No existe el archivo: {file_path}")

        return pd.read_excel(file_path, sheet_name=sheet_name)

    def load_model(self) -> StructuralModel:
        materials_df = self.read_excel_table("materials.xlsx", "materials")
        sections_df = self.read_excel_table("sections.xlsx", "sections")
        stories_df = self.read_excel_table("stories.xlsx", "stories")
        grids_df = self.read_excel_table("grids.xlsx", "grids")
        frames_df = self.read_excel_table("frames.xlsx", "frames")
        loads_df = self.read_excel_table("loads.xlsx", "loads")
        combos_df = self.read_excel_table("combos.xlsx", "combos")

        model = StructuralModel(
            materials=[Material(**row) for row in materials_df.to_dict(orient="records")],
            sections=[Section(**row) for row in sections_df.to_dict(orient="records")],
            stories=[Story(**row) for row in stories_df.to_dict(orient="records")],
            grids=[Grid(**row) for row in grids_df.to_dict(orient="records")],
            frames=[Frame(**row) for row in frames_df.to_dict(orient="records")],
            loads=[LoadCase(**row) for row in loads_df.to_dict(orient="records")],
            combos=[LoadCombo(**row) for row in combos_df.to_dict(orient="records")],
        )

        validate_model(model)
        return model