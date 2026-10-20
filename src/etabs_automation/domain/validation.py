from __future__ import annotations

from typing import Any, Dict

from etabs_automation.domain.models import StructuralModel


class ValidationError(ValueError):
    pass


def validate_model(model: StructuralModel) -> None:
    if not model.materials:
        raise ValidationError("No hay materiales definidos.")
    if not model.sections:
        raise ValidationError("No hay secciones definidas.")
    if not model.stories:
        raise ValidationError("No hay stories definidos.")
    if not model.frames:
        raise ValidationError("No hay frames definidos.")

    # Validación simple de duplicados
    material_names = [m.material_name for m in model.materials]
    if len(material_names) != len(set(material_names)):
        raise ValidationError("Hay materiales duplicados.")

    section_names = [s.section_name for s in model.sections]
    if len(section_names) != len(set(section_names)):
        raise ValidationError("Hay secciones duplicadas.")

    story_names = [s.story_name for s in model.stories]
    if len(story_names) != len(set(story_names)):
        raise ValidationError("Hay stories duplicados.")

    # Elevaciones crecientes
    elevations = [s.elevation for s in model.stories]
    if elevations != sorted(elevations):
        raise ValidationError("Las elevaciones de stories no están ordenadas de forma creciente.")