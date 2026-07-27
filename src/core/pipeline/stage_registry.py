"""
============================================================
InsightForge Sentinel
Stage Registry
============================================================

Purpose:
    Registers and manages pipeline stages.

Author : InsightForge
Version : 1.0.0
"""

from typing import List

from core.pipeline.pipeline_stage import (
    PipelineStage
)


class StageRegistry:
    """
    Maintains the ordered collection of stages
    executed by the Sentinel Pipeline.
    """

    def __init__(self):

        self._stages: List[PipelineStage] = []

    # ==================================================
    # Register Stage
    # ==================================================

    def register(
        self,
        stage: PipelineStage
    ) -> None:
        """
        Register a pipeline stage.
        """

        self._stages.append(stage)

    # ==================================================
    # Get All Stages
    # ==================================================

    def get_stages(
        self
    ) -> List[PipelineStage]:
        """
        Return registered stages.
        """

        return self._stages

    # ==================================================
    # Clear Registry
    # ==================================================

    def clear(
        self
    ) -> None:
        """
        Remove all registered stages.
        """

        self._stages.clear()

    # ==================================================
    # Count
    # ==================================================

    def count(
        self
    ) -> int:

        return len(self._stages)