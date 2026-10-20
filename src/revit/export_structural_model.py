# -*- coding: utf-8 -*-
# pyRevit script: export structural members to Excel

import os
import math
import pandas as pd
import clr

clr.AddReference("RevitAPI")
clr.AddReference("RevitAPIUI")
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Structure import *

doc = __revit__.ActiveUIDocument.Document

def get_param_value(element, param_name):
    param = element.LookupParameter(param_name)
    if param is None:
        return None
    try:
        return param.AsString()
    except:
        try:
            return param.AsValueString()
        except:
            try:
                return param.AsDouble()
            except:
                return None

def get_curve_points(element):
    loc = element.Location
    if loc is None:
        return None
    if isinstance(loc, LocationCurve):
        curve = loc.Curve
        p1 = curve.Evaluate(0.0, True)
        p2 = curve.Evaluate(1.0, True)
        return p1, p2
    return None

def get_type_name(element):
    type_id = element.GetTypeId()
    if type_id:
        _type = doc.GetElement(type_id)
        if _type:
            return _type.Name
    return "UNKNOWN_TYPE"

def get_level_name(element):
    level = element.Level if hasattr(element, "Level") else None
    return level.Name if level else "NO_LEVEL"

rows = []

categories = [
    BuiltInCategory.OST_StructuralColumns,
    BuiltInCategory.OST_StructuralFraming,
    BuiltInCategory.OST_StructuralFoundation,
]

for cat in categories:
    elems = FilteredElementCollector(doc).OfCategory(cat).WhereElementIsNotElementType().ToElements()
    for el in elems:
        if not hasattr(el, "Location"):
            continue

        points = get_curve_points(el)
        if points is None:
            continue

        p1, p2 = points
        category_name = el.Category.Name if el.Category else "UNKNOWN"
        family_name = el.Symbol.FamilyName if hasattr(el, "Symbol") and el.Symbol else "UNKNOWN_FAMILY"
        type_name = get_type_name(el)
        level_name = get_level_name(el)
        material_name = el.Material.Name if el.Material else "UNKNOWN_MATERIAL"

        section_name = get_param_value(el, "Section")
        if not section_name:
            section_name = type_name

        element_type = "column" if "column" in category_name.lower() else "beam"

        row = {
            "element_id": str(el.Id.IntegerValue),
            "category": category_name,
            "family_name": family_name,
            "type_name": type_name,
            "section_name": section_name,
            "material_name": material_name,
            "level_name": level_name,
            "start_x": p1.X,
            "start_y": p1.Y,
            "start_z": p1.Z,
            "end_x": p2.X,
            "end_y": p2.Y,
            "end_z": p2.Z,
            "length": round(math.dist((p1.X, p1.Y, p1.Z), (p2.X, p2.Y, p2.Z)), 4),
            "element_type": element_type,
        }
        rows.append(row)

df = pd.DataFrame(rows)
out_dir = os.path.join(os.path.expanduser("~"), "Desktop", "revit_structural_export")
os.makedirs(out_dir, exist_ok=True)
output_path = os.path.join(out_dir, "revit_export.xlsx")
df.to_excel(output_path, index=False)
print("Archivo exportado:", output_path)