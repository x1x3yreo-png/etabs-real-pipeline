from __future__ import annotations

import logging
from typing import Any

class ModelBuilder:
    def __init__(self, sap_model: Any):
        self.sap = sap_model
        self.logger = logging.getLogger(__name__)

    def create_materials(self, materials_df):
        for _, row in materials_df.iterrows():
            material_name = row["material_name"]
            e = row["E"]
            nu = row["nu"]
            gamma = row["gamma"]

            # Pseudocódigo – ajustar según la versión ETABS:
            # self.sap.PropMaterial.AddMaterial(material_name, "Concrete")
            # self.sap.PropMaterial.SetMaterial(material_name, e, nu, gamma)
            self.logger.debug(f"Material listo: {material_name}")

    def create_sections(self, sections_df):
        for _, row in sections_df.iterrows():
            section_name = row["section_name"]
            material_name = row["material_name"]
            shape = row["shape"]

            if shape.lower() == "rect":
                b = row.get("b", None)
                h = row.get("h", None)
                # self.sap.PropFrame.SetRectangle(section_name, material_name, b, h)
                pass
            elif shape.lower() == "circle":
                diameter = row.get("diameter", None)
                # self.sap.PropFrame.SetCircle(section_name, material_name, diameter)
                pass
            else:
                # Sección general
                # self.sap.PropFrame.SetGeneral(...)
                pass

            self.logger.debug(f"Sección lista: {section_name}")

    def create_stories(self, stories_df):
        for _, row in stories_df.iterrows():
            story_name = row["story_name"]
            elevation = row["elevation"]
            # self.sap.Story.Setup.SetStory(story_name, elevation)
            self.logger.debug(f"Story creada: {story_name} @ {elevation}")

    def create_grids(self, grids_df):
        for _, row in grids_df.iterrows():
            grid_name = row["grid_name"]
            x = row["x"]
            y = row["y"]
            direction = row["direction"]
            # self.sap.GridSys.SetGrid(...)
            self.logger.debug(f"Grid creada: {grid_name}")

    def create_frames(self, frames_df):
        for _, row in frames_df.iterrows():
            frame_id = row["frame_id"]
            story = row["story"]
            start_node = row["start_node"]
            end_node = row["end_node"]
            section_name = row["section_name"]

            # self.sap.PointObj.AddCartesian(...)
            # self.sap.FrameObj.AddByCoord(...)
            # self.sap.FrameObj.SetSection(frame_id, section_name)
            self.logger.debug(f"Frame creada: {frame_id} -> {section_name}")

    def create_load_cases(self, loads_df):
        for _, row in loads_df.iterrows():
            load_case = row["load_case"]
            load_type = row["type"]
            value = row["value"]
            direction = row["direction"]
            element_id = row["element_id"]

            # self.sap.LoadCases.StaticNonlinear.Add(...)
            self.logger.debug(f"Carga creada: {load_case} - {load_type}")

    def create_combos(self, combos_df):
        for _, row in combos_df.iterrows():
            combo_name = row["combo_name"]
            case_name = row["case_name"]
            factor = row["factor"]

            # self.sap.LoadCases.LoadCombination.Add(...)
            self.logger.debug(f"Combinación creada: {combo_name}")