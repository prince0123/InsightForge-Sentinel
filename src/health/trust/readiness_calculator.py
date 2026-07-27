"""
============================================================
InsightForge Sentinel
Readiness Calculator
============================================================
"""


class ReadinessCalculator:

    def production_ready(
        self,
        validation_output
    ) -> bool:

        for result in validation_output["results"]:

            if (
                result.status == "FAIL"
                and result.severity.upper() == "HIGH"
            ):
                return False

        return True

    # -----------------------------------------------------

    def analytics_ready(
        self,
        health_score
    ) -> bool:

        return health_score.overall_score >= 75

    # -----------------------------------------------------

    def ai_ready(
        self,
        health_score
    ) -> bool:

        return health_score.overall_score >= 90