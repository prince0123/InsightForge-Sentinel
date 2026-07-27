"""
============================================================
InsightForge Sentinel
Pipeline Builder
============================================================

Purpose:
    Builds and configures the Sentinel Pipeline.

Author : InsightForge
Version : 1.0.0
"""

from core.pipeline.sentinel_pipeline import (
    SentinelPipeline
)


class PipelineBuilder:
    """
    Responsible for constructing
    Sentinel Pipelines.

    Business stages are registered here.
    """

    # ==================================================
    # Build Pipeline
    # ==================================================

    def build(
        self
    ) -> SentinelPipeline:

        pipeline = SentinelPipeline()

        # ----------------------------------------------
        # Register Stages
        # ----------------------------------------------
        #
        # Sprint 17.2
        # These will be added gradually.
        #
        # pipeline.add_stage(
        #     LoadDatasetStage()
        # )
        #
        # pipeline.add_stage(
        #     PreprocessingStage()
        # )
        #
        # pipeline.add_stage(
        #     ProfilingStage()
        # )
        #
        # pipeline.add_stage(
        #     InferenceStage()
        # )
        #
        # pipeline.add_stage(
        #     SchemaStage()
        # )
        #
        # pipeline.add_stage(
        #     RuleStage()
        # )
        #
        # pipeline.add_stage(
        #     ValidationStage()
        # )
        #
        # pipeline.add_stage(
        #     HealthStage()
        # )
        #
        # pipeline.add_stage(
        #     ReportingStage()
        # )
        #

        return pipeline