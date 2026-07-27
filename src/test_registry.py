from core.pipeline.stage_registry import StageRegistry
from core.pipeline.pipeline_stage import PipelineStage
from core.pipeline.pipeline_context import PipelineContext


class DummyStage(PipelineStage):

    name = "Dummy"

    def execute(
        self,
        context: PipelineContext
    ) -> PipelineContext:

        return context


registry = StageRegistry()

registry.register(
    DummyStage()
)

print(registry.count())

print(registry.get_stages()[0].name)