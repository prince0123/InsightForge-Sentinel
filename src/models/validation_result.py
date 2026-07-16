"""
============================================================
InsightForge Sentinel
Validation Result Model
============================================================

Purpose:
    Represents the outcome of a single validation rule.

Author : InsightForge
Version : 1.0
"""


class ValidationResult:

    def __init__(
        self,
        rule_id,
        rule_name,
        column,
        business_type,
        validation,
        severity,
        status,
        message,
        recommendation,
        business_impact,
        failed_count=0,
        failed_rows=None,
        failed_values=None
    ):

        self.rule_id = rule_id
        self.rule_name = rule_name
        self.column = column
        self.business_type = business_type
        self.validation = validation
        self.severity = severity

        self.status = status
        self.message = message

        self.recommendation = recommendation
        self.business_impact = business_impact

        self.failed_count = failed_count
        self.failed_rows = failed_rows or []
        self.failed_values = failed_values or []

    # ======================================================
    # Status Helpers
    # ======================================================

    def is_pass(self):

        return self.status == "PASS"

    def is_fail(self):

        return self.status == "FAIL"

    def is_not_implemented(self):

        return self.status == "NOT_IMPLEMENTED"

    # ======================================================
    # Dictionary Representation
    # ======================================================

    def to_dict(self):

        return {

            "rule_id": self.rule_id,

            "rule_name": self.rule_name,

            "column": self.column,

            "business_type": self.business_type,

            "validation": self.validation,

            "severity": self.severity,

            "status": self.status,

            "message": self.message,

            "recommendation": self.recommendation,

            "business_impact": self.business_impact,

            "failed_count": self.failed_count,

            "failed_rows": self.failed_rows,

            "failed_values": self.failed_values

        }

    # ======================================================
    # String Representation
    # ======================================================

    def __repr__(self):

        return (

            f"ValidationResult("
            f"{self.column}, "
            f"{self.validation}, "
            f"{self.status}"
            f")"

        )
