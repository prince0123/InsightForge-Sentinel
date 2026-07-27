"""
============================================================
Stage Result
============================================================
"""

from dataclasses import dataclass


@dataclass(slots=True)
class StageResult:

    stage: str

    status: str

    elapsed_seconds: float

    message: str