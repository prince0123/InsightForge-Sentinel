"""
============================================================
Base Renderer
============================================================
"""

from abc import ABC, abstractmethod


class BaseRenderer(ABC):

    @abstractmethod
    def render(
        self,
        report
    ):
        pass
