"""
============================================================
InsightForge Sentinel
Rule Model
============================================================

Purpose:
    Represents a validation rule used by the Rule Engine.

Author : InsightForge
Version: 1.0
"""


class Rule:
    """
    Domain model representing a validation rule.

    Rules are loaded from JSON rule packs and executed
    by the Rule Engine.
    """

    def __init__(
        self,
        rule_id,
        name,
        business_type,
        validation,
        severity,
        business_impact,
        recommendation,
        enabled=True,
        version="1.0"
    ):

        self.rule_id = rule_id

        self.name = name

        self.business_type = business_type

        self.validation = validation

        self.severity = severity

        self.business_impact = business_impact

        self.recommendation = recommendation

        self.enabled = enabled

        self.version = version

    # ======================================================
    # Utility
    # ======================================================

    def is_enabled(self):

        return self.enabled

    def to_dict(self):

        return {

            "rule_id": self.rule_id,

            "name": self.name,

            "business_type": self.business_type,

            "validation": self.validation,

            "severity": self.severity,

            "business_impact": self.business_impact,

            "recommendation": self.recommendation,

            "enabled": self.enabled,

            "version": self.version

        }

    def __repr__(self):

        return (
            f"Rule("
            f"{self.rule_id}, "
            f"{self.name}, "
            f"{self.business_type})"
        )