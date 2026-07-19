"""
============================================================
InsightForge Sentinel
Health Score Model
============================================================

Purpose:
    Represents the overall health assessment of a dataset.

Author : InsightForge
Version : 1.0
"""


class HealthScore:

    def __init__(

        self,

        overall_score=100,

        completeness=100,

        uniqueness=100,

        validity=100,

        consistency=100,

        risk_level="LOW",

        issues=None,

        summary=""

    ):

        self.overall_score = overall_score

        self.completeness = completeness

        self.uniqueness = uniqueness

        self.validity = validity

        self.consistency = consistency

        self.risk_level = risk_level

        self.issues = issues or []

        self.summary = summary

    # ==================================================

    def to_dict(self):

        return {

            "overall_score": self.overall_score,

            "completeness": self.completeness,

            "uniqueness": self.uniqueness,

            "validity": self.validity,

            "consistency": self.consistency,

            "risk_level": self.risk_level,

            "issues": self.issues,

            "summary": self.summary

        }

    # ==================================================

    def __repr__(self):

        return (

            f"HealthScore("

            f"overall={self.overall_score}, "

            f"risk='{self.risk_level}')"

        )

    # ==================================================

    def __str__(self):

        return (

            f"Dataset Health "

            f"{self.overall_score}/100"

        )