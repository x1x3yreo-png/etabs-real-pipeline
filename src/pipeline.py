from __future__ import annotations

import logging

from src.config import OUTPUT_DIR, DRIFT_LIMIT_DEFAULT, SECTION_LIMIT_DEFAULT
from src.excel_loader import ExcelLoader
from src.etabs_client import ETABSClient
from src.model_builder import ModelBuilder
from src.drift_checks import DriftChecker
from src.section_checks import SectionChecker
from src.report import export_report
from src.utils import ensure_dir


class Pipeline:
    def __init__(self, base_dir: str):
        self.base_dir = base_dir
        self.output_dir = OUTPUT_DIR
        self.loader = ExcelLoader(f"{base_dir}/data/input")
        self.logger = logging.getLogger(__name__)

    def run(self):
        self.logger.info("Cargando archivos Excel...")
        data = self.loader.load_all()

        ensure_dir(self.output_dir)

        self.logger.info("Conectando con ETABS...")
        etabs = ETABSClient()
        sap_model = etabs.connect()

        builder = ModelBuilder(sap_model)
        builder.create_materials(data["materials"])
        builder.create_sections(data["sections"])
        builder.create_stories(data["stories"])
        builder.create_grids(data["grids"])
        builder.create_frames(data["frames"])
        builder.create_load_cases(data["loads"])
        builder.create_combos(data["combos"])

        self.logger.info("Ejecutando análisis...")
        etabs.run_analysis()

        # Estos resultados normalmente se extraen de ETABS.
        # Aquí se usan como ejemplo para la validación automática.
        story_results = {
            "Story 1": 0.0032,
            "Story 2": 0.0046,
            "Story 3": 0.0061,
        }

        element_ratios = {
            "C1-01": 0.88,
            "V1-05": 0.94,
            "C2-07": 0.67,
        }

        drift_checker = DriftChecker(story_results)
        section_checker = SectionChecker(element_ratios)

        drift_violations = drift_checker.check_story_drift(limit=DRIFT_LIMIT_DEFAULT)
        section_violations = section_checker.check_utilization(limit=SECTION_LIMIT_DEFAULT)

        drift_path = export_report(drift_violations, "drift_report.xlsx", str(self.output_dir))
        section_path = export_report(section_violations, "section_report.xlsx", str(self.output_dir))

        self.logger.info(f"Reporte drift: {drift_path}")
        self.logger.info(f"Reporte sección: {section_path}")

        return {
            "drift_report": drift_path,
            "section_report": section_path,
            "story_results": story_results,
            "element_ratios": element_ratios,
            "drift_violations": drift_violations,
            "section_violations": section_violations,
        }