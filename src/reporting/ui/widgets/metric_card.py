"""
============================================================
Metric Card
============================================================
"""

from rich.align import Align
from rich.panel import Panel
from rich.text import Text

from reporting.ui.widgets.base_widget import BaseWidget
from reporting.ui.design.typography import Typography


class MetricCard(BaseWidget):

    def render(
        self,
        title,
        value,
        icon="",
        border_style=None,
        width=32
    ):

        body = Text()

        body.append(
            f"{icon} {title.upper()}\n\n",
            style=Typography.TITLE
        )

        body.append(
            str(value),
            style=Typography.HERO
        )

        panel = Panel(

            Align.center(body),

            width=width,

            border_style=(
                border_style
                or
                self.theme.colors.BORDER
            ),

            padding=(1, 2)

        )

        return panel