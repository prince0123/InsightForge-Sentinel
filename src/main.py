"""
============================================================
InsightForge Sentinel
Main Application
============================================================

Author : InsightForge
Version : 0.2
"""

from pathlib import Path

from connectors.file_connector import FileConnector
from profiling.profiler import DataProfiler
from analyzers.primary_key_analyzer import PrimaryKeyAnalyzer


def print_dataset_profile(profile: dict):
    """Print dataset profile."""

    print("\n" + "=" * 60)
    print("DATASET PROFILE")
    print("=" * 60)

    print(f"Rows              : {profile['rows']}")
    print(f"Columns           : {profile['columns']}")
    print(f"Duplicate Rows    : {profile['duplicate_rows']}")
    print(f"Memory Usage (MB) : {profile['memory_usage_mb']}")

    print("\nColumn Names")
    print("-" * 40)

    for column in profile["column_names"]:
        print(f"• {column}")

    print("\nMissing Values")
    print("-" * 40)

    for column, count in profile["missing_values"].items():
        print(f"{column}: {count}")

    print("\nData Types")
    print("-" * 40)

    for column, dtype in profile["data_types"].items():
        print(f"{column}: {dtype}")


def print_primary_key_analysis(results: list):
    """Print primary key analysis."""

    print("\n" + "=" * 60)
    print("PRIMARY KEY ANALYSIS")
    print("=" * 60)

    for result in results:

        print(f"\nColumn        : {result['column']}")
        print(f"Score         : {result['score']}")
        print(f"Confidence    : {result['confidence']}")
        print(f"NULL Values   : {result['nulls']}")
        print(f"Duplicates    : {result['duplicates']}")
        print(f"Unique Values : {result['unique_values']}")

        print("\nReasons")

        for reason in result["reasons"]:
            print(f"  ✓ {reason}")

        print("-" * 60)


def main():

    print("=" * 60)
    print("InsightForge Sentinel")
    print("=" * 60)

    # -------------------------------------------------------
    # Load Dataset
    # -------------------------------------------------------

    base_dir = Path(__file__).resolve().parent.parent

    file_path = (
        base_dir
        / "data"
        / "sample"
        / "sample_sales.csv"
    )

    connector = FileConnector()

    df = connector.load(file_path)

    # -------------------------------------------------------
    # Profile Dataset
    # -------------------------------------------------------

    profiler = DataProfiler()

    profile = profiler.profile(df)

    print_dataset_profile(profile)

    # -------------------------------------------------------
    # Primary Key Analysis
    # -------------------------------------------------------

    analyzer = PrimaryKeyAnalyzer()

    results = analyzer.analyze(df)

    print_primary_key_analysis(results)

    print("\n" + "=" * 60)
    print("Sentinel Analysis Completed Successfully")
    print("=" * 60)


if __name__ == "__main__":
    main()