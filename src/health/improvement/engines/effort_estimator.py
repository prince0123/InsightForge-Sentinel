"""
Effort Estimator
"""

from health.improvement.config.improvement_weights import (
    EFFORT_TABLE
)


class EffortEstimator:

    def estimate(
        self,
        validation
    ):

        return EFFORT_TABLE.get(
            validation.upper(),
            5
        )