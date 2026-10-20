import pandas as pd

def validate_materials(df: pd.DataFrame):
    required = ["material_name", "material_type", "E", "nu", "gamma", "code"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Faltan columnas de material: {missing}")
    if df.empty:
        raise ValueError("materials.xlsx vacío.")
    return True

def validate_sections(df: pd.DataFrame):
    required = ["section_name", "material_name", "shape", "area"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Faltan columnas de sección: {missing}")
    if df.empty:
        raise ValueError("sections.xlsx vacío.")
    return True

def validate_stories(df: pd.DataFrame):
    required = ["story_name", "elevation"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Faltan columnas de stories: {missing}")
    if df.empty:
        raise ValueError("stories.xlsx vacío.")
    return True

def validate_revit_export(df: pd.DataFrame):
    required = [
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
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Faltan columnas en Revit export: {missing}")
    if df.empty:
        raise ValueError("revit_export.xlsx vacío.")
    return True