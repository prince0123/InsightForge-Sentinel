"""
Priority Engine
"""

from health.improvement.config.improvement_weights import (
    SEVERITY_WEIGHT
)


class PriorityEngine:

    def calculate(
        self,
        severity,
        affected_rows,
        trust_gain
    ):

        severity_score = SEVERITY_WEIGHT.get(
            severity.upper(),
            1
        )

        return round(

            severity_score
            *
            max(1, affected_rows)
            *
            trust_gain,

            2

        )