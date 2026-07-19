"""
============================================================
InsightForge Sentinel
Default Scoring Policy
============================================================

Purpose:
    Applies Sentinel's default scoring policy to dataset
    quality metrics.

Author : InsightForge
Version : 2.0
"""

from health.policies.base_scoring_policy import (
    BaseScoringPolicy
)

class DefaultScoringPolicy(BaseScoringPolicy):

    # ==================================================
    # Constructor
    # ==================================================

    def __init__(
    self,
    config
    ):
        
        self.weights = config.health_weights
        
        self.risk_levels = config.risk_levels

    # ==================================================
    # Overall Score
    # ==================================================

    def overall_score(
        self,
        metrics
    ):

        score = (

            metrics["completeness"]
            * self.weights["completeness"]

            +

            metrics["uniqueness"]
            * self.weights["uniqueness"]

            +

            metrics["validity"]
            * self.weights["validity"]

            +

            metrics["consistency"]
            * self.weights["consistency"]

        )

        return round(score, 2)

    # ==================================================
    # Risk Level
    # ==================================================

    def risk_level(
        self,
        score
    ):

        for level, threshold in self.risk_levels.items():

            if score >= threshold:

                return level

        return "CRITICAL"

    # ==================================================
    # Summary
    # ==================================================

    def summary(
        self,
        score
    ):

        risk = self.risk_level(score)

        summaries = {

            "LOW": (
                "Dataset is healthy and ready "
                "for production use."
            ),

            "MEDIUM": (
                "Dataset is suitable for analytics "
                "after resolving identified issues."
            ),

            "HIGH": (
                "Dataset requires data quality "
                "improvements before use."
            ),

            "CRITICAL": (
                "Dataset is not suitable for "
                "production until critical "
                "issues are resolved."
            )

        }

        return summaries[risk]