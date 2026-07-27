"""
============================================================
InsightForge Sentinel
Improvement Plan
============================================================
"""

from dataclasses import dataclass, field

from health.improvement.models.improvement import (
    Improvement
)


@dataclass(slots=True)
class ImprovementPlan:

    current_score: float

    projected_score: float

    improvements: list[Improvement] = field(
        default_factory=list
    )