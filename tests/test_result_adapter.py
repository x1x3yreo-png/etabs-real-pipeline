import pandas as pd

from src.etabs.results import ETABSResultsAdapter

class DummyResults:
    def __init__(self):
        self.story_data = {"Nivel 1": 0.003, "Nivel 2": 0.006}

    def StoryDrifts(self, *args, **kwargs):
        return self.story_data

class DummySap:
    def __init__(self):
        self.Results = DummyResults()

def test_story_drift_to_df():
    adapter = ETABSResultsAdapter(DummySap())
    df = adapter.story_drift_to_df()
    assert isinstance(df, pd.DataFrame)
    assert "story" in df.columns