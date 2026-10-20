from __future__ import annotations

from etabs_automation.domain.models import DriftCheckResult, SectionCheckResult


def parse_story_drift(raw_story_data: dict) -> list[DriftCheckResult]:
    results = []
    for story, drift in raw_story_data.items():
        status = "OK" if drift <= 0.005 else "NO CUMPLE"
        results.append(DriftCheckResult(story=story, drift=float(drift), limit=0.005, status=status))
    return results


def parse_section_ratios(raw_section_data: dict) -> list[SectionCheckResult]:
    results = []
    for element, ratio in raw_section_data.items():
        status = "OK" if ratio <= 0.90 else "NO CUMPLE"
        results.append(SectionCheckResult(element_id=element, ratio=float(ratio), limit=0.90, status=status))
    return results