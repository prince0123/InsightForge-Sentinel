"""
============================================================
InsightForge Sentinel
Email Validator
============================================================

Purpose:
    Validates email address format.

Author : InsightForge
Version : 2.0
"""

import re
import pandas as pd

from models.validation_result import ValidationResult
from rules.validation.base_validator import BaseValidator


class EmailValidator(BaseValidator):

    EMAIL_PATTERN = re.compile(
        r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    )

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

        failed_rows = []
        failed_values = []

        series = dataframe[column]

        for index, value in series.items():

            if pd.isna(value):
                continue

            value = str(value).strip()

            if value == "":
                continue

            if not self.EMAIL_PATTERN.fullmatch(value):

                failed_rows.append(index + 1)
                failed_values.append(value)

        failed_count = len(failed_rows)

        if failed_count == 0:

            status = "PASS"

            message = "All email addresses are valid."

        else:

            status = "FAIL"

            message = (
                f"{failed_count} invalid email address(es) found."
            )

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