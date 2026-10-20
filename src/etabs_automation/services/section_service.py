from __future__ import annotations

from etabs_automation.domain.models import SectionCheckResult


class SectionService:
    def __init__(self, section_limit: float):
        self.section_limit = section_limit

    def evaluate(self, element_ratios: dict[str, float]) -> list[SectionCheckResult]:
        results = []
        for element_id, ratio in element_ratios.items():
            status = "OK" if ratio <= self.section_limit else "NO CUMPLE"
            results.append(
                SectionCheckResult(
                    element_id=element_id,
                    ratio=float(ratio),
                    limit=self.section_limit,
                    status=status,
                )
            )
        return results