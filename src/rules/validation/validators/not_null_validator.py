"""
============================================================
InsightForge Sentinel
Not Null Validator
============================================================

Purpose:
    Validates that a column contains no NULL values.

Author : InsightForge
Version : 2.0
"""

from models.validation_result import ValidationResult
from rules.validation.base_validator import BaseValidator


class NotNullValidator(BaseValidator):

    def validate(
        self,
        dataframe,
        knowledge,
        task
    ):

        # ==================================================
        # Task Information
        # ==================================================

        column = task.column
        rule = task.rule

        text = self.format_rule_text(
            rule=rule,
            column=column,
            business_type=task.business_type
        )

        # ==================================================
        # Validation Logic
        # ==================================================

        nulls = knowledge.get_fact(
            column,
            "null_values",
            0
        )

        if nulls == 0:

            status = "PASS"

            message = "No NULL values found."

            failed_count = 0

            failed_rows = []

            failed_values = []

        else:

            status = "FAIL"

            message = (
                f"{nulls} NULL value(s) found."
            )

            failed_count = nulls

            # Sprint 11
            failed_rows = []

            # Sprint 11
            failed_values = []

        # ==================================================
        # Validation Result
        # ==================================================

        return ValidationResult(

            rule_id=rule.rule_id,

            rule_name=text["rule_name"],

            column=column,

            business_type=task.business_type,

            validation=rule.validation,

            severity=rule.severity,

            status=status,

            message=message,

            recommendation=text["recommendation"],

            business_impact=text["business_impact"],

            failed_count=failed_count,

            failed_rows=failed_rows,

            failed_values=failed_values

        )