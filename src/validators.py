from __future__ import annotations

from typing import Dict, Any

from src.config import REQUIRED_TABLES


class DataValidationError(ValueError):
    pass


def validate_data(data: Dict[str, Any]) -> bool:
    for table_name, required_cols in REQUIRED_TABLES.items():
        if table_name not in data:
            raise DataValidationError(f"Falta la tabla: {table_name}")

        missing = [col for col in required_cols if col not in data[table_name].columns]
        if missing:
            raise DataValidationError(f"En '{table_name}' faltan columnas: {missing}")

    # Validaciones adicionales
    validate_story_orders(data["stories"])
    validate_materials(data["materials"])
    validate_sections(data["sections"])
    return True


def validate_story_orders(stories_df) -> None:
    if stories_df.empty:
        raise DataValidationError("La tabla stories está vacía.")

    if "elevation" not in stories_df.columns:
        raise DataValidationError("La tabla stories no tiene 'elevation'.")

    if not stories_df["elevation"].is_monotonic_increasing:
        raise DataValidationError("Las elevaciones de stories no están ordenadas de forma creciente.")


def validate_materials(materials_df) -> None:
    required = ["material_name", "E", "nu", "gamma"]
    for col in required:
        if col not in materials_df.columns:
            raise DataValidationError(f"materials.xlsx no tiene la columna '{col}'.")

    if materials_df.empty:
        raise DataValidationError("materials.xlsx está vacío.")

    if materials_df["material_name"].duplicated().any():
        raise DataValidationError("Hay materiales duplicados.")


def validate_sections(sections_df) -> None:
    if sections_df.empty:
        raise DataValidationError("sections.xlsx está vacío.")

    if "section_name" not in sections_df.columns:
        raise DataValidationError("sections.xlsx no tiene 'section_name'.")

    if sections_df["section_name"].duplicated().any():
        raise DataValidationError("Hay secciones duplicadas.")