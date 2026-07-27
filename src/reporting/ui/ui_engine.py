"""
============================================================
InsightForge Sentinel
UI Engine
============================================================

Purpose:
    Controls the complete Sentinel user interface lifecycle.

Author : InsightForge
Version : 1.0
"""

from reporting.ui.boot_screen import BootScreen
from reporting.ui.progress_pipeline import ProgressPipeline


class UIEngine:

    def __init__(self):

        self.boot = BootScreen()

        self.progress = ProgressPipeline()

    # -------------------------------------------------

    def start(self):

        self.boot.show()

    # -------------------------------------------------

    def stage(self, message):

        self.progress.advance(message)

    # -------------------------------------------------

    def finish(self):

        self.progress.finish()