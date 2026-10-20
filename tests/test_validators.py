import pandas as pd
from src.domain.validators import validate_revit_export, validate_materials

def test_validate_materials():
    df = pd.DataFrame([
        {"material_name": "C25", "material_type": "Concrete", "E": 25000000, "nu": 0.2, "gamma": 25.0, "code": "EC2"},
        {"material_name": "S355", "material_type": "Steel", "E": 210000000, "nu": 0.3, "gamma": 78.5, "code": "EN"},
    ])
    assert validate_materials(df) is True

def test_validate_revit_export():
    df = pd.DataFrame([
        {
            "element_id": "1001",
            "category": "Structural Columns",
            "family_name": "Concrete Col",
            "type_name": "C25 Rect",
            "section_name": "RC_RECT_300x600",
            "material_name": "C25",
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