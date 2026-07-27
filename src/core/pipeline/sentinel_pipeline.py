"""
============================================================
InsightForge Sentinel
Sentinel Pipeline
============================================================

Purpose:
    Executes all registered pipeline stages in sequence.

Author : InsightForge
Version : 1.0.0
"""

from core.pipeline.pipeline_context import (
    PipelineContext
)

from core.pipeline.stage_registry import (
    StageRegistry
)


class SentinelPipeline:
    """
    Executes the Sentinel pipeline.

    The pipeline is responsible only for orchestration.
    It does not contain any business logic.
    """

    # ==================================================
    # Constructor
    # ==================================================

    def __init__(self):

        self.registry = StageRegistry()

    # ==================================================
    # Register Stage
    # ==================================================

    def add_stage(
        self,
        stage
    ) -> None:

        self.registry.register(stage)

    # ==================================================
    # Execute Pipeline
    # ==================================================

    def run(
        self,
        context: PipelineContext
    ) -> PipelineContext:

        for stage in self.registry.get_stages():

            context = stage.execute(context)

        return context