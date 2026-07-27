"""
============================================================
InsightForge Sentinel
Improvement
============================================================
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Improvement:

    rule_id: str

    title: str

    severity: str

    priority_score: float

    estimated_trust_gain: float

    estimated_effort_minutes: int

    affected_rows: int

    business_impact: str

    recommendation: str