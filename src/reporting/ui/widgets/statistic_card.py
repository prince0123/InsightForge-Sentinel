"""
============================================================
Statistic Card
============================================================
"""

from rich.panel import Panel
from rich.table import Table

from reporting.ui.widgets.base_widget import BaseWidget


class StatisticCard(BaseWidget):

    def render(

        self,

        title,

        icon,

        statistics

    ):

        table = Table.grid(

            padding=(0, 1)

        )

        for label, value in statistics:

            table.add_row(

                f"[cyan]{label}[/]",

                f"[bold]{value}[/]"

            )

        return Panel(

            table,

            title=f"{icon} {title}",

            border_style=self.theme.colors.BORDER,

            padding=(1, 2)

        )