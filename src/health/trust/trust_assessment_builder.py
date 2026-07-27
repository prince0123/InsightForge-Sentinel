"""
============================================================
InsightForge Sentinel
Trust Assessment Builder
============================================================

Purpose:
    Builds a business-level TrustAssessment object from
    profiling, validation and health results.

Author : InsightForge
Version : 1.0
"""

from health.trust.grade_calculator import GradeCalculator
from health.trust.readiness_calculator import ReadinessCalculator
from health.trust.trust_assessment import TrustAssessment


class TrustAssessmentBuilder:

    def __init__(self):

        self.grade_calculator = GradeCalculator()

        self.readiness_calculator = ReadinessCalculator()

    # =====================================================

    def build(
        self,
        profile,
        validation_output,
        health_score
    ) -> TrustAssessment:

        return TrustAssessment(

            data_trust_index=health_score.overall_score,

            dataset_grade=self.grade_calculator.calculate(
                health_score.overall_score
            ),

            risk_level=health_score.risk_level,

            production_ready=self.readiness_calculator.production_ready(
                validation_output
            ),

            analytics_ready=self.readiness_calculator.analytics_ready(
                health_score
            ),

            ai_ready=self.readiness_calculator.ai_ready(
                health_score
            ),

            rows=profile["rows"],

            columns=profile["columns"],

            rules_executed=validation_output["rules_executed"],

            passed_rules=validation_output["passed"],

            failed_rules=validation_output["failed"],

            completeness=health_score.completeness,

            uniqueness=health_score.uniqueness,

            validity=health_score.validity,

            consistency=health_score.consistency,

            top_issues=list(health_score.issues),

            recommendations=[],

            summary=health_score.summary
        )