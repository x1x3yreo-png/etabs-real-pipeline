import pandas as pd

def normalize_revit_export(df: pd.DataFrame):
    required_cols = [
        "element_id",
        "category",
        "family_name",
        "type_name",
        "section_name",
        "material_name",
        "level_name",
        "start_x",
        "start_y",
        "start_z",
        "end_x",
        "end_y",
        "end_z",
        "length",
        "element_type",
    ]

    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(f"Faltan columnas: {missing}")

    out = df.copy()
    out["section_name"] = out["section_name"].str.strip()
    out["level_name"] = out["level_name"].str.strip()
    return out

def build_materials_df():
    return pd.DataFrame([
        {"material_name": "RC", "E": 25000000, "nu": 0.2, "gamma": 25},
        {"material_name": "Steel", "E": 200000000, "nu": 0.3, "gamma": 78.5},
    ])

def build_sections_df():
    return pd.DataFrame([
        {"section_name": "C1", "material_name": "RC", "shape": "rect", "area": 0.25, "b": 0.4, "h": 0.6},
        {"section_name": "V1", "material_name": "RC", "shape": "rect", "area": 0.18, "b": 0.3, "h": 0.6},
        {"section_name": "COL1", "material_name": "RC", "shape": "circle", "area": 0.19635, "diameter": 0.5},
    ])

def build_stories_df():
    return pd.DataFrame([
        {"story_name": "Base", "elevation": 0.0},
        {"story_name": "Nivel 1", "elevation": 3.2},
        {"story_name": "Nivel 2", "elevation": 6.4},
        {"story_name": "Nivel 3", "elevation": 9.6},
    ])