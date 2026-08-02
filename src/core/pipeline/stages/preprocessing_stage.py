"""
============================================================
InsightForge Sentinel
Preprocessing Stage
============================================================

Purpose:
    Executes preprocessing on the loaded dataset.

Author : InsightForge
Version : 1.0.0
"""

from preprocessing.preprocessor import (
    Preprocessor
)

from preprocessing.datatype_inference import (
    DataTypeInference
)

from core.pipeline.pipeline_context import (
    PipelineContext
)

from core.pipeline.pipeline_stage import (
    PipelineStage
)


class PreprocessingStage(PipelineStage):
    """
    Cleans and standardises the dataset before
    downstream analysis.
    """

    def __init__(
        self,
        preprocessor,
        datatype_engine):

        self.preprocessor = preprocessor

        self.datatype_engine = datatype_engine

    # ==================================================

    def execute(
        self,
        context: PipelineContext
    ) -> PipelineContext:

        context.dataframe = self.preprocessor.process(
            context.dataframe
        )

        context.dataframe = self.datatype_engine.process(
            context.dataframe
        )

        return context