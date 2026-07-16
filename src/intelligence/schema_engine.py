"""
============================================================
InsightForge Sentinel
Schema Intelligence Engine
============================================================

Purpose:
    Builds intelligent ColumnProfile objects for every
    column in a dataset.

Author : InsightForge
Version : 1.0
"""

import profile

from models.column_profile import ColumnProfile


class SchemaEngine:
    def build_profiles(
        self,
        dataframe,
        profile,
        knowledge,
        business_type_result
    ):

        profiles = []

        profile_info = profile
        
        for result in business_type_result["results"]:

            column = result["column"]

            physical_type = str(
                dataframe[column].dtype
            )

            nullable = (
                profile_info["missing_values"][column] > 0
            )

            duplicates = knowledge.get_fact(
                column,
                "duplicate_values",
                0
            )

            unique = duplicates == 0

            uniqueness_ratio = (
                knowledge.get_fact(
                    column,
                    "uniqueness_ratio",
                    0
                )
            )

            validators = self._recommended_validators(
                result["business_type"]
            )

            profiles.append(

                ColumnProfile(

                    name=column,

                    logical_type=result["business_type"],

                    physical_type=physical_type,

                    confidence=result["confidence"],

                    nullable=nullable,

                    unique=unique,

                    uniqueness_ratio=uniqueness_ratio,

                    recommended_validators=validators

                )

            )

        return profiles

    # ==================================================

    def _recommended_validators(
        self,
        logical_type
    ):

        mapping = {

            "Identifier": [
                "UNIQUE",
                "NOT_NULL"
            ],

            "Currency": [
                "POSITIVE",
                "NOT_NULL"
            ],

            "Date": [
                "NOT_FUTURE_DATE"
            ],

            "Email Address": [
                "VALID_EMAIL",
                "NOT_NULL"
            ]

        }

        return mapping.get(
            logical_type,
            []
        )