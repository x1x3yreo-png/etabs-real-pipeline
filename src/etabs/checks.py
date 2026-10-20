import pandas as pd

class StructuralChecks:
    def __init__(self, drift_limit=0.005, section_limit=0.90):
        self.drift_limit = drift_limit
        self.section_limit = section_limit

    def check_drift(self, drift_df: pd.DataFrame) -> pd.DataFrame:
        if drift_df.empty:
            return pd.DataFrame(columns=["story", "drift", "limit", "status"])

        result = drift_df.copy()
        result["limit"] = self.drift_limit
        result["status"] = result["drift"].apply(
            lambda x: "OK" if float(x) <= self.drift_limit else "NO CUMPLE"
        )
        return result

    def check_section(self, section_df: pd.DataFrame) -> pd.DataFrame:
        if section_df.empty:
            return pd.DataFrame(columns=["element_id", "ratio", "limit", "status"])

        result = section_df.copy()
        result["limit"] = self.section_limit
        result["status"] = result["ratio"].apply(
            lambda x: "OK" if float(x) <= self.section_limit else "NO CUMPLE"
        )
        return result