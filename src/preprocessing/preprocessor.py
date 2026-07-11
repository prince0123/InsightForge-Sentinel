"""
============================================================
InsightForge Sentinel
Preprocessing Engine
============================================================

Purpose:
    Clean incoming datasets before profiling and analysis.

Author : InsightForge
Version: 0.5.0
"""

import pandas as pd
import numpy as np


class Preprocessor:

    def process(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Execute the complete preprocessing pipeline.
        """

        df = df.copy()

        df = self._trim_whitespace(df)

        df = self._normalize_missing_values(df)

        df = self._standardize_column_names(df)

        df = self._remove_empty_rows(df)

        df = self._reset_index(df)

        return df

    # -----------------------------------------------------
    # Private Methods
    # -----------------------------------------------------

    def _trim_whitespace(self, df: pd.DataFrame) -> pd.DataFrame:

        # Clean column names
        df.columns = [str(col).strip() for col in df.columns]

        # Clean string values
        for column in df.columns:

            if df[column].dtype == object:

                df[column] = df[column].astype(str).str.strip()

        return df

    def _normalize_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:

        missing_values = [

            "",

            " ",

            "NA",

            "N/A",

            "NULL",

            "Null",

            "null",

            "None",

            "none"

        ]

        df.replace(missing_values, np.nan, inplace=True)

        return df

    def _standardize_column_names(self, df: pd.DataFrame) -> pd.DataFrame:

        df.columns = [

            column.strip().replace(" ", "_")

            for column in df.columns

        ]

        return df

    def _remove_empty_rows(self, df: pd.DataFrame) -> pd.DataFrame:

        df = df.dropna(how="all")

        return df

    def _reset_index(self, df: pd.DataFrame) -> pd.DataFrame:

        return df.reset_index(drop=True)