"""
============================================================
InsightForge Sentinel
Rule Loader
============================================================

Purpose:
    Loads rule packs from JSON files and converts them
    into Rule objects.

Author : InsightForge
Version: 1.0
"""

import json
from pathlib import Path

from models.rule import Rule


class RuleLoader:

    """
    Loads JSON rule packs.
    """

    def load(self, file_path):

        file_path = Path(file_path)

        if not file_path.exists():

            raise FileNotFoundError(
                f"Rule pack not found: {file_path}"
            )

        with open(file_path, "r", encoding="utf-8") as file:

            data = json.load(file)

        rules = []

        for item in data:

            rule = Rule(

                rule_id=item["rule_id"],

                name=item["name"],

                business_type=item["business_type"],

                validation=item["validation"],

                severity=item["severity"],

                business_impact=item["business_impact"],

                recommendation=item["recommendation"],

                enabled=item.get("enabled", True),

                version=item.get("version", "1.0")

            )

            rules.append(rule)

        return rules