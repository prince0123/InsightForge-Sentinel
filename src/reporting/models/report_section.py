"""
============================================================
InsightForge Sentinel
Report Section Model
============================================================
"""


class ReportSection:

    def __init__(

        self,

        title,

        content=None,

        widgets=None

    ):

        self.title = title

        self.content = content or {}

        self.widgets = widgets or []