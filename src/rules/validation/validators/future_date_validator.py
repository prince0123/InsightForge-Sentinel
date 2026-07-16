"""
============================================================
InsightForge Sentinel
Future Date Validator
============================================================

Purpose:
    Validates that dates are not in the future.

Author : InsightForge
Version : 1.0
"""

import pandas as pd

from datetime import datetime

from models.validation_result import ValidationResult
from rules.validation.base_validator import BaseValidator


class FutureDateValidator(BaseValidator):

    def validate(
        self,
        dataframe,
        knowledge,
        task
    ):

        column = task.column
        rule = task.rule

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

            failed_count=failed_count,

            failed_rows=failed_rows,

            failed_values=failed_values

        )