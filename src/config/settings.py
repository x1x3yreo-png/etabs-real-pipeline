from dataclasses import dataclass
from pathlib import Path

@dataclass
class Settings:
    drift_limit: float = 0.005
    utilization_limit: float = 0.90
    input_dir: Path = Path("data/input")
    output_dir: Path = Path("data/output")
    material_file: str = "materials.xlsx"
    section_file: str = "sections.xlsx"
    story_file: str = "stories.xlsx"
    load_file: str = "loads.xlsx"
    combos_file: str = "combos.xlsx"
    export_file: str = "revit_export.xlsx"