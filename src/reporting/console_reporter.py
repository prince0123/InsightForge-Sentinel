"""
============================================================
InsightForge Sentinel
Console Reporter
============================================================

Purpose:
    Displays Sentinel analysis results in a consistent,
    human-readable format.

Author : InsightForge
Version : 4.0
"""


import health


class ConsoleReporter:

    # ======================================================
    # Header
    # ======================================================

    def show_header(self):

        print("\n" + "=" * 70)
        print("InsightForge Sentinel")
        print("=" * 70)

    # ======================================================
    # Dataset Profile
    # ======================================================

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

    # ======================================================
    # Primary Key Analysis
    # ======================================================

    def show_primary_keys(self, analyzer_result):

        print("\n" + "=" * 70)
        print("PRIMARY KEY ANALYSIS")
        print("=" * 70)

        for result in analyzer_result["results"]:

            print(f"\nColumn              : {result['column']}")
            print(f"Confidence          : {result['confidence']}%")
            print(f"Risk                : {result['risk']}")
            print(f"Severity            : {result['severity']}")
            print(f"Status              : {result['status']}")

            print(f"\nNULL Values         : {result['null_values']}")
            print(f"Duplicate Values    : {result['duplicate_values']}")
            print(f"Unique Values       : {result['unique_values']}")
            print(f"Uniqueness Ratio    : {result['uniqueness_ratio']}%")

            print("\nEvidence")
            print("-" * 50)

            for evidence in result["evidence"]:

                icon = "✓" if evidence["passed"] else "✗"

                print(
                    f"{icon} {evidence['rule']} "
                    f"(Weight: {evidence['weight']})"
                )

            print("\nRecommendations")
            print("-" * 50)

            for recommendation in result["recommendations"]:
                print(f"• {recommendation}")

            print("\nBusiness Impact")
            print("-" * 50)

            for impact in result["business_impact"]:
                print(f"• {impact}")

            print("=" * 70)

    # ======================================================
    # Business Type Analysis
    # ======================================================

    def show_business_types(self, analyzer_result):

        print("\n" + "=" * 70)
        print("BUSINESS TYPE ANALYSIS")
        print("=" * 70)

        for result in analyzer_result["results"]:

            print(f"\nColumn              : {result['column']}")
            print(f"Business Type       : {result['business_type']}")
            print(f"Confidence          : {result['confidence']}%")

            print("\nReasons")
            print("-" * 50)

            for reason in result["reasons"]:
                print(f"✓ {reason}")

            print("\nRecommended Rules")
            print("-" * 50)

            for rule in result["recommended_rules"]:
                print(f"• {rule}")

            print("=" * 70)

        print("\nOverall Recommendations")

        for recommendation in analyzer_result["recommendations"]:
            print(f"✓ {recommendation}")

    # ======================================================
    # Schema Intelligence
    # ======================================================

    def show_schema_profiles(self, column_profiles):

        print("\n" + "=" * 70)
        print("SCHEMA INTELLIGENCE")
        print("=" * 70)

        for profile in column_profiles:

            print(f"\nColumn              : {profile.name}")
            print(f"Logical Type        : {profile.logical_type}")
            print(f"Physical Type       : {profile.physical_type}")
            print(f"Confidence          : {profile.confidence}%")

            print(f"\nNullable            : {profile.nullable}")
            print(f"Unique              : {profile.unique}")
            print(
                f"Uniqueness Ratio    : "
                f"{profile.uniqueness_ratio}%"
            )

            print("\nRecommended Validators")
            print("-" * 50)

            if profile.recommended_validators:

                for validator in profile.recommended_validators:

                    print(f"• {validator}")

            else:

                print("No recommendations.")

            print("=" * 70)
    # ======================================================
    # Validation Results


    def show_validation_results(self, validation_output):

        print("\n" + "=" * 70)
        print("VALIDATION RESULTS")
        print("=" * 70)

        print(f"Status             : {validation_output['status']}")
        print(f"Rules Executed     : {validation_output['rules_executed']}")
        print(f"Passed             : {validation_output['passed']}")
        print(f"Failed             : {validation_output['failed']}")
        print(
            f"Not Implemented    : "
            f"{validation_output.get('not_implemented', 0)}"
        )

        print("\nValidation Details")
        print("-" * 70)

        for result in validation_output["results"]:

            status = result.status

            if status == "PASS":
                icon = "✓"

            elif status == "FAIL":
                icon = "✗"

            else:
                icon = "⚠"

            print(f"\n{icon} Rule")

            print(f"Rule ID            : {result.rule_id}")
            print(f"Rule Name          : {result.rule_name}")
            print(f"Column             : {result.column}")
            print(f"Business Type      : {result.business_type}")
            print(f"Validation         : {result.validation}")
            print(f"Severity           : {result.severity}")
            print(f"Result             : {result.status}")
            print(f"Message            : {result.message}")

            if result.failed_count > 0:

                print(f"Failed Count       : {result.failed_count}")

            if result.failed_rows:

                print("\nFailed Rows")
                print("-" * 50)

                for row in result.failed_rows:
                    print(f"• {row}")

            if result.failed_values:

                print("\nSample Failed Values")
                print("-" * 50)

                for value in result.failed_values[:10]:
                    print(f"• {value}")

            print("\nBusiness Impact")
            print("-" * 50)
            print(f"• {result.business_impact}")

            print("\nRecommendation")
            print("-" * 50)
            print(f"• {result.recommendation}")

            print("-" * 70)

# ======================================================
# Dataset Health
# ======================================================

    def show_health_score(
    self,
    health
    ):

        print("\n" + "=" * 70)
        print("DATASET HEALTH")
        print("=" * 70)

        print(
            f"Overall Score      : "
            f"{health.overall_score}/100"
            )

        print(
        f"Risk Level         : "
        f"{health.risk_level}"
        )

        print()

        print(
            f"Completeness       : "
            f"{health.completeness}%"
        )

        print(
            f"Uniqueness         : "
            f"{health.uniqueness}%"
        )

        print(
            f"Validity           : "
            f"{health.validity}%"
        )

        print(
            f"Consistency        : "
            f"{health.consistency}%"
        )

        print("\nTop Issues")
        print("-" * 50)

        if health.issues:

            for issue in health.issues:

                print(f"• {issue}")

        else:

            print("No issues detected.")

        print("\nSummary")
        print("-" * 50)

        print(health.summary)

    # ======================================================
    # Footer
    # ======================================================

    def show_footer(self):

        print("\n" + "=" * 70)
        print("Sentinel Analysis Completed Successfully")
        print("=" * 70)