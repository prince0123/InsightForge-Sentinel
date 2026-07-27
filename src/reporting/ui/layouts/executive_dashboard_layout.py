"""
============================================================
Executive Dashboard Layout
============================================================
"""

from rich.columns import Columns

from reporting.ui.widgets.metric_card import MetricCard
from reporting.ui.widgets.status_badge import StatusBadge


class ExecutiveDashboardLayout:

    def __init__(self):

        self.metric = MetricCard()

        self.badge = StatusBadge()

    # =====================================================

    def render(
        self,
        assessment
    ):

        cards = [

            self.metric.render(
                "Data Trust Index",
                f"{assessment.data_trust_index:.2f}",
                "🛡"
            ),

            self.metric.render(
                "Dataset Grade",
                assessment.dataset_grade,
                "🏆"
            ),

            self.metric.render(
                "Risk Level",
                assessment.risk_level,
                "⚠"
            ),

            self.metric.render(
                "Production",
                "YES"
                if assessment.production_ready
                else "REVIEW",
                "🏭"
            ),

            self.metric.render(
                "Analytics",
                "YES"
                if assessment.analytics_ready
                else "NO",
                "📊"
            ),

            self.metric.render(
                "AI Ready",
                "YES"
                if assessment.ai_ready
                else "NO",
                "🤖"
            )

        ]

        return Columns(

            cards,

            equal=True,

            expand=True

        )