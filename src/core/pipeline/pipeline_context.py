"""
============================================================
InsightForge Sentinel
Pipeline Context
============================================================

Purpose:
    Shared execution context passed between every stage
    of the Sentinel pipeline.

Author : InsightForge
Version : 1.0.0
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class PipelineContext:
    """
    Shared object used throughout the Sentinel pipeline.

    Every stage reads from and writes to this object.
    """

    # ==================================================
    # Input
    # ==================================================

    dataset_path: Path | None = None

    dataframe: Any = None

    # ==================================================
    # Profiling
    # ==================================================

    profile: Any = None

    # ==================================================
    # Intelligence
    # ==================================================

    knowledge: Any = None

    capabilities: Any = None

    schema_profiles: Any = None

    # ==================================================
    # Rule Engine
    # ==================================================

    execution_plan: Any = None

    # ==================================================
    # Validation
    # ==================================================

    validation_output: Any = None

    # ==================================================
    # Health
    # ==================================================

    health_score: Any = None

    trust_assessment: Any = None

    # ==================================================
    # Improvement
    # ==================================================

    improvement_plan: Any = None

    decision_plan: Any = None

    # ==================================================
    # Reporting
    # ==================================================

    report: Any = None

    # ==================================================
    # Runtime
    # ==================================================

    runtime_summary: Any = None

    elapsed_seconds: float = 0.0

    # ==================================================
    # Metadata
    # ==================================================

    version: str = "1.0.0"