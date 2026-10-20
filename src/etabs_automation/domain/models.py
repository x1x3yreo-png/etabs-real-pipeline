from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Dict, Any


@dataclass
class Material:
    material_name: str
    E: float
    nu: float
    gamma: float


@dataclass
class Section:
    section_name: str
    material_name: str
    shape: str
    area: float
    b: float | None = None
    h: float | None = None
    diameter: float | None = None


@dataclass
class Story:
    story_name: str
    elevation: float


@dataclass
class Grid:
    grid_name: str
    x: float
    y: float
    direction: str


@dataclass
class Frame:
    frame_id: str
    story: str
    start_node: str
    end_node: str
    section_name: str


@dataclass
class LoadCase:
    load_case: str
    element_id: str
    type: str
    value: float
    direction: str


@dataclass
class LoadCombo:
    combo_name: str
    case_name: str
    factor: float


@dataclass
class StructuralModel:
    materials: List[Material] = field(default_factory=list)
    sections: List[Section] = field(default_factory=list)
    stories: List[Story] = field(default_factory=list)
    grids: List[Grid] = field(default_factory=list)
    frames: List[Frame] = field(default_factory=list)
    loads: List[LoadCase] = field(default_factory=list)
    combos: List[LoadCombo] = field(default_factory=list)


@dataclass
class DriftCheckResult:
    story: str
    drift: float
    limit: float
    status: str


@dataclass
class SectionCheckResult:
    element_id: str
    ratio: float
    limit: float
    status: str