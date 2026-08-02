"""
============================================================
InsightForge Sentinel
Profiling Stage
============================================================

Purpose:
    Profiles the loaded dataset.

Author : InsightForge
Version : 1.0.0
"""

from profiling import profiler
from profiling.profiler import (
    DataProfiler
)

from core.pipeline.pipeline_context import (
    PipelineContext
)

from core.pipeline.pipeline_stage import (
    PipelineStage
)


class ProfilingStage(PipelineStage):
    """
    Builds dataset profile information.
    """

    def __init__(
    self,
    profiler):
        self.profiler = profiler

    # ==================================================

    def execute(
        self,
        context: PipelineContext
    ) -> PipelineContext:

        context.profile = self.profiler.profile(
            context.dataframe
        )

        return context