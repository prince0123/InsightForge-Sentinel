"""
============================================================
InsightForge Sentinel
Grade Calculator
============================================================
"""


class GradeCalculator:

    def calculate(
        self,
        score: float
    ) -> str:

        if score >= 95:
            return "A+"

        if score >= 90:
            return "A"

        if score >= 85:
            return "B+"

        if score >= 75:
            return "B"

        if score >= 65:
            return "C"

        if score >= 50:
            return "D"

        return "F"