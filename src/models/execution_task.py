"""
============================================================
InsightForge Sentinel
Execution Task Model
============================================================

Purpose:
    Represents a single validation task to be executed
    by the Validation Engine.

Author : InsightForge
Version : 1.0
"""


class ExecutionTask:

    """
    Represents one validation task.

    Example

    Column:
        Order_ID

    Rule:
        RET-001

    Business Type:
        Identifier
    """

    def __init__(
        self,
        column,
        business_type,
        rule
    ):

        self.column = column

        self.business_type = business_type

        self.rule = rule

    # ======================================================

    def to_dict(self):

        return {

            "column": self.column,

            "business_type": self.business_type,

            "rule": self.rule.to_dict()

        }

    # ======================================================

    def __repr__(self):

        return (

            f"ExecutionTask("
            f"{self.column}, "
            f"{self.rule.rule_id}"
            f")"

        )