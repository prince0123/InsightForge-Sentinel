"""
============================================================
InsightForge Sentinel
Business Type Analyzer
============================================================

Purpose:
    Detect the business meaning of dataset columns.

Author : InsightForge
Version: 0.4.0
"""

import pandas as pd


class BusinessTypeAnalyzer:
    """
    Detects business meaning from column names.

    Future versions will also analyze:
    - Sample values
    - Data patterns
    - Regular expressions
    """

    def __init__(self):

        self.rules = {

            "Identifier": {
                "keywords": [
                    "id",
                    "code",
                    "number",
                    "no"
                ],
                "recommended_rules": [
                    "Must be unique",
                    "Cannot be NULL"
                ]
            },

            "Email Address": {
                "keywords": [
                    "email",
                    "mail"
                ],
                "recommended_rules": [
                    "Valid Email Format",
                    "Cannot be NULL"
                ]
            },

            "Date": {
                "keywords": [
                    "date",
                    "dob",
                    "created",
                    "updated"
                ],
                "recommended_rules": [
                    "Valid Date",
                    "Cannot be Future Date"
                ]
            },

            "Currency": {
                "keywords": [
                    "amount",
                    "price",
                    "cost",
                    "salary",
                    "revenue",
                    "income"
                ],
                "recommended_rules": [
                    "Cannot be Negative",
                    "Detect Outliers"
                ]
            },

            "Phone Number": {
                "keywords": [
                    "phone",
                    "mobile",
                    "contact"
                ],
                "recommended_rules": [
                    "Valid Phone Format",
                    "Length Validation"
                ]
            },

            "Quantity": {
                "keywords": [
                    "qty",
                    "quantity",
                    "count"
                ],
                "recommended_rules": [
                    "Cannot be Negative"
                ]
            },

            "Percentage": {
                "keywords": [
                    "percentage",
                    "percent",
                    "discount"
                ],
                "recommended_rules": [
                    "Must be between 0 and 100"
                ]
            },

            "Product SKU": {
                "keywords": [
                    "sku",
                    "product"
                ],
                "recommended_rules": [
                    "Must Exist in Product Master"
                ]
            }

        }

    def analyze(self, df: pd.DataFrame):

        results = []

        overall_recommendations = []

        for column in df.columns:

            column_name = column.lower()

            detected_type = "Unknown"

            confidence = 50

            reasons = []

            recommended_rules = []

            for business_type, config in self.rules.items():

                keywords = config["keywords"]

                if any(keyword in column_name for keyword in keywords):

                    detected_type = business_type

                    confidence = 95

                    reasons.append(
                        f"Column name matched keyword(s): {', '.join(keywords)}"
                    )

                    recommended_rules = config["recommended_rules"]

                    break

            if detected_type == "Unknown":

                reasons.append(
                    "No known business pattern detected."
                )

                recommended_rules = [
                    "Manual Review Recommended"
                ]

            results.append({

                "column": column,

                "business_type": detected_type,

                "confidence": confidence,

                "reasons": reasons,

                "recommended_rules": recommended_rules

            })

        overall_recommendations.append(
            "Review Unknown columns before validation."
        )

        return {

            "analyzer": "BusinessTypeAnalyzer",

            "status": "SUCCESS",

            "summary": f"{len(results)} columns analyzed.",

            "results": results,

            "recommendations": overall_recommendations

        }