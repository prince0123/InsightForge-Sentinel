from core.pipeline.pipeline_stage import PipelineStage
from core.pipeline.pipeline_context import PipelineContext


class HealthStage(PipelineStage):

    def execute(
        self,
        context
    ):
        return context


print(HealthStage().stage_name)