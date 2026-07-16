"""
============================================================
InsightForge Sentinel
Sentinel Dataset
============================================================

Purpose:
    Central domain object representing an entire dataset
    as it flows through the Sentinel pipeline.

Author : InsightForge
Version : 1.0
"""


class SentinelDataset:

    def __init__(

        self,

        dataframe=None,

        profile=None,

        knowledge=None,

        columns=None,

        execution_plan=None,

        validation_results=None,

        health=None,

        trust=None,

        recommendations=None,

        metadata=None

    ):

        self.dataframe = dataframe

        self.profile = profile

        self.knowledge = knowledge

        self.columns = columns or []

        self.execution_plan = execution_plan or []

        self.validation_results = validation_results

        self.health = health

        self.trust = trust

        self.recommendations = recommendations or []

        self.metadata = metadata or {}

    # =====================================================

    def add_column(self, profile):

        self.columns.append(profile)

    # =====================================================

    def get_column(self, name):

        for column in self.columns:

            if column.name == name:

                return column

        return None

    # =====================================================

    def to_dict(self):

        return {

            "profile": self.profile,

            "columns": [

                column.to_dict()

                for column in self.columns

            ],

            "health": self.health,

            "trust": self.trust,

            "recommendations": self.recommendations,

            "metadata": self.metadata

        }

    # =====================================================

    def summary(self):

        return {

            "rows": self.profile["rows"]

            if self.profile else 0,

            "columns": self.profile["columns"]

            if self.profile else 0,

            "health": self.health,

            "trust": self.trust

        }

    # =====================================================

    def __repr__(self):

        return (

            f"SentinelDataset("

            f"rows={self.profile['rows'] if self.profile else 0}, "

            f"columns={self.profile['columns'] if self.profile else 0})"

        )

    # =====================================================

    def __str__(self):

        return (

            f"Sentinel Dataset "

            f"({self.profile['rows'] if self.profile else 0} rows)"

        )