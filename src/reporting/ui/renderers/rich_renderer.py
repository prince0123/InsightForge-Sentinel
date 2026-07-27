from rich.console import Console


class RichRenderer:

    def __init__(self):

        self.console = Console()

    def display(self, component):

        self.console.print(component)