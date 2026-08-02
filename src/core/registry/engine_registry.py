"""
============================================================
InsightForge Sentinel
Engine Registry
============================================================

Purpose:
    Central registry for all application engines.

Author : InsightForge
Version : 1.0.0
"""

from connectors.file_connector import FileConnector

from preprocessing.preprocessor import Preprocessor
from preprocessing.datatype_inference import DataTypeInference

from profiling.profiler import DataProfiler

from inference.inference_engine import InferenceEngine

from intelligence.schema_engine import SchemaEngine

from rules.rule_engine import RuleEngine
from rules.validation.validation_engine import ValidationEngine

from health.health_engine import HealthEngine

from reporting.console_reporter import ConsoleReporter


class EngineRegistry:
    """
    Creates and owns all application engines.

    Acts as the Composition Root for business services.
    """

    def __init__(self):

        # -------------------------------
        # Data
        # -------------------------------

        self.connector = FileConnector()

        self.preprocessor = Preprocessor()

        self.datatype_inference = DataTypeInference()

        self.profiler = DataProfiler()

        # -------------------------------
        # Intelligence
        # -------------------------------

        self.inference = InferenceEngine()

        self.schema = SchemaEngine()

        # -------------------------------
        # Validation
        # -------------------------------

        self.rule_engine = RuleEngine()

        self.validation_engine = ValidationEngine()

        # -------------------------------
        # Trust
        # -------------------------------

        self.health_engine = HealthEngine()

        # -------------------------------
        # Reporting
        # -------------------------------

        self.reporter = ConsoleReporter()