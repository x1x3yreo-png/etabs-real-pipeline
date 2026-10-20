from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import yaml

@dataclass
class ProjectConfig:
    project_name: str
    input_dir: Path
    output_dir: Path
    drift_limit: float
    section_limit: float
    etabs_model_path: str | None
    auto_run_analysis: bool = True


def load_config(path: str | Path) -> ProjectConfig:
    with open(path, "r", encoding="utf-8") as f:
        raw = yaml.safe_load(f) or {}

    project_cfg = raw.get("project", {})
    paths_cfg = raw.get("paths", {})
    limits_cfg = raw.get("limits", {})
    etabs_cfg = raw.get("etabs", {})

    return ProjectConfig(
        project_name=project_cfg.get("name", "ETABS Automation"),
        input_dir=Path(paths_cfg.get("input_dir", "data/input")),
        output_dir=Path(paths_cfg.get("output_dir", "data/output")),
        drift_limit=float(limits_cfg.get("drift_limit", 0.005)),
        section_limit=float(limits_cfg.get("section_limit", 0.90)),
        etabs_model_path=etabs_cfg.get("model_path"),
        auto_run_analysis=bool(etabs_cfg.get("auto_run_analysis", True)),
    )