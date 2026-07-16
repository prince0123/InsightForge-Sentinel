"""
============================================================
InsightForge Sentinel
Rule Engine
============================================================

Purpose:
    Builds an execution plan by matching business
    types to validation rules.

Author : InsightForge
Version : 3.0
"""

from pathlib import Path

from models.execution_task import ExecutionTask
from rules.rule_loader import RuleLoader


class RuleEngine:

    def __init__(self):

        self.loader = RuleLoader()

    # ======================================================
    # Public API
    # ======================================================

    def run(
        self,
        knowledge,
        industry="retail"
    ):

        rules = self._load_rule_pack(industry)

        execution_plan = []

        for column in knowledge.get_columns():

            business_type = knowledge.get_fact(
                column,
                "business_type"
            )

            for rule in rules:

                if not rule.is_enabled():
                    continue

                if rule.business_type != business_type:
                    continue

                task = ExecutionTask(

                    column=column,

                    business_type=business_type,

                    rule=rule

                )

                execution_plan.append(task)

        return {

            "engine": "RuleEngine",

            "status": "SUCCESS",

            "industry": industry,

            "rules_loaded": len(rules),

            "tasks_created": len(execution_plan),

            "execution_plan": execution_plan

        }

    # ======================================================
    # Internal
    # ======================================================

    def _load_rule_pack(self, industry):

        rules_folder = (
            Path(__file__)
            .resolve()
            .parent
        )

        rule_file = (
            rules_folder
            / industry
            / f"{industry}_rules.json"
        )

        return self.loader.load(rule_file)