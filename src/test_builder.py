from core.pipeline.pipeline_builder import (
    PipelineBuilder
)

builder = PipelineBuilder()

pipeline = builder.build()

print(type(pipeline).__name__)