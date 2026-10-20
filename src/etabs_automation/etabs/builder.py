from __future__ import annotations

import logging
from typing import Any

from etabs_automation.domain.models import StructuralModel


class ETABSBuilder:
    def __init__(self, sap_model: Any):
        self.sap = sap_model
        self.logger = logging.getLogger(__name__)

    def build(self, model: StructuralModel):
        self._create_materials(model)
        self._create_sections(model)
        self._create_stories(model)
        self._create_grids(model)
        self._create_frames(model)
        self._create_loads(model)
        self._create_combos(model)

    def _create_materials(self, model: StructuralModel):
        for m in model.materials:
            # Pseudocódigo según ETABS
            # self.sap.PropMaterial.AddMaterial(m.material_name, "Concrete")
            # self.sap.PropMaterial.SetMaterial(...)
            self.logger.debug(f"Material creado: {m.material_name}")

    def _create_sections(self, model: StructuralModel):
        for s in model.sections:
            # Pseudocódigo según ETABS
            # self.sap.PropFrame.SetRectangle(...)
            self.logger.debug(f"Sección creada: {s.section_name}")

    def _create_stories(self, model: StructuralModel):
        for s in model.stories:
            # self.sap.Story.Setup.SetStory(s.story_name, s.elevation)
            self.logger.debug(f"Story creada: {s.story_name}")

    def _create_grids(self, model: StructuralModel):
        for g in model.grids:
            # self.sap.GridSys.SetGrid(...)
            self.logger.debug(f"Grid creada: {g.grid_name}")

    def _create_frames(self, model: StructuralModel):
        for f in model.frames:
            # self.sap.FrameObj.AddByCoord(...)
            # self.sap.FrameObj.SetSection(f.frame_id, f.section_name)
            self.logger.debug(f"Frame creada: {f.frame_id}")

    def _create_loads(self, model: StructuralModel):
        for load in model.loads:
            # self.sap.LoadCases.StaticNonlinear.Add(...)
            self.logger.debug(f"Carga creada: {load.load_case}")

    def _create_combos(self, model: StructuralModel):
        for combo in model.combos:
            # self.sap.LoadCases.LoadCombination.Add(...)
            self.logger.debug(f"Combinación creada: {combo.combo_name}")