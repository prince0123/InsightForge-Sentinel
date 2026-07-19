"""
============================================================
InsightForge Sentinel
Base Scoring Policy
============================================================

Purpose:
    Defines the interface for all scoring policies.

Author : InsightForge
Version : 1.0
"""

from abc import ABC, abstractmethod


class BaseScoringPolicy(ABC):

    @abstractmethod
    def overall_score(
        self,
        metrics
    ):
        pass

    @abstractmethod
    def risk_level(
        self,
        score
    ):
        pass

    @abstractmethod
    def summary(
        self,
        score
    ):
        pass