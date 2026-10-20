import pandas as pd
from src.shared.validation import validate_revit_export

def test_validate_revit_export_ok():
    df = pd.DataFrame([
        {
            "element_id": "1001",
            "category": "Structural Columns",
            "family_name": "Concrete Col",
            "type_name": "Col 300x500",
            "section_name": "C1",
            "material_name": "RC",
            "level_name": "Nivel 1",
            "start_x": 0,
            "start_y": 0,
            "start_z": 0,
            "end_x": 0,
            "end_y": 0,
            "end_z": 3.2,
            "length": 3.2,
            "element_type": "column",
        }
    ])
    assert validate_revit_export(df) is True