"""
============================================================
InsightForge Sentinel
Knowledge Model
============================================================

Purpose:
    Shared knowledge repository used by Sentinel engines.

Author : InsightForge
Version: 1.0
"""


class KnowledgeModel:
    """
    Shared repository for inferred knowledge.

    Each column in a dataset has a collection
    of facts that are gradually populated by
    different engines.

    Example

    Order_ID

    {
        "business_type": "Identifier",
        "primary_key_confidence": 85,
        "risk": "LOW"
    }
    """

    def __init__(self):

        self.columns = {}

    # ======================================================
    # Column Management
    # ======================================================

    def add_column(self, column_name):

        if column_name not in self.columns:

            self.columns[column_name] = {}

    # ======================================================
    # Knowledge Management
    # ======================================================

    def set_fact(self, column_name, key, value):

        self.add_column(column_name)

        self.columns[column_name][key] = value

    def get_fact(self, column_name, key, default=None):

        if column_name not in self.columns:

            return default

        return self.columns[column_name].get(key, default)

    # ======================================================
    # Retrieval
    # ======================================================

    def get_column(self, column_name):

        return self.columns.get(column_name, {})

    def get_columns(self):

        return list(self.columns.keys())

    def to_dict(self):

        return self.columns

    # ======================================================
    # Utility
    # ======================================================

    def __len__(self):

        return len(self.columns)

    def __contains__(self, column_name):

        return column_name in self.columns

    def __repr__(self):

        return f"KnowledgeModel(columns={len(self.columns)})"