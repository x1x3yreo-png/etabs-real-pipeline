import pandas as pd
import logging

class ModelBuilder:
    def __init__(self, sap_model):
        self.sap = sap_model
        self.logger = logging.getLogger(__name__)

    def create_materials(self, materials_df: pd.DataFrame):
        for _, row in materials_df.iterrows():
            self.logger.info(f"Material: {row['material_name']}")

    def create_sections(self, sections_df: pd.DataFrame):
        for _, row in sections_df.iterrows():
            self.logger.info(f"Sección: {row['section_name']}")

    def create_stories(self, stories_df: pd.DataFrame):
        for _, row in stories_df.iterrows():
            self.logger.info(f"Story: {row['story_name']} @ {row['elevation']}")

    def create_frames(self, frames_df: pd.DataFrame):
        for _, row in frames_df.iterrows():
            self.logger.info(f"Frame: {row['element_id']}")

    def create_loads(self, loads_df: pd.DataFrame):
        for _, row in loads_df.iterrows():
            self.logger.info(f"Load: {row['load_case']}")

    def create_combos(self, combos_df: pd.DataFrame):
        for _, row in combos_df.iterrows():
            self.logger.info(f"Combo: {row['combo_name']}")