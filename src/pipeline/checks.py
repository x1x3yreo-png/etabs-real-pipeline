import pandas as pd

class StructuralChecks:
    def __init__(self, drift_limit=0.005, section_limit=0.90):
        self.drift_limit = drift_limit
        self.section_limit = section_limit

    def check_story_drift(self, drift_df: pd.DataFrame):
        if drift_df.empty:
            return pd.DataFrame(columns=["story", "drift", "limit", "status"])
        df = drift_df.copy()
        df["limit"] = self.drift_limit
        df["status"] = df["drift"].apply(lambda x: "OK" if float(x) <= self.drift_limit else "NO CUMPLE")
        return df

    def check_section_utilization(self, section_df: pd.DataFrame):
        if section_df.empty:
            return pd.DataFrame(columns=["element_id", "ratio", "limit", "status"])
        df = section_df.copy()
        df["limit"] = self.section_limit
        df["status"] = df["ratio"].apply(lambda x: "OK" if float(x) <= self.section_limit else "NO CUMPLE")
        return df