"""
============================================================
Improvement Intelligence Engine
============================================================
"""

from health.improvement.engines.recommendation_engine import (
    RecommendationEngine
)

from health.improvement.models.improvement_plan import (
    ImprovementPlan
)


class ImprovementEngine:

    def __init__(self):

        self.recommendation_engine = (
            RecommendationEngine()
        )

    # ==================================================

    def run(
        self,
        validation_output,
        health_score
    ):

        improvements = []

        for result in validation_output["results"]:

            if result.status != "FAIL":
                continue

            improvements.append(

                self.recommendation_engine.build(
                    result
                )

            )

        improvements.sort(

            key=lambda x: x.priority_score,

            reverse=True

        )

        projected_score = min(

            100,

            health_score.overall_score
            +

            sum(

                item.estimated_trust_gain

                for item in improvements

            )

        )

        return ImprovementPlan(

            current_score=health_score.overall_score,

            projected_score=round(
                projected_score,
                2
            ),

            improvements=improvements

        )