"""
============================================================
Base Engine
============================================================
"""

from abc import ABC
from abc import abstractmethod

from core.pipeline.pipeline_context import (
    PipelineContext
)


class BaseEngine(ABC):

    name = "Base Engine"

    version = "1.0"

    @abstractmethod
    def run(

        self,

        context: PipelineContext

    ) -> PipelineContext:

        """
        Execute engine.

        Returns updated PipelineContext.
        """

        raise NotImplementedError