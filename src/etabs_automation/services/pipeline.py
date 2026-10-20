from __future__ import annotations

import logging
from pathlib import Path

from etabs_automation.config import ProjectConfig
from etabs_automation.domain.models import StructuralModel
from etabs_automation.io.excel_loader import ExcelLoader
from etabs_automation.io.report_writer import write_excel, write_json
from etabs_automation.etabs.client import ETABSClient
from etabs_automation.services.drift_service import DriftService
from etabs_automation.services.model_service import ModelService
from etabs_automation.services.section_service import SectionService


class Pipeline:
    def __init__(self, config: ProjectConfig):
        self.config = config
        self.logger = logging.getLogger(__name__)

    def run(self) -> dict:
        self.logger.info("Cargando modelo desde Excel...")
        loader = ExcelLoader(self.config.input_dir)
        model = loader.load_model()

        self.logger.info("Conectando al ETABS...")
        client = ETABSClient()
        client.connect()

        self.logger.info("Generando modelo ETABS...")
        model_service = ModelService(client)
        model_service.generate_model(model)

        if self.config.auto_run_analysis:
            self.logger.info("Ejecutando análisis...")
            client.run_analysis()

        # Datos de ejemplo para chequeo; idealmente se obtendrían de ETABS directamente
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

        drift_service = DriftService(self.config.drift_limit)
        section_service = SectionService(self.config.section_limit)

        drift_results = drift_service.evaluate(story_results)
        section_results = section_service.evaluate(element_ratios)

        drift_path = write_excel(
            [r.__dict__ for r in drift_results],
            Path(self.config.output_dir) / "drift_report.xlsx",
        )
        section_path = write_excel(
            [r.__dict__ for r in section_results],
            Path(self.config.output_dir) / "section_report.xlsx",
        )

        summary = {
            "drift_limit": self.config.drift_limit,
            "section_limit": self.config.section_limit,
            "drift_results": [r.__dict__ for r in drift_results],
            "section_results": [r.__dict__ for r in section_results],
        }

        write_json(summary, Path(self.config.output_dir) / "summary.json")

        return {
            "drift_report": str(drift_path),
            "section_report": str(section_path),
            "summary": summary,
        }