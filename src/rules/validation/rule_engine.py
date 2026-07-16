"""
============================================================
InsightForge Sentinel
Rule Engine
============================================================

Purpose:
    Loads rule packs and selects applicable rules
    for a dataset based on inferred business types.

Author : InsightForge
Version : 2.0
"""

from pathlib import Path

from rules.rule_loader import RuleLoader


class RuleEngine:
    """
    Selects applicable rules for the current dataset.

    The Rule Engine DOES NOT execute rules.

    It simply determines which rules should be
    passed to the Validation Engine.
    """

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

        applicable_rules = []

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

                applicable_rules.append(rule)

        return {

            "engine": "RuleEngine",

            "status": "SUCCESS",

            "industry": industry,

            "rules_loaded": len(rules),

            "applicable_rules": applicable_rules,

            "rules_selected": len(applicable_rules)

        }

    # ======================================================
    # Internal
    # ======================================================

    def _load_rule_pack(self, industry):

        project_root = (
            Path(__file__)
            .resolve()
            .parent
            .parent
            .parent
        )

        rule_file = (
            project_root
            / "rules"
            / industry
            / f"{industry}_rules.json"
        )

        return self.loader.load(rule_file)