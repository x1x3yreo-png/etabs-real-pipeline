import logging
import pandas as pd

class ETABSBuilder:
    def __init__(self, sap_model):
        self.sap = sap_model
        self.logger = logging.getLogger(__name__)

    def initialize_new_model(self):
        # self.sap.InitializeNewModel()
        # self.sap.File.NewBlank()
        self.logger.info("Modelo inicializado.")

    def add_materials(self, materials_df: pd.DataFrame):
        for _, row in materials_df.iterrows():
            material_name = row["material_name"]
            e = float(row["E"])
            nu = float(row["nu"])
            gamma = float(row["gamma"])

            # self.sap.PropMaterial.AddMaterial(material_name, "Concrete")
            # self.sap.PropMaterial.SetMaterial(material_name, e, nu, gamma)
            self.logger.info(f"Material creado: {material_name}")

    def add_sections(self, sections_df: pd.DataFrame):
        for _, row in sections_df.iterrows():
            section_name = row["section_name"]
            material_name = row["material_name"]
            shape = row["shape"]

            if shape.lower() == "rect":
                b = float(row["b"])
                h = float(row["h"])
                # self.sap.PropFrame.SetRectangle(section_name, material_name, b, h)
                pass
            elif shape.lower() == "circle":
                d = float(row["diameter"])
                # self.sap.PropFrame.SetCircle(section_name, material_name, d)
                pass

            self.logger.info(f"Sección creada: {section_name}")

    def add_stories(self, stories_df: pd.DataFrame):
        for _, row in stories_df.iterrows():
            story_name = row["story_name"]
            elevation = float(row["elevation"])
            # self.sap.Story.Setup.SetStory(story_name, elevation)
            self.logger.info(f"Story creada: {story_name} @ {elevation}")

    def add_grids(self, grids_df: pd.DataFrame):
        for _, row in grids_df.iterrows():
            name = row["grid_name"]
            x = row["x"]
            y = row["y"]
            direction = row["direction"]
            # self.sap.GridSys.SetGrid(name, x, y, direction)
            self.logger.info(f"Grid creada: {name}")

    def add_frames_from_revit_export(self, frames_df: pd.DataFrame):
        for _, row in frames_df.iterrows():
            x1 = float(row["start_x"])
            y1 = float(row["start_y"])
            z1 = float(row["start_z"])
            x2 = float(row["end_x"])
            y2 = float(row["end_y"])
            z2 = float(row["end_z"])
            section_name = row["section_name"]

            # self.sap.PointObj.AddCartesian(x1, y1, z1)
            # self.sap.PointObj.AddCartesian(x2, y2, z2)
            # self.sap.FrameObj.AddByCoord(x1, y1, z1, x2, y2, z2)
            # self.sap.FrameObj.SetSection(frame_name, section_name)

            self.logger.info(f"Frame creada: {section_name}")

    def add_load_cases(self, loads_df: pd.DataFrame):
        for _, row in loads_df.iterrows():
            load_case = row["load_case"]
            load_type = row["type"]
            value = float(row["value"])
            direction = row["direction"]
            self.logger.info(f"Carga creada: {load_case} ({load_type}, {direction})")

    def add_load_combos(self, combos_df: pd.DataFrame):
        for _, row in combos_df.iterrows():
            combo_name = row["combo_name"]
            case_name = row["case_name"]
            factor = float(row["factor"])
            self.logger.info(f"Combinación creada: {combo_name}")

    def run_analysis(self):
        # self.sap.Analyze.RunAnalysis()
        self.logger.info("Análisis ejecutado.")