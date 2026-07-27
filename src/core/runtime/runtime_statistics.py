"""
============================================================
Runtime Statistics
============================================================
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class RuntimeStatistics:

    total_runtime: float = 0

    stages: dict = field(default_factory=dict)

    warnings: int = 0

    errors: int = 0

    successful_stages: int = 0

    failed_stages: int = 0