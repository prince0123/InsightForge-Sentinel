from pathlib import Path

from connectors.file_connector import FileConnector
from profiling.profiler import DataProfiler


def main():

    print("=" * 60)
    print("InsightForge Sentinel")
    print("=" * 60)

    base_dir = Path(__file__).resolve().parent.parent

    file_path = (
        base_dir
        / "data"
        / "sample"
        / "sample_sales.csv"
    )

    connector = FileConnector()

    df = connector.load(file_path)

    profiler = DataProfiler()

    profile = profiler.profile(df)

    print("\nDataset Profile")
    print("-" * 40)

    print(f"Rows              : {profile['rows']}")
    print(f"Columns           : {profile['columns']}")
    print(f"Duplicate Rows    : {profile['duplicate_rows']}")
    print(f"Memory Usage (MB) : {profile['memory_usage_mb']}")

    print("\nColumn Names")

    for column in profile["column_names"]:
        print(f"• {column}")

    print("\nMissing Values")

    for column, count in profile["missing_values"].items():
        print(f"{column}: {count}")

    print("\nData Types")

    for column, dtype in profile["data_types"].items():
        print(f"{column}: {dtype}")


if __name__ == "__main__":
    main()