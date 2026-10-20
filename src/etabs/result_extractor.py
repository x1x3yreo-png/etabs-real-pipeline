import pandas as pd

def extract_story_drift(story_results: dict) -> pd.DataFrame:
    rows = []
    for story, drift in story_results.items():
        rows.append({
            "story": story,
            "drift": drift,
            "status": "OK" if drift <= 0.005 else "NO CUMPLE"
        })
    return pd.DataFrame(rows)

def extract_section_utilization(element_results: dict) -> pd.DataFrame:
    rows = []
    for element, ratio in element_results.items():
        rows.append({
            "element_id": element,
            "ratio": ratio,
            "status": "OK" if ratio <= 0.90 else "NO CUMPLE"
        })
    return pd.DataFrame(rows)