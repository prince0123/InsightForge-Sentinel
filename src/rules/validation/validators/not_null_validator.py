"""
============================================================
InsightForge Sentinel
Not Null Validator
============================================================

Purpose:
    Validates that a column contains no NULL values.

Author : InsightForge
Version : 1.0
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

        column = task.column
        rule = task.rule

        nulls = knowledge.get_fact(
            column,
            "null_values",
            0
        )

        if nulls == 0:

            status = "PASS"

            message = "No NULL values found."

        else:

            status = "FAIL"

            message = (
                f"{nulls} NULL value(s) found."
            )

        return ValidationResult(

            rule_id=rule.rule_id,

            rule_name=rule.name,

            column=column,

            business_type=task.business_type,

            validation=rule.validation,

            severity=rule.severity,

            status=status,

            message=message,

            recommendation=rule.recommendation,

            business_impact=rule.business_impact,

            failed_count=nulls

        )