"""
============================================================
InsightForge Sentinel
Validator Registry
============================================================

Purpose:
    Maintains mapping between validation names
    and validator implementations.

Author : InsightForge
Version : 1.4
"""

from rules.validation.validators.unique_validator import UniqueValidator
from rules.validation.validators.not_null_validator import NotNullValidator
from rules.validation.validators.positive_validator import PositiveValidator
from rules.validation.validators.email_validator import EmailValidator
from rules.validation.validators.future_date_validator import FutureDateValidator


class ValidatorRegistry:

    def __init__(self):

        self._validators = {}

        self.register(
            "UNIQUE",
            UniqueValidator()
        )

        self.register(
            "NOT_NULL",
            NotNullValidator()
        )

        self.register(
            "POSITIVE",
            PositiveValidator()
        )

        self.register(
            "VALID_EMAIL",
            EmailValidator()
        )

        self.register(
            "NOT_FUTURE_DATE",
            FutureDateValidator()
        )

    # =====================================================

    def register(
        self,
        validation_name,
        validator
    ):

        self._validators[
            validation_name.upper()
        ] = validator

    # =====================================================

    def get(
        self,
        validation_name
    ):

        return self._validators.get(
            validation_name.upper()
        )

    # =====================================================

    def available(self):

        return sorted(
            self._validators.keys()
        )