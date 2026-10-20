from __future__ import annotations

from etabs_automation.domain.models import DriftCheckResult


class DriftService:
    def __init__(self, drift_limit: float):
        self.drift_limit = drift_limit

    def evaluate(self, story_results: dict[str, float]) -> list[DriftCheckResult]:
        results = []
        for story, drift in story_results.items():
            status = "OK" if drift <= self.drift_limit else "NO CUMPLE"
            results.append(
                DriftCheckResult(
                    story=story,
                    drift=float(drift),
                    limit=self.drift_limit,
                    status=status,
                )
            )
        return results