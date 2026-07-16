"""
============================================================
InsightForge Sentinel
Column Profile
============================================================

Purpose:
    Represents all metadata and intelligence discovered
    for a dataset column.

Author : InsightForge
Version : 1.0
"""


class ColumnProfile:

    def __init__(

        self,

        name,

        logical_type,

        physical_type,

        confidence=0,

        nullable=True,

        unique=False,

        uniqueness_ratio=0,

        recommended_validators=None

    ):

        self.name = name

        self.logical_type = logical_type

        self.physical_type = physical_type

        self.confidence = confidence

        self.nullable = nullable

        self.unique = unique

        self.uniqueness_ratio = uniqueness_ratio

        self.recommended_validators = (
            recommended_validators or []
        )

    # ===============================================

    def to_dict(self):

        return {

            "name": self.name,

            "logical_type": self.logical_type,

            "physical_type": self.physical_type,

            "confidence": self.confidence,

            "nullable": self.nullable,

            "unique": self.unique,

            "uniqueness_ratio": self.uniqueness_ratio,

            "recommended_validators":
                self.recommended_validators

        }

    # ===============================================

    @classmethod
    def from_dict(cls, data):

        return cls(**data)

    # ===============================================

    def __repr__(self):

        return (

            f"ColumnProfile("

            f"name='{self.name}', "

            f"logical_type='{self.logical_type}', "

            f"physical_type='{self.physical_type}', "

            f"confidence={self.confidence})"

        )

    # ===============================================

    def __str__(self):

        return (

            f"{self.name}"

            f" [{self.logical_type}]"

        )