"""
============================================================
InsightForge Sentinel
Base Validator
============================================================

Purpose:
    Base class for all Sentinel validators.

Author : InsightForge
Version : 1.0
"""


class BaseValidator:

    def validate(
        self,
        dataframe,
        knowledge,
        task
    ):
        """
        Execute validation.

        Every validator must return a ValidationResult.
        """

        raise NotImplementedError(
            "Validator must implement validate()."
        )
