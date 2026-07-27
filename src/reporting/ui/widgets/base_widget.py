"""
Base Widget
"""

from abc import ABC
from rich.console import Console

from reporting.ui.design.theme import SentinelTheme


class BaseWidget(ABC):

    def __init__(self):

        self.console = Console()

        self.theme = SentinelTheme()