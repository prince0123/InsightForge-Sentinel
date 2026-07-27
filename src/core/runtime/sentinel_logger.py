"""
============================================================
Sentinel Logger
============================================================
"""

from rich.console import Console

from rich.panel import Panel

from rich.text import Text

from datetime import datetime


class SentinelLogger:

    def __init__(self):

        self.console = Console()

    # =============================================

    def stage(

        self,

        name

    ):

        self.console.print(

            f"\n[bold cyan]▶ {name}[/]"

        )

    # =============================================

    def success(

        self,

        message

    ):

        self.console.print(

            f"[bold green]✓ {message}[/]"

        )

    # =============================================

    def warning(

        self,

        message

    ):

        self.console.print(

            f"[yellow]⚠ {message}[/]"

        )

    # =============================================

    def error(

        self,

        message

    ):

        self.console.print(

            f"[bold red]✖ {message}[/]"

        )

    # =============================================

    def info(

        self,

        message

    ):

        self.console.print(

            f"[white]{message}[/]"

        )

    # =============================================

    def header(

        self,

        title

    ):

        self.console.print(

            Panel.fit(

                title,

                border_style="cyan"

            )

        )