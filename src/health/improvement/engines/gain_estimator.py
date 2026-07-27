"""
Gain Estimator
"""

from health.improvement.config.improvement_weights import (
    GAIN_TABLE
)


class GainEstimator:

    def estimate(
        self,
        validation
    ):

        return GAIN_TABLE.get(
            validation.upper(),
            1.0
        )