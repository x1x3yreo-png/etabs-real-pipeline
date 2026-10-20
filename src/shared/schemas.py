from dataclasses import dataclass

@dataclass
class MaterialEntry:
    material_name: str
    E: float
    nu: float
    gamma: float

@dataclass
class SectionEntry:
    section_name: str
    material_name: str
    shape: str
    area: float
    b: float | None = None
    h: float | None = None
    diameter: float | None = None

@dataclass
class StoryEntry:
    story_name: str
    elevation: float

@dataclass
class GridEntry:
    grid_name: str
    x: float
    y: float
    direction: str

@dataclass
class FrameEntry:
    element_id: str
    section_name: str
    material_name: str
    level_name: str
    start_x: float
    start_y: float
    start_z: float
    end_x: float
    end_y: float
    end_z: float