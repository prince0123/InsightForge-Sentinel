"""
============================================================
InsightForge Sentinel
Load Dataset Stage
============================================================

Purpose:
    Loads the dataset into the Pipeline Context.

Author : InsightForge
Version : 1.0.0
"""

from connectors.file_connector import FileConnector

from core.pipeline.pipeline_context import (
    PipelineContext
)

from core.pipeline.pipeline_stage import (
    PipelineStage
)


class LoadDatasetStage(PipelineStage):

    name = "Load Dataset"

    description = "Loads dataset from disk."

    # ==================================================

    def __init__(self):

        self.connector = FileConnector()

    # ==================================================

    def execute(
        self,
        context: PipelineContext
    ) -> PipelineContext:

        if context.dataset_path is None:

            raise ValueError(
                "PipelineContext.dataset_path is not set."
            )

        context.dataframe = self.connector.load(
            context.dataset_path
        )

        return context