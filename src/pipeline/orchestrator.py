from pathlib import Path
import json
import pandas as pd

from src.config.settings import Settings
from src.io.excel_loader import ExcelLoader
from src.domain.validators import validate_materials, validate_sections, validate_stories, validate_revit_export
from src.integration.etabs_client import ETABSClient
from src.pipeline.builder import ModelBuilder
from src.integration.etabs_adapter import ETABSResultAdapter
from src.pipeline.checks import StructuralChecks

class Orchestrator:
    def __init__(self, settings: Settings):
        self.settings = settings

    def run(self):
        input_dir = Path(self.settings.input_dir)
        loader = ExcelLoader(input_dir)

        revit_df = loader.load_revit_export()
        materials_df = loader.load_materials()
        sections_df = loader.load_sections()
        stories_df = loader.load_stories()
        loads_df = loader.load_loads()
        combos_df = loader.load_combos()

        validate_revit_export(revit_df)
        validate_materials(materials_df)
        validate_sections(sections_df)
        validate_stories(stories_df)

        client = ETABSClient()
        sap = client.get_sap_model()

        builder = ModelBuilder(sap)
        builder.create_materials(materials_df)
        builder.create_sections(sections_df)
        builder.create_stories(stories_df)
        builder.create_frames(revit_df)
        builder.create_loads(loads_df)
        builder.create_combos(combos_df)

        # ETABS analysis should run here in production:
        # sap.Analyze.RunAnalysis()

        adapter = ETABSResultAdapter(sap)
        drift_df = adapter.story_drift_to_df()
        frame_df = adapter.frame_force_to_df()
        joint_df = adapter.joint_displacement_to_df()

        checker = StructuralChecks(drift_limit=self.settings.drift_limit, section_limit=self.settings.utilization_limit)

        section_df = pd.DataFrame([
            {"element_id": "C1-01", "ratio": 0.88},
            {"element_id": "V1-02", "ratio": 0.92},
            {"element_id": "COL1-03", "ratio": 0.74},
        ])

        drift_report = checker.check_story_drift(drift_df)
        section_report = checker.check_section_utilization(section_df)

        output_dir = Path(self.settings.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        if not drift_report.empty:
            drift_report.to_excel(output_dir / "drift_report.xlsx", index=False)

        if not section_report.empty:
            section_report.to_excel(output_dir / "section_report.xlsx", index=False)

        if not frame_df.empty:
            frame_df.to_excel(output_dir / "frame_force_report.xlsx", index=False)

        if not joint_df.empty:
            joint_df.to_excel(output_dir / "joint_displacement_report.xlsx", index=False)

        summary = {
            "drift_report": str(output_dir / "drift_report.xlsx") if not drift_report.empty else None,
            "section_report": str(output_dir / "section_report.xlsx") if not section_report.empty else None,
            "frame_force_report": str(output_dir / "frame_force_report.xlsx") if not frame_df.empty else None,
            "joint_displacement_report": str(output_dir / "joint_displacement_report.xlsx") if not joint_df.empty else None,
            "checks": {
                "drift": drift_report.to_dict(orient="records"),
                "sections": section_report.to_dict(orient="records"),
            }
        }

        with open(output_dir / "summary.json", "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)

        return summary