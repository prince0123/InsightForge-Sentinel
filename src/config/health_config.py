"""
============================================================
InsightForge Sentinel
Health Configuration
============================================================

Purpose:
    Central configuration for dataset health scoring.

Author : InsightForge
Version : 1.0
"""

# ==========================================================
# Health Metric Weights
# ==========================================================

HEALTH_WEIGHTS = {

    "completeness": 0.30,

    "uniqueness": 0.25,

    "validity": 0.30,

    "consistency": 0.15

}

# ==========================================================
# Severity Penalties
# ==========================================================

SEVERITY_PENALTIES = {

    "HIGH": 20,

    "MEDIUM": 10,

    "LOW": 5

}

# ==========================================================
# Risk Thresholds
# ==========================================================

RISK_LEVELS = {

    "LOW": 90,

    "MEDIUM": 75,

    "HIGH": 60,

    "CRITICAL": 0

}