"""
============================================================
InsightForge Sentinel
Base Report Section
============================================================

Purpose:
    Defines the contract for every reporting section.

Author : InsightForge
Version : 1.0
"""

from abc import ABC, abstractmethod


class BaseSection(ABC):

    @abstractmethod
    def build(self, **kwargs):
        """
        Build a presentation model.

        Returns
        -------
        dict
            Structured report data.
        """
        pass