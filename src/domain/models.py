from dataclasses import dataclass

@dataclass
class Material:
    material_name: str
    material_type: str
    E: float
    nu: float
    gamma: float
    fy: float | None = None
    fc: float | None = None
    code: str | None = None

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
class Frame:
    element_id: str
    section_name: str
    material_name: str
    start_x: float
    start_y: float
    start_z: float
    end_x: float
    end_y: float
    end_z: float