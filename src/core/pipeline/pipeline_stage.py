"""
============================================================
InsightForge Sentinel
Pipeline Stage
============================================================

Purpose:
    Defines the standard contract for every pipeline stage.

Author : InsightForge
Version : 1.0.0
"""

from abc import ABC
from abc import abstractmethod

from core.pipeline.pipeline_context import (
    PipelineContext
)


class PipelineStage(ABC):
    """
    Base class for all pipeline stages.

    A stage is responsible for orchestrating one
    step of the Sentinel pipeline.
    """

    name: str = "Pipeline Stage"

    description: str = ""

    version: str = "1.0.0"

    @abstractmethod
    def execute(
        self,
        context: PipelineContext
    ) -> PipelineContext:
        """
        Execute the pipeline stage.

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