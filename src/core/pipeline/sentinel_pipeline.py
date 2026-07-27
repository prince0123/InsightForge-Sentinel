"""
============================================================
Sentinel Pipeline
============================================================
"""

from core.pipeline.pipeline_context import (
    PipelineContext
)


class SentinelPipeline:

    def __init__(self):

        self.stages = []

    # ==============================================

    def add_stage(

        self,

        stage

    ):

        self.stages.append(stage)

    # ==============================================

    def run(

        self,

        context: PipelineContext

    ):

        for stage in self.stages:

            context = stage.execute(context)

        return context