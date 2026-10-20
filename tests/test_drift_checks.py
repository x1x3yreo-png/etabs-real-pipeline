from src.drift_checks import DriftChecker

def test_drift_checker():
    story_results = {
        "Story 1": 0.003,
        "Story 2": 0.009
    }
    checker = DriftChecker(story_results)
    result = checker.check_story_drift(limit=0.005)
    assert any(item["status"] == "NO CUMPLE" for item in result)