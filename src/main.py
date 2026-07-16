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
Rule Engine
      ↓
Validation Engine
      ↓
Reporting

Author : InsightForge
Version : 0.8.0
"""

from pathlib import Path

from connectors.file_connector import FileConnector
from intelligence import schema_engine
from intelligence.schema_engine import SchemaEngine
from preprocessing.preprocessor import Preprocessor
from preprocessing.datatype_inference import DataTypeInference
from profiling.profiler import DataProfiler

from inference.inference_engine import InferenceEngine

from rules.rule_engine import RuleEngine
from rules.validation.validation_engine import ValidationEngine

from reporting.console_reporter import ConsoleReporter


def main():

    # =====================================================
    # Initialize Components
    # =====================================================

    connector = FileConnector()

    preprocessor = Preprocessor()

    datatype_engine = DataTypeInference()

    profiler = DataProfiler()

    inference_engine = InferenceEngine()

    rule_engine = RuleEngine()

    validation_engine = ValidationEngine()

    reporter = ConsoleReporter()


    # =====================================================
    # Header
    # =====================================================

    reporter.show_header()

    # =====================================================
    # Load Dataset
    # =====================================================

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

    profile = profiler.profile(df)

    reporter.show_profile(profile)

    # =====================================================
    # Inference Engine
    # =====================================================

    print("\nRunning Inference Engine...")

    inference_output = inference_engine.run(df)

    print("✓ Inference Complete")

    knowledge = inference_output["knowledge"]

    capabilities = inference_output["capabilities"]
    
    print("\nRunning Schema Intelligence Engine...")

    schema_engine = SchemaEngine()

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
    # Reporting
    # =====================================================

    reporter.show_primary_keys(
        capabilities["primary_key"]
    )

    reporter.show_business_types(
        capabilities["business_type"]
    )

    reporter.show_schema_profiles(column_profiles)

    reporter.show_validation_results(
        validation_output
    )

    # =====================================================
    # Footer
    # =====================================================

    reporter.show_footer()


if __name__ == "__main__":

    main()