"""
============================================================
InsightForge Sentinel
Executive Dashboard Section
============================================================

Purpose:
    Displays the executive summary of dataset trust.

Author : InsightForge
Version : 1.0
"""

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

from health.trust.trust_assessment import TrustAssessment


class ExecutiveDashboardSection:

    def __init__(self):

        self.console = Console()

    # =====================================================

    def render(
        self,
        assessment: TrustAssessment
    ):

        title = Text()

        title.append(
            "INSIGHTFORGE SENTINEL\n",
            style="bold cyan"
        )

        title.append(
            "Know your data. Trust your decisions.",
            style="white"
        )

        self.console.print(
            Panel.fit(
                title,
                border_style="cyan"
            )
        )

        self.console.print()

        # -------------------------------------------------
        # Executive Summary
        # -------------------------------------------------

        table = Table(
            title="Executive Dashboard",
            show_header=False,
            expand=False
        )

        table.add_column(width=30)

        table.add_column(width=25)

        table.add_row(
            "🛡 Data Trust Index",
            f"{assessment.data_trust_index:.2f}"
        )

        table.add_row(
            "🏆 Dataset Grade",
            assessment.dataset_grade
        )

        table.add_row(
            "⚠ Risk Level",
            assessment.risk_level
        )

        table.add_row(
            "🏭 Production Ready",
            "YES" if assessment.production_ready else "REVIEW REQUIRED"
        )

        table.add_row(
            "📊 Analytics Ready",
            "YES" if assessment.analytics_ready else "NO"
        )

        table.add_row(
            "🤖 AI Ready",
            "YES" if assessment.ai_ready else "NO"
        )

        self.console.print(table)

        self.console.print()

        # -------------------------------------------------
        # Dataset Summary
        # -------------------------------------------------

        dataset = Table(
            title="Dataset Summary"
        )

        dataset.add_column("Metric")

        dataset.add_column("Value")

        dataset.add_row(
            "Rows",
            str(assessment.rows)
        )

        dataset.add_row(
            "Columns",
            str(assessment.columns)
        )

        dataset.add_row(
            "Rules Executed",
            str(assessment.rules_executed)
        )

        dataset.add_row(
            "Passed",
            str(assessment.passed_rules)
        )

        dataset.add_row(
            "Failed",
            str(assessment.failed_rules)
        )

        self.console.print(dataset)

        self.console.print()

        # -------------------------------------------------
        # Top Issues
        # -------------------------------------------------

        if assessment.top_issues:

            issues = Table(
                title="Top Issues"
            )

            issues.add_column("#")

            issues.add_column("Issue")

            for index, issue in enumerate(
                assessment.top_issues[:5],
                start=1
            ):

                issues.add_row(
                    str(index),
                    issue
                )

            self.console.print(issues)