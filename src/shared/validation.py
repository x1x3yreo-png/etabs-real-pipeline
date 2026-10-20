import pandas as pd

def validate_revit_export(df: pd.DataFrame) -> bool:
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

    missing = [col for col in required if col not in df.columns]
    if missing:
        raise ValueError(f"Faltan columnas en revit_export.xlsx: {missing}")

    if df.empty:
        raise ValueError("No hay elementos estructurales exportados desde Revit.")

    return True