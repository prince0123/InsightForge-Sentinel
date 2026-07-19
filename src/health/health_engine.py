"""
============================================================
InsightForge Sentinel
Health Engine
============================================================

Purpose:
    Coordinates dataset health analysis by delegating
    metric calculation and scoring to specialized
    components.

Author : InsightForge
Version : 3.0
"""

from health.health_score import HealthScore
from health.metric_calculator import MetricCalculator
from health.default_scoring_policy import (
    DefaultScoringPolicy
)

from services.configuration_service import (
    ConfigurationService
)


class HealthEngine:

    # ==================================================
    # Constructor
    # ==================================================

    def __init__(self):
        
        self.config = ConfigurationService()

        self.calculator = MetricCalculator()

        self.policy = DefaultScoringPolicy(
        
        self.config
        
        )

    # ==================================================
    # Run Health Engine
    # ==================================================

    def run(
        self,
        profile,
        validation_output
    ):

        # ----------------------------------------------
        # Calculate Dataset Metrics
        # ----------------------------------------------

        metrics = self.calculator.calculate(
            profile,
            validation_output
        )

        # ----------------------------------------------
        # Apply Scoring Policy
        # ----------------------------------------------

        overall = self.policy.overall_score(
            metrics
        )

        risk = self.policy.risk_level(
            overall
        )

        summary = self.policy.summary(
            overall
        )

        # ----------------------------------------------
        # Collect Issues
        # ----------------------------------------------

        issues = self._collect_issues(
            profile,
            validation_output
        )

        # ----------------------------------------------
        # Build Health Score
        # ----------------------------------------------

        return HealthScore(

            overall_score=overall,

            completeness=metrics["completeness"],

            uniqueness=metrics["uniqueness"],

            validity=metrics["validity"],

            consistency=metrics["consistency"],

            risk_level=risk,

            issues=issues,

            summary=summary

        )

    # ==================================================
    # Collect Issues
    # ==================================================

    def _collect_issues(
        self,
        profile,
        validation_output
    ):

        issues = []

        if profile["duplicate_rows"] > 0:

            issues.append(
                f"{profile['duplicate_rows']} duplicate row(s)"
            )

        for column, count in profile[
            "missing_values"
        ].items():

            if count > 0:

                issues.append(
                    f"{count} missing value(s) in {column}"
                )

        for result in validation_output["results"]:

            if result.status == "FAIL":

                issues.append(
                    result.message
                )

        return issues