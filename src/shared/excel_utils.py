from pathlib import Path
import pandas as pd

def normalize_section_name(value: str) -> str:
    return str(value).strip().replace(" ", "_").upper()

def ensure_dir(path: str | Path):
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p

def build_materials_template():
    return pd.DataFrame([
        {"material_name": "RC", "E": 25000000, "nu": 0.2, "gamma": 25},
        {"material_name": "Steel", "E": 200000000, "nu": 0.3, "gamma": 78.5},
    ])

def build_sections_template():
    return pd.DataFrame([
        {"section_name": "C1", "material_name": "RC", "shape": "rect", "area": 0.25, "b": 0.4, "h": 0.6},
        {"section_name": "V1", "material_name": "RC", "shape": "rect", "area": 0.18, "b": 0.3, "h": 0.6},
        {"section_name": "COL1", "material_name": "RC", "shape": "circle", "area": 0.19635, "diameter": 0.5},
    ])

def build_stories_template():
    return pd.DataFrame([
        {"story_name": "Base", "elevation": 0.0},
        {"story_name": "Nivel 1", "elevation": 3.2},
        {"story_name": "Nivel 2", "elevation": 6.4},
        {"story_name": "Nivel 3", "elevation": 9.6},
    ])

def build_frames_from_revit_export(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        raise ValueError("Revit export vacío.")

    out = df.copy()
    out["section_name"] = out["section_name"].apply(normalize_section_name)
    return out