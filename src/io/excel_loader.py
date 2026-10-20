from pathlib import Path
import pandas as pd

class ExcelLoader:
    def __init__(self, input_dir: str | Path):
        self.input_dir = Path(input_dir)

    def read_excel(self, file_name: str):
        file_path = self.input_dir / file_name
        if not file_path.exists():
            raise FileNotFoundError(f"No existe {file_path}")
        return pd.read_excel(file_path)

    def load_materials(self):
        return self.read_excel("materials.xlsx")

    def load_sections(self):
        return self.read_excel("sections.xlsx")

    def load_stories(self):
        return self.read_excel("stories.xlsx")

    def load_loads(self):
        return self.read_excel("loads.xlsx")

    def load_combos(self):
        return self.read_excel("combos.xlsx")

    def load_revit_export(self):
        return self.read_excel("revit_export.xlsx")