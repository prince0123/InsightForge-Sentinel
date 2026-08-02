from pathlib import Path

from core.pipeline.pipeline_builder import (
    PipelineBuilder
)

from core.pipeline.pipeline_context import (
    PipelineContext
)

context = PipelineContext()

project_root = Path(__file__).resolve().parent.parent

context.dataset_path = (
    project_root
    / "data"
    / "sample"
    / "sample_sales.csv"
)

pipeline = PipelineBuilder().build()

context = pipeline.run(context)

print()

print("Rows:", context.profile["rows"])

print("Columns:", context.profile["columns"])