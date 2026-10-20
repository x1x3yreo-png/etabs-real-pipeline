from pathlib import Path
import json
import pandas as pd
import logging

from src.etabs.client import ETABSClient
from src.etabs.builder import ETABSBuilder
from src.etabs.checks import StructuralChecks
from src.etabs.results import ETABSResultAdapter

class ETABSPipeline:
    def __init__(self, input_dir: str, output_dir: str):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.logger = logging.getLogger(__name__)

    def run(self):
        revit_path = Path(self.input_dir) / "revit_export.xlsx"
        if not revit_path.exists():
            raise FileNotFoundError(f"No existe {revit_path}. Exporta desde Revit antes de ejecutar.")

        frames_df = pd.read_excel(revit_path)
        if frames_df.empty:
            raise ValueError("El export desde Revit está vacío.")

        materials_df = pd.read_excel(Path(self.input_dir) / "materials.xlsx")
        sections_df = pd.read_excel(Path(self.input_dir) / "sections.xlsx")
        stories_df = pd.read_excel(Path(self.input_dir) / "stories.xlsx")
        loads_df = pd.read_excel(Path(self.input_dir) / "loads.xlsx")
        combos_df = pd.read_excel(Path(self.input_dir) / "combos.xlsx")

        client = ETABSClient()
        etabs = client.connect()
        sap = client.get_sap_model()

        builder = ETABSBuilder(sap)
        builder.initialize_new_model()
        builder.add_materials(materials_df)
        builder.add_sections(sections_df)
        builder.add_stories(stories_df)

        grids_df = pd.DataFrame([
            {"grid_name": "A", "x": 0, "y": 0, "direction": "X"},
            {"grid_name": "B", "x": 6, "y": 0, "direction": "X"},
            {"grid_name": "1", "x": 0, "y": 0, "direction": "Y"},
            {"grid_name": "2", "x": 0, "y": 6, "direction": "Y"},
        ])
        builder.add_grids(grids_df)
        builder.add_frames_from_revit_export(frames_df)
        builder.add_load_cases(loads_df)
        builder.add_load_combos(combos_df)

        # builder.run_analysis()

        adapter = ETABSResultAdapter(sap)
        drift_df = adapter.story_drift_to_df()
        frame_force_df = adapter.frame_force_to_df()
        joint_disp_df = adapter.joint_displacement_to_df()

        checker = StructuralChecks(drift_limit=0.005, section_limit=0.90)

        section_df = pd.DataFrame([
            {"element_id": "C1-01", "ratio": 0.88},
            {"element_id": "V1-02", "ratio": 0.92},
            {"element_id": "COL1-03", "ratio": 0.74},
        ])

        drift_report = checker.check_drift(drift_df)
        section_report = checker.check_section(section_df)

        out_dir = Path(self.output_dir)
        out_dir.mkdir(parents=True, exist_ok=True)

        if not drift_report.empty:
            drift_report.to_excel(out_dir / "drift_report.xlsx", index=False)

        if not section_report.empty:
            section_report.to_excel(out_dir / "section_report.xlsx", index=False)

        if not frame_force_df.empty:
            frame_force_df.to_excel(out_dir / "frame_force_report.xlsx", index=False)

        if not joint_disp_df.empty:
            joint_disp_df.to_excel(out_dir / "joint_displacement_report.xlsx", index=False)

        summary = {
            "drift_report": str(out_dir / "drift_report.xlsx") if not drift_report.empty else None,
            "section_report": str(out_dir / "section_report.xlsx") if not section_report.empty else None,
            "frame_force_report": str(out_dir / "frame_force_report.xlsx") if not frame_force_df.empty else None,
            "joint_displacement_report": str(out_dir / "joint_displacement_report.xlsx") if not joint_disp_df.empty else None,
            "checks": {
                "drift": drift_report.to_dict(orient="records"),
                "sections": section_report.to_dict(orient="records"),
            }
        }

        with open(out_dir / "summary.json", "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)

        return summary