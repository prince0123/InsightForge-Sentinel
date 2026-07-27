"""
============================================================
InsightForge Sentinel
Logo Widget
============================================================
"""

from rich.panel import Panel
from rich.align import Align
from rich.text import Text


class LogoWidget:

    def build(self):

        title = Text()

        title.append(
            "InsightForge Sentinel\n",
            style="bold cyan"
        )

        title.append(
            "Enterprise Data Trust Platform\n",
            style="white"
        )

        title.append(
            "Version 0.9 Alpha",
            style="dim"
        )

        return Panel.fit(

            Align.center(title),

            border_style="cyan",

            padding=(1, 4)

        )