"""
============================================================
InsightForge Sentinel
Main Application
============================================================

Author  : InsightForge
Version : 0.5.0
"""

from pathlib import Path

from connectors.file_connector import FileConnector
from preprocessing.preprocessor import Preprocessor
from profiling.profiler import DataProfiler
from analyzers.primary_key_analyzer import PrimaryKeyAnalyzer
from analyzers.business_type_analyzer import BusinessTypeAnalyzer
from reporting.console_reporter import ConsoleReporter


def main():

    # --------------------------------------------------------
    # Initialize Components
    # --------------------------------------------------------

    reporter = ConsoleReporter()

    connector = FileConnector()

    preprocessor = Preprocessor()

    profiler = DataProfiler()

    pk_analyzer = PrimaryKeyAnalyzer()

    bt_analyzer = BusinessTypeAnalyzer()

    # --------------------------------------------------------
    # Header
    # --------------------------------------------------------

    reporter.show_header()

    # --------------------------------------------------------
    # Load Dataset
    # --------------------------------------------------------

    project_root = Path(__file__).resolve().parent.parent

    file_path = (
        project_root
        / "data"
        / "sample"
        / "sample_sales.csv"
    )

    df = connector.load(file_path)

    # --------------------------------------------------------
    # NEW : Preprocessing
    # --------------------------------------------------------

    print("\nRunning Preprocessing Engine...")

    df = preprocessor.process(df)

    print("Preprocessing Completed Successfully")

    # --------------------------------------------------------
    # Dataset Profiling
    # --------------------------------------------------------

    profile = profiler.profile(df)

    reporter.show_profile(profile)

    # --------------------------------------------------------
    # Primary Key Analysis
    # --------------------------------------------------------

    pk_results = pk_analyzer.analyze(df)

    reporter.show_primary_keys(pk_results)

    # --------------------------------------------------------
    # Business Type Analysis
    # --------------------------------------------------------

    bt_results = bt_analyzer.analyze(df)

    reporter.show_business_types(bt_results)

    # --------------------------------------------------------
    # Footer
    # --------------------------------------------------------

    reporter.show_footer()


if __name__ == "__main__":
    main()