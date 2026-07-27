from time import sleep

from rich.console import Console
from rich.progress import Progress


class ProgressPipeline:

    def __init__(self):

        self.console = Console()

    def advance(self, stage):

        with Progress() as progress:

            task = progress.add_task(stage, total=100)

            while not progress.finished:

                progress.update(task, advance=5)

                sleep(0.02)

    def finish(self):

        self.console.print()

        self.console.print(
            "[bold green]✓ Initialization Complete[/bold green]"
        )

        self.console.print()