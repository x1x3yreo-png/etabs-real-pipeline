import pandas as pd
from src.pipeline.checks import StructuralChecks

def test_story_drift_check():
    df = pd.DataFrame([
        {"story": "Nivel 1", "drift": 0.003},
        {"story": "Nivel 2", "drift": 0.006},
    ])
    checker = StructuralChecks()
    result = checker.check_story_drift(df)
    assert "status" in result.columns

def test_section_check():
    df = pd.DataFrame([
        {"element_id": "C1-01", "ratio": 0.88},
        {"element_id": "V1-02", "ratio": 0.92},
    ])
    checker = StructuralChecks()
    result = checker.check_section_utilization(df)
    assert "status" in result.columns