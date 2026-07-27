"""
============================================================
InsightForge Sentinel
Base Engine
============================================================

Purpose:
    Defines the standard contract for every Sentinel engine.

Author : InsightForge
Version : 1.0.0
"""

from abc import ABC
from abc import abstractmethod

from core.pipeline.pipeline_context import (
    PipelineContext
)


class BaseEngine(ABC):
    """
    Base class for all Sentinel engines.

    Every engine must implement run() and
    return the updated PipelineContext.
    """

    name: str = "Base Engine"

    version: str = "1.0.0"

    description: str = ""

    @abstractmethod
    def run(
        self,
        context: PipelineContext
    ) -> PipelineContext:
        """
        Execute the engine.

        Parameters
        ----------
        context
            Shared pipeline context.

        Returns
        -------
        PipelineContext
            Updated pipeline context.
        """
        raise NotImplementedError