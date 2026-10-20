from __future__ import annotations

from typing import Dict, List


class SectionChecker:
    def __init__(self, element_ratios: Dict[str, float]):
        self.element_ratios = element_ratios

    def check_utilization(self, limit: float = 0.90) -> List[dict]:
        violations = []
        for element_id, ratio in self.element_ratios.items():
            status = "OK" if ratio <= limit else "NO CUMPLE"
            violations.append({
                "element_id": element_id,
                "ratio": ratio,
                "limit": limit,
                "status": status,
            })
        return violations