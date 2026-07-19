"""
============================================================
InsightForge Sentinel
Future Date Validator
============================================================

Purpose:
    Validates that dates are not in the future.

Author : InsightForge
Version : 2.0
"""

from datetime import datetime

import pandas as pd

from models.validation_result import ValidationResult
from rules.validation.base_validator import BaseValidator


class FutureDateValidator(BaseValidator):

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

        today = pd.Timestamp(datetime.now().date())

        series = dataframe[column]

        for index, value in series.items():

            if pd.isna(value):
                continue

            try:

                date_value = pd.Timestamp(value)

                if date_value > today:

                    failed_rows.append(index + 1)
                    failed_values.append(str(date_value.date()))

            except Exception:
                continue

        failed_count = len(failed_rows)

        if failed_count == 0:

            status = "PASS"

            message = "No future dates found."

        else:

            status = "FAIL"

            message = (
                f"{failed_count} future date(s) found."
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