from __future__ import annotations

from typing import Dict, List


class DriftChecker:
    def __init__(self, story_results: Dict[str, float]):
        self.story_results = story_results

    def check_story_drift(self, limit: float = 0.005) -> List[dict]:
        violations = []
        for story, drift in self.story_results.items():
            status = "OK" if drift <= limit else "NO CUMPLE"
            violations.append({
                "story": story,
                "drift": drift,
                "limit": limit,
                "status": status,
            })
        return violations