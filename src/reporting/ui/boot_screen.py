from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text

from reporting.ui.design.theme import SentinelTheme


class BootScreen:

    def __init__(self):

        self.console = Console()

        self.theme = SentinelTheme()

    def show(self):

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
            f"Build {self.theme.version.VERSION}\n",
            style="grey70"
        )

        title.append(
            f"Codename: {self.theme.version.CODENAME}",
            style="bold yellow"
        )

        panel = Panel.fit(

            Align.center(title),

            border_style="cyan",

            padding=(1, 4)

        )

        self.console.print()

        self.console.print(panel)

        self.console.print()