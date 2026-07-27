"""
============================================================
InsightForge Sentinel
Main Application
============================================================

Purpose:
    Entry point for the Sentinel pipeline.

Pipeline

Load Dataset
      ↓
Preprocess
      ↓
Profile
      ↓
Inference Engine
      ↓
Schema Intelligence
      ↓
Rule Engine
      ↓
Validation Engine
      ↓
Health Engine
      ↓
Trust Assessment
      ↓
Executive Dashboard
      ↓
Reporting

Author : InsightForge
Version : 1.0.0
"""

from pathlib import Path

from connectors.file_connector import FileConnector

from preprocessing.preprocessor import Preprocessor
from preprocessing.datatype_inference import DataTypeInference

from profiling.profiler import DataProfiler

from inference.inference_engine import InferenceEngine

from intelligence.schema_engine import SchemaEngine

from rules.rule_engine import RuleEngine
from rules.validation.validation_engine import ValidationEngine

from health.health_engine import HealthEngine
from health.trust.trust_assessment_builder import (
    TrustAssessmentBuilder
)

from reporting.console_reporter import ConsoleReporter
from reporting.ui.ui_engine import UIEngine


def main():

    # =====================================================
    # Initialize Components
    # =====================================================

    connector = FileConnector()

    preprocessor = Preprocessor()

    datatype_engine = DataTypeInference()

    profiler = DataProfiler()

    inference_engine = InferenceEngine()

    schema_engine = SchemaEngine()

    rule_engine = RuleEngine()

    validation_engine = ValidationEngine()

    health_engine = HealthEngine()

    assessment_builder = TrustAssessmentBuilder()

    reporter = ConsoleReporter()

    ui = UIEngine()

    # =====================================================
    # Header
    # =====================================================

    reporter.show_header()

    ui.start()

    # =====================================================
    # Load Dataset
    # =====================================================

    ui.stage("Loading Dataset")

    project_root = Path(__file__).resolve().parent.parent

    dataset_path = (
        project_root
        / "data"
        / "sample"
        / "sample_sales.csv"
    )

    df = connector.load(dataset_path)

    # =====================================================
    # Preprocessing
    # =====================================================

    print("\nRunning Preprocessing Engine...")

    df = preprocessor.process(df)

    print("\nRunning Data Type Inference...")

    df = datatype_engine.process(df)

    print("✓ Data Type Inference Complete")

    print("✓ Preprocessing Complete")

    # =====================================================
    # Profiling
    # =====================================================

    ui.stage("Profiling Dataset")

    profile = profiler.profile(df)

    # =====================================================
    # Inference Engine
    # =====================================================

    ui.stage("Inference Engine")

    print("\nRunning Inference Engine...")

    inference_output = inference_engine.run(df)

    print("✓ Inference Complete")

    knowledge = inference_output["knowledge"]

    capabilities = inference_output["capabilities"]

    # =====================================================
    # Schema Intelligence
    # =====================================================

    print("\nRunning Schema Intelligence Engine...")

    column_profiles = schema_engine.build_profiles(
        dataframe=df,
        profile=profile,
        knowledge=knowledge,
        business_type_result=capabilities["business_type"]
    )

    print("✓ Schema Intelligence Complete")

    # =====================================================
    # Rule Engine
    # =====================================================

    print("\nRunning Rule Engine...")

    rule_output = rule_engine.run(
        knowledge=knowledge,
        industry="retail"
    )

    print(
        f"✓ Created {rule_output['tasks_created']} execution tasks"
    )

    execution_plan = rule_output["execution_plan"]

    # =====================================================
    # Validation Engine
    # =====================================================

    ui.stage("Validation Engine")

    print("\nRunning Validation Engine...")

    validation_output = validation_engine.run(
        dataframe=df,
        knowledge=knowledge,
        execution_plan=execution_plan
    )

    print(
        f"✓ Executed {validation_output['rules_executed']} validation tasks"
    )

    # =====================================================
    # Health Engine
    # =====================================================

    ui.stage("Health Analysis")

    print("\nRunning Dataset Health Engine...")

    health_score = health_engine.run(
        profile=profile,
        validation_output=validation_output
    )

    print("✓ Dataset Health Complete")

    # =====================================================
    # Trust Assessment
    # =====================================================

    trust_assessment = assessment_builder.build(
        profile=profile,
        validation_output=validation_output,
        health_score=health_score
    )

    # =====================================================
    # Executive Dashboard
    # =====================================================

    ui.stage("Executive Dashboard")

    reporter.show_executive_dashboard(
        trust_assessment
    )

    # =====================================================
    # Reporting
    # =====================================================

    reporter.show_profile(
        profile
    )

    reporter.show_primary_keys(
        capabilities["primary_key"]
    )

    reporter.show_business_types(
        capabilities["business_type"]
    )

    reporter.show_schema_profiles(
        column_profiles
    )

    reporter.show_validation_results(
        validation_output
    )

    reporter.show_health_score(
        health_score
    )

    # =====================================================
    # Footer
    # =====================================================

    reporter.show_footer()

    ui.finish()


if __name__ == "__main__":

    main()