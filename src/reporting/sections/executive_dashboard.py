"""
============================================================
InsightForge Sentinel
Executive Dashboard Model
============================================================
"""

from dataclasses import dataclass


@dataclass
class ExecutiveDashboard:

    data_trust_index: float

    dataset_grade: str

    risk_level: str

    production_ready: bool

    analytics_ready: bool

    ai_ready: bool

    rows: int

    columns: int

    rules_executed: int

    passed_rules: int

    failed_rules: int

    completeness: float

    uniqueness: float

    validity: float

    consistency: float

    top_issues: list[str]