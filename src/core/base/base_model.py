"""
============================================================
InsightForge Sentinel
Base Model
============================================================

Purpose:
    Base class for all Sentinel business models.

Author : InsightForge
Version : 1.0
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class BaseModel:

    created_at: datetime = datetime.now()

    version: str = "1.0"