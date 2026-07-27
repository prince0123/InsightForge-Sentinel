"""
Recommendation Engine
"""

from health.improvement.engines.gain_estimator import (
    GainEstimator
)

from health.improvement.engines.effort_estimator import (
    EffortEstimator
)

from health.improvement.engines.priority_engine import (
    PriorityEngine
)

from health.improvement.models.improvement import (
    Improvement
)


class RecommendationEngine:

    def __init__(self):

        self.gain = GainEstimator()

        self.effort = EffortEstimator()

        self.priority = PriorityEngine()

    # ==================================================

    def build(
        self,
        validation_result
    ):

        gain = self.gain.estimate(
            validation_result.validation
        )

        effort = self.effort.estimate(
            validation_result.validation
        )

        priority = self.priority.calculate(

            validation_result.severity,

            validation_result.failed_count,

            gain

        )

        return Improvement(

            rule_id=validation_result.rule_id,

            title=validation_result.rule_name,

            severity=validation_result.severity,

            priority_score=priority,

            estimated_trust_gain=gain,

            estimated_effort_minutes=effort,

            affected_rows=validation_result.failed_count,

            business_impact=validation_result.business_impact,

            recommendation=validation_result.recommendation

        )