"""
============================================================
InsightForge Sentinel
Console Reporter
============================================================

Purpose:
    Display analysis results in a clean and consistent format.

Author : InsightForge
Version: 0.4.0
"""


class ConsoleReporter:

    def show_header(self):

        print("\n" + "=" * 70)
        print("InsightForge Sentinel")
        print("=" * 70)

    def show_profile(self, profile):

        print("\n" + "=" * 70)
        print("DATASET PROFILE")
        print("=" * 70)

        print(f"Rows              : {profile['rows']}")
        print(f"Columns           : {profile['columns']}")
        print(f"Duplicate Rows    : {profile['duplicate_rows']}")
        print(f"Memory Usage (MB) : {profile['memory_usage_mb']}")

        print("\nColumn Names")
        print("-" * 50)

        for column in profile["column_names"]:
            print(f"• {column}")

        print("\nMissing Values")
        print("-" * 50)

        for column, count in profile["missing_values"].items():
            print(f"{column:<25} : {count}")

        print("\nData Types")
        print("-" * 50)

        for column, dtype in profile["data_types"].items():
            print(f"{column:<25} : {dtype}")

    def show_primary_keys(self, results):

        print("\n" + "=" * 70)
        print("PRIMARY KEY ANALYSIS")
        print("=" * 70)

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

            print("-" * 70)

    def show_business_types(self, analyzer_result):

        print("\n" + "=" * 70)
        print("BUSINESS TYPE ANALYSIS")
        print("=" * 70)

        print(f"Status  : {analyzer_result['status']}")
        print(f"Summary : {analyzer_result['summary']}")

        print("\n")

        for item in analyzer_result["results"]:

            print(f"Column            : {item['column']}")
            print(f"Business Type     : {item['business_type']}")
            print(f"Confidence        : {item['confidence']}%")

            print("\nReasons")

            for reason in item["reasons"]:
                print(f"  ✓ {reason}")

            print("\nRecommended Rules")

            for rule in item["recommended_rules"]:
                print(f"  • {rule}")

            print("-" * 70)

        print("\nOverall Recommendations")

        for recommendation in analyzer_result["recommendations"]:
            print(f"✓ {recommendation}")

    def show_footer(self):

        print("\n" + "=" * 70)
        print("Sentinel Analysis Completed Successfully")
        print("=" * 70)