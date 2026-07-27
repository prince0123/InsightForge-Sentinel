from core.pipeline.pipeline_context import (
    PipelineContext
)

from core.pipeline.pipeline_stage import (
    PipelineStage
)

from core.pipeline.sentinel_pipeline import (
    SentinelPipeline
)


class StageOne(PipelineStage):

    name = "Stage One"

    def execute(
        self,
        context
    ):

        print("Stage One")

        return context


class StageTwo(PipelineStage):

    name = "Stage Two"

    def execute(
        self,
        context
    ):

        print("Stage Two")

        return context


pipeline = SentinelPipeline()

pipeline.add_stage(StageOne())

pipeline.add_stage(StageTwo())

pipeline.run(
    PipelineContext()
)