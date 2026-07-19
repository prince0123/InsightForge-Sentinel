"""
============================================================
InsightForge Sentinel
Configuration Service
============================================================

Purpose:
    Central access point for Sentinel configuration.

Author : InsightForge
Version : 1.0
"""

from config.health_config import (
    HEALTH_WEIGHTS,
    SEVERITY_PENALTIES,
    RISK_LEVELS
)

from config.validation_config import (
    MAX_FAILED_ROWS,
    MAX_FAILED_VALUES,
    SHOW_FAILED_ROWS,
    SHOW_FAILED_VALUES
)

from config.business_config import (
    SHOW_HEALTH_BAR,
    SHOW_EXECUTIVE_SUMMARY,
    SHOW_BUSINESS_IMPACT,
    SHOW_RECOMMENDATIONS,
    SHOW_CONFIDENCE
)


class ConfigurationService:

    def __init__(self):
        pass

    # =====================================================
    # Health
    # =====================================================

    @property
    def health_weights(self):
        return HEALTH_WEIGHTS

    @property
    def severity_penalties(self):
        return SEVERITY_PENALTIES

    @property
    def risk_levels(self):
        return RISK_LEVELS

    # =====================================================
    # Validation
    # =====================================================

    @property
    def validation(self):

        return {

            "max_failed_rows": MAX_FAILED_ROWS,

            "max_failed_values": MAX_FAILED_VALUES,

            "show_failed_rows": SHOW_FAILED_ROWS,

            "show_failed_values": SHOW_FAILED_VALUES

        }

    # =====================================================
    # Business Reporting
    # =====================================================

    @property
    def reporting(self):

        return {

            "show_health_bar": SHOW_HEALTH_BAR,

            "show_executive_summary": SHOW_EXECUTIVE_SUMMARY,

            "show_business_impact": SHOW_BUSINESS_IMPACT,

            "show_recommendations": SHOW_RECOMMENDATIONS,

            "show_confidence": SHOW_CONFIDENCE

        }