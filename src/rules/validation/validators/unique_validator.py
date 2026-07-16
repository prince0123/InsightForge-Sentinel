"""
============================================================
InsightForge Sentinel
Unique Validator
============================================================

Purpose:
    Validates that a column contains unique values.

Author : InsightForge
Version : 1.0
"""

from models.validation_result import ValidationResult
from rules.validation.base_validator import BaseValidator


class UniqueValidator(BaseValidator):

    def validate(
        self,
        dataframe,
        knowledge,
        task
    ):

        column = task.column
        rule = task.rule

        duplicates = knowledge.get_fact(
            column,
            "duplicate_values",
            0
        )

        if duplicates == 0:

            status = "PASS"

            message = "No duplicate values found."

        else:

            status = "FAIL"

            message = (
                f"{duplicates} duplicate value(s) found."
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

            failed_count=duplicates

        )