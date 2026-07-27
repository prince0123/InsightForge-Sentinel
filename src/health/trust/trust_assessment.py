"""
============================================================
InsightForge Sentinel
Trust Assessment
============================================================

Purpose:
    Represents Sentinel's overall business assessment of
    dataset trustworthiness.

Author : InsightForge
Version : 1.0
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class TrustAssessment:

    # =====================================================
    # Core Trust
    # =====================================================

    data_trust_index: float

    dataset_grade: str

    risk_level: str

    # =====================================================
    # Readiness
    # =====================================================

    production_ready: bool

    analytics_ready: bool

    ai_ready: bool

    # =====================================================
    # Dataset Summary
    # =====================================================

    rows: int

    columns: int

    # =====================================================
    # Rule Summary
    # =====================================================

    rules_executed: int

    passed_rules: int

    failed_rules: int

    # =====================================================
    # Quality Metrics
    # =====================================================

    completeness: float

    uniqueness: float

    validity: float

    consistency: float

    # =====================================================
    # Insights
    # =====================================================

    top_issues: list[str] = field(default_factory=list)

    recommendations: list[str] = field(default_factory=list)

    summary: str = ""