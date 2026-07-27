"""
Status Badge
"""

from rich.panel import Panel
from rich.text import Text

from reporting.ui.widgets.base_widget import BaseWidget
from reporting.ui.design.typography import Typography


class StatusBadge(BaseWidget):

    def render(
        self,
        text,
        colour
    ):

        return Panel.fit(

            Text(
                text,
                style=Typography.VALUE,
                justify="center"
            ),

            border_style=colour

        )