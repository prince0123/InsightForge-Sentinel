"""
============================================================
InsightForge Sentinel
Primary Key Analyzer
============================================================

Purpose:
    Identify potential primary key columns using explainable,
    evidence-based scoring.

Author : InsightForge
Version: 2.0
"""

import pandas as pd


class PrimaryKeyAnalyzer:

    def analyze(self, df: pd.DataFrame):

        results = []

        for column in df.columns:

            result = self._analyze_column(df, column)

            results.append(result)

        return {
            "analyzer": "PrimaryKeyAnalyzer",
            "status": "SUCCESS",
            "results": results
        }

    # ==========================================================
    # Internal Methods
    # ==========================================================

    def _analyze_column(self, df, column):

        series = df[column]

        null_count = int(series.isnull().sum())

        duplicate_count = int(series.duplicated().sum())

        unique_count = int(series.nunique(dropna=True))

        total_rows = len(series)

        uniqueness_ratio = 0

        if total_rows > 0:
            uniqueness_ratio = unique_count / total_rows

        evidence = []

        confidence = 0

        # ------------------------------------------------------
        # Rule 1
        # No NULL Values
        # ------------------------------------------------------

        passed = null_count == 0

        evidence.append({

            "rule": "No NULL values",

            "weight": 25,

            "passed": passed

        })

        if passed:
            confidence += 25

        # ------------------------------------------------------
        # Rule 2
        # No Duplicate Values
        # ------------------------------------------------------

        passed = duplicate_count == 0

        evidence.append({

            "rule": "No duplicate values",

            "weight": 35,

            "passed": passed

        })

        if passed:
            confidence += 35

        # ------------------------------------------------------
        # Rule 3
        # Identifier Name
        # ------------------------------------------------------

        identifier_keywords = [

            "id",
            "code",
            "number",
            "no"

        ]

        passed = any(

            keyword in column.lower()

            for keyword in identifier_keywords

        )

        evidence.append({

            "rule": "Identifier style column name",

            "weight": 20,

            "passed": passed

        })

        if passed:
            confidence += 20

        # ------------------------------------------------------
        # Rule 4
        # High Uniqueness
        # ------------------------------------------------------

        passed = uniqueness_ratio >= 0.95

        evidence.append({

            "rule": "High uniqueness (>95%)",

            "weight": 20,

            "passed": passed

        })

        if passed:
            confidence += 20

        # ------------------------------------------------------
        # Risk
        # ------------------------------------------------------

        if confidence >= 90:

            risk = "LOW"

        elif confidence >= 70:

            risk = "MEDIUM"

        else:

            risk = "HIGH"

        # ------------------------------------------------------
        # Severity
        # ------------------------------------------------------

        if confidence >= 90:

            severity = "LOW"

        elif confidence >= 70:

            severity = "MEDIUM"

        else:

            severity = "HIGH"

        # ------------------------------------------------------
        # Recommendations
        # ------------------------------------------------------

        recommendations = []

        if null_count > 0:

            recommendations.append(
                "Populate missing values before using this column as a primary key."
            )

        if duplicate_count > 0:

            recommendations.append(
                "Remove duplicate values to ensure uniqueness."
            )

        if not any(
            keyword in column.lower()
            for keyword in identifier_keywords
        ):

            recommendations.append(
                "Consider renaming the column if it represents a business identifier."
            )

        if uniqueness_ratio < 0.95:

            recommendations.append(
                "Increase uniqueness before selecting this column as a primary key."
            )

        if len(recommendations) == 0:

            recommendations.append(
                "Column is a strong primary key candidate."
            )

        # ------------------------------------------------------
        # Business Impact
        # ------------------------------------------------------

        business_impact = []

        if duplicate_count > 0:

            business_impact.append(
                "Duplicate identifiers can create incorrect joins."
            )

            business_impact.append(
                "Reports may double-count business transactions."
            )

        if null_count > 0:

            business_impact.append(
                "Missing identifiers reduce record traceability."
            )

        if len(business_impact) == 0:

            business_impact.append(
                "Low business risk detected."
            )

        # ------------------------------------------------------

        return {

            "column": column,

            "confidence": confidence,

            "risk": risk,

            "severity": severity,

            "status": "SUCCESS",

            "null_values": null_count,

            "duplicate_values": duplicate_count,

            "unique_values": unique_count,

            "uniqueness_ratio": round(
                uniqueness_ratio * 100,
                2
            ),

            "evidence": evidence,

            "recommendations": recommendations,

            "business_impact": business_impact

        }