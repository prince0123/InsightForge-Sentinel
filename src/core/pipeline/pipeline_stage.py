"""
============================================================
InsightForge Sentinel
Pipeline Stage
============================================================

Purpose:
    Defines the standard contract for every pipeline stage.

Author : InsightForge
Version : 1.1.0
"""

from abc import ABC
from abc import abstractmethod

from core.pipeline.pipeline_context import (
    PipelineContext
)


class PipelineStage(ABC):
    """
    Base class for all Sentinel pipeline stages.
    """

    version = "1.1.0"

    description = ""

    # ==================================================
    # Stage Name
    # ==================================================

    @property
    def stage_name(self) -> str:
        """
        Human-readable stage name.

        Example

        HealthStage

        becomes

        Health Stage
        """

        name = self.__class__.__name__

        if name.endswith("Stage"):
            name = name[:-5]

        result = ""

        for index, character in enumerate(name):

            if (
                index > 0
                and character.isupper()
            ):
                result += " "

            result += character

        return result

    # ==================================================
    # Before Execute
    # ==================================================

    def before_execute(
        self,
        context: PipelineContext
    ) -> PipelineContext:

        return context

    # ==================================================
    # Execute
    # ==================================================

    @abstractmethod
    def execute(
        self,
        context: PipelineContext
    ) -> PipelineContext:

        raise NotImplementedError

    # ==================================================
    # After Execute
    # ==================================================

    def after_execute(
        self,
        context: PipelineContext
    ) -> PipelineContext:

        return context