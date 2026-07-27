from pathlib import Path

from core.pipeline.pipeline_context import (
    PipelineContext
)

from core.pipeline.stages.load_dataset_stage import (
    LoadDatasetStage
)

context = PipelineContext()

project_root = Path(__file__).resolve().parent.parent

context.dataset_path = (
    project_root
    / "data"
    / "sample"
    / "sample_sales.csv"
)

stage = LoadDatasetStage()

context = stage.execute(context)

print(context.dataframe.shape)