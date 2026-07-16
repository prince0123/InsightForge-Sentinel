"""
============================================================
InsightForge Sentinel
Inference Engine
============================================================

Purpose:
    Executes all inference capabilities and builds
    the shared Knowledge Model.

Author : InsightForge
Version: 2.0
"""

import pandas as pd

from analyzers.primary_key_analyzer import PrimaryKeyAnalyzer
from analyzers.business_type_analyzer import BusinessTypeAnalyzer
from models.knowledge_model import KnowledgeModel


class InferenceEngine:

    def __init__(self):

        self.primary_key_analyzer = PrimaryKeyAnalyzer()

        self.business_type_analyzer = BusinessTypeAnalyzer()

    # ======================================================
    # Public API
    # ======================================================

    def run(self, df: pd.DataFrame):

        knowledge = KnowledgeModel()

        # --------------------------------------------------
        # Execute Analyzers
        # --------------------------------------------------

        primary_key_results = self.primary_key_analyzer.analyze(df)

        business_type_results = self.business_type_analyzer.analyze(df)

        # --------------------------------------------------
        # Populate Knowledge Model
        # --------------------------------------------------

        self._populate_business_type_knowledge(
            knowledge,
            business_type_results
        )

        self._populate_primary_key_knowledge(
            knowledge,
            primary_key_results
        )

        # --------------------------------------------------
        # Return Engine Output
        # --------------------------------------------------

        return {

            "engine": "InferenceEngine",

            "status": "SUCCESS",

            "knowledge": knowledge,

            "capabilities": {

                "primary_key": primary_key_results,

                "business_type": business_type_results

            },

            "summary": {

                "columns": len(df.columns),

                "knowledge_entries": len(knowledge),

                "capabilities_executed": 2

            }   

        }

    # ======================================================
    # Internal Methods
    # ======================================================

    def _populate_business_type_knowledge(
        self,
        knowledge,
        results
    ):

        for result in results["results"]:

            column = result["column"]

            knowledge.set_fact(
                column,
                "business_type",
                result["business_type"]
            )

            knowledge.set_fact(
                column,
                "business_type_confidence",
                result["confidence"]
            )

    def _populate_primary_key_knowledge(
        self,
        knowledge,
        results
    ):

        for result in results["results"]:

            column = result["column"]

            knowledge.set_fact(
                column,
                "primary_key_confidence",
                result["confidence"]
            )

            knowledge.set_fact(
                column,
                "risk",
                result["risk"]
            )

            knowledge.set_fact(
                column,
                "severity",
                result["severity"]
            )

            knowledge.set_fact(
                column,
                "null_values",
                result["null_values"]
            )

            knowledge.set_fact(
                column,
                "duplicate_values",
                result["duplicate_values"]
            )

            knowledge.set_fact(
                column,
                "uniqueness_ratio",
                result["uniqueness_ratio"]
            )