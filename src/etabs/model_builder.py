import logging
import pandas as pd

class ETABSModelBuilder:
    def __init__(self, sap_model):
        self.sap = sap_model
        self.logger = logging.getLogger(__name__)

    def create_materials(self, materials_df: pd.DataFrame):
        for _, row in materials_df.iterrows():
            name = row["material_name"]
            e = row["E"]
            nu = row["nu"]
            gamma = row["gamma"]

            # EJEMPLO GENERICO
            # self.sap.PropMaterial.AddMaterial(name, "Concrete")
            # self.sap.PropMaterial.SetMaterial(name, e, nu, gamma)

            self.logger.info(f"Material creado: {name}")

    def create_sections(self, sections_df: pd.DataFrame):
        for _, row in sections_df.iterrows():
            name = row["section_name"]
            material = row["material_name"]
            shape = row["shape"]

            if shape.lower() == "rect":
                b = row["b"]
                h = row["h"]
                # self.sap.PropFrame.SetRectangle(name, material, b, h)
                pass
            elif shape.lower() == "circle":
                d = row["diameter"]
                # self.sap.PropFrame.SetCircle(name, material, d)
                pass

            self.logger.info(f"Sección creada: {name}")

    def create_stories(self, stories_df: pd.DataFrame):
        for _, row in stories_df.iterrows():
            story_name = row["story_name"]
            level = row["elevation"]
            # self.sap.Story.Setup.SetStory(story_name, level)
            self.logger.info(f"Story creada: {story_name}")

    def create_frames(self, frames_df: pd.DataFrame):
        for _, row in frames_df.iterrows():
            # se crea frame desde start/end coords
            # self.sap.PointObj.AddCartesian(...)
            # self.sap.FrameObj.AddByCoord(...)
            # self.sap.FrameObj.SetSection(...)
            self.logger.info(f"Frame creada: {row['element_id']}")

    def create_load_cases(self, loads_df: pd.DataFrame):
        for _, row in loads_df.iterrows():
            # ejemplo
            # self.sap.LoadCases.StaticNonlinear.Add(...)
            self.logger.info(f"Carga definida: {row['load_case']}")

    def create_combos(self, combos_df: pd.DataFrame):
        for _, row in combos_df.iterrows():
            # self.sap.LoadCases.LoadCombination.Add(...)
            self.logger.info(f"Combinación creada: {row['combo_name']}")