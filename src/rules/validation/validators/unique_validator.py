"""
============================================================
InsightForge Sentinel
Unique Validator
============================================================

Purpose:
    Validates that a column contains unique values.

Author : InsightForge
Version : 2.0
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

        duplicates = knowledge.get_fact(
            column,
            "duplicate_values",
            0
        )

        if duplicates == 0:

            status = "PASS"

            message = "No duplicate values found."

            failed_count = 0

            failed_rows = []

            failed_values = []

        else:

            status = "FAIL"

            message = (
                f"{duplicates} duplicate value(s) found."
            )

            failed_count = duplicates

            # Will be implemented in Sprint 11
            failed_rows = []

            # Will be implemented in Sprint 11
            failed_values = []

        # ==================================================
        # Result
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