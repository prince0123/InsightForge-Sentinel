"""
============================================================
InsightForge Sentinel
Data Type Inference Engine
============================================================

Purpose:
    Automatically infers and converts dataframe columns
    into appropriate data types.

Author : InsightForge
Version : 1.0
"""

import pandas as pd


class DataTypeInference:

    def process(self, df: pd.DataFrame) -> pd.DataFrame:

        df = df.copy()

        for column in df.columns:

            series = df[column]

            # Skip columns that are already numeric/datetime
            if pd.api.types.is_numeric_dtype(series):
                continue

            if pd.api.types.is_datetime64_any_dtype(series):
                continue

            # ------------------------------------------------
            # Try Integer
            # ------------------------------------------------

            try:

                converted = pd.to_numeric(series, errors="raise")

                if (converted % 1 == 0).all():

                    df[column] = converted.astype("Int64")

                    continue

                df[column] = converted.astype(float)

                continue

            except Exception:

                pass

            # ------------------------------------------------
            # Try Date
            # ------------------------------------------------

            try:

                converted = pd.to_datetime(
                    series,
                    errors="raise"
                )

                df[column] = converted

                continue

            except Exception:

                pass

            # ------------------------------------------------
            # Default
            # ------------------------------------------------

            df[column] = series.astype("string")

        return df