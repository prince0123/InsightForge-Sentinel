"""
============================================================
InsightForge Sentinel
Base Validator
============================================================

Purpose:
    Base class for all validators.

Author : InsightForge
Version : 2.0
"""

from abc import ABC, abstractmethod


class BaseValidator(ABC):

    @abstractmethod
    def validate(
        self,
        dataframe,
        knowledge,
        task
    ):
        pass

    # ======================================================
    # Rule Text Formatter
    # ======================================================

    def format_rule_text(
        self,
        rule,
        column,
        business_type=None,
        industry=None
    ):
        """
        Formats rule templates using available placeholders.

        Supported placeholders:
            {column}
            {business_type}
            {industry}
        """

        context = {
            "column": column,
            "business_type": business_type or "",
            "industry": industry or ""
        }

        return {

            "rule_name": rule.name.format(**context),

            "recommendation": rule.recommendation.format(**context),

            "business_impact": rule.business_impact.format(**context)

        }