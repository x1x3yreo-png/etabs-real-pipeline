import pandas as pd
import logging

logger = logging.getLogger(__name__)

class ETABSResultAdapter:
    def __init__(self, sap_model):
        self.sap = sap_model

    def _call_first_available(self, method_names, *args, **kwargs):
        for name in method_names:
            if hasattr(self.sap.Results, name):
                method = getattr(self.sap.Results, name)
                try:
                    return method(*args, **kwargs)
                except TypeError:
                    continue
        raise AttributeError(f"Ningún método disponible en SapModel.Results: {method_names}")

    def get_story_drift(self):
        candidates = ["StoryDrifts", "GetStoryDrifts", "StoryDrift", "GetStoryDrift"]
        return self._call_first_available(candidates, "ALL")

    def get_frame_forces(self):
        candidates = ["FrameForce", "GetFrameForce", "FrameForces", "GetFrameForces"]
        return self._call_first_available(candidates, "ALL")

    def get_joint_displacements(self):
        candidates = ["JointDisplacements", "GetJointDisplacements", "JointDisplacement", "GetJointDisplacement"]
        return self._call_first_available(candidates, "ALL")

    def story_drift_to_df(self):
        raw = self.get_story_drift()
        rows = []
        if isinstance(raw, dict):
            for story, drift in raw.items():
                rows.append({"story": story, "drift": float(drift)})
        elif isinstance(raw, (list, tuple)):
            for item in raw:
                if isinstance(item, dict):
                    story = item.get("Story", item.get("story"))
                    drift = item.get("Drift", item.get("drift"))
                    if story is not None:
                        rows.append({"story": story, "drift": float(drift)})
        return pd.DataFrame(rows)

    def frame_force_to_df(self):
        raw = self.get_frame_forces()
        rows = []
        if isinstance(raw, dict):
            for element_id, force in raw.items():
                rows.append({"element_id": element_id, "force": force})
        elif isinstance(raw, (list, tuple)):
            for item in raw:
                if isinstance(item, dict):
                    element_id = item.get("Element", item.get("element_id"))
                    force = item.get("Force", item.get("force"))
                    rows.append({"element_id": element_id, "force": force})
        return pd.DataFrame(rows)

    def joint_displacement_to_df(self):
        raw = self.get_joint_displacements()
        rows = []
        if isinstance(raw, dict):
            for joint, disp in raw.items():
                rows.append({"joint": joint, "disp": disp})
        elif isinstance(raw, (list, tuple)):
            for item in raw:
                if isinstance(item, dict):
                    joint = item.get("Joint", item.get("joint"))
                    disp = item.get("Displacement", item.get("disp"))
                    rows.append({"joint": joint, "disp": disp})
        return pd.DataFrame(rows)