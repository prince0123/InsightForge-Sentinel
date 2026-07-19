"""
============================================================
InsightForge Sentinel
Metric Calculator
============================================================

Purpose:
    Calculates raw dataset quality metrics.

Author : InsightForge
Version : 1.0
"""


class MetricCalculator:

    # ==================================================

    def calculate(
        self,
        profile,
        validation_output
    ):

        return {

            "completeness":
                self._completeness(profile),

            "uniqueness":
                self._uniqueness(profile),

            "validity":
                self._validity(validation_output),

            "consistency":
                self._consistency(validation_output)

        }

    # ==================================================

    def _completeness(
        self,
        profile
    ):

        total = (
            profile["rows"] *
            profile["columns"]
        )

        missing = sum(
            profile["missing_values"].values()
        )

        if total == 0:

            return 100

        return round(

            ((total - missing) / total)

            * 100,

            2

        )

    # ==================================================

    def _uniqueness(
        self,
        profile
    ):

        rows = profile["rows"]

        duplicates = profile["duplicate_rows"]

        if rows == 0:

            return 100

        return round(

            ((rows - duplicates) / rows)

            * 100,

            2

        )

    # ==================================================

    def _validity(
        self,
        validation_output
    ):

        executed = validation_output[
            "rules_executed"
        ]

        failed = validation_output[
            "failed"
        ]

        if executed == 0:

            return 100

        return round(

            ((executed - failed) / executed)

            * 100,

            2

        )

    # ==================================================

    def _consistency(
        self,
        validation_output
    ):

        # Sprint 11

        return 100