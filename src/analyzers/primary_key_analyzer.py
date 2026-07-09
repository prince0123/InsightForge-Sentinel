"""
============================================================
InsightForge Sentinel
Primary Key Analyzer
============================================================

Detects possible primary key columns.

Author : InsightForge
Version : 0.1
"""

import pandas as pd


class PrimaryKeyAnalyzer:

    def analyze(self, df: pd.DataFrame) -> list:

        candidates = []

        total_rows = len(df)

        for column in df.columns:

            null_count = df[column].isnull().sum()

            duplicate_count = df[column].duplicated().sum()

            unique_count = df[column].nunique()

            uniqueness = unique_count / total_rows

            score = 0
            reasons = []

            # No NULL values
            if null_count == 0:
                score += 30
                reasons.append("No NULL values")

            # No duplicates
            if duplicate_count == 0:
                score += 40
                reasons.append("No duplicate values")

            # High uniqueness
            if uniqueness >= 0.95:
                score += 20
                reasons.append("High uniqueness")

            # Column name contains ID
            if "id" in column.lower():
                score += 10
                reasons.append("Column name contains 'ID'")

            candidates.append({

                "column": column,

                "score": score,

                "confidence": f"{score}%",

                "nulls": int(null_count),

                "duplicates": int(duplicate_count),

                "unique_values": int(unique_count),

                "reasons": reasons

            })

        candidates.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return candidates