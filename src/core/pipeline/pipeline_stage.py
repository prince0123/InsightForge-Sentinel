"""
Pipeline Stage
"""

from abc import ABC
from abc import abstractmethod

from core.pipeline.pipeline_context import (
    PipelineContext
)


class PipelineStage(ABC):

    @abstractmethod
    def execute(

        self,

        context: PipelineContext

    ) -> PipelineContext:

        raise NotImplementedError