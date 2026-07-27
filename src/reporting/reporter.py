"""
============================================================
InsightForge Sentinel
Reporter
============================================================

Purpose:
    Coordinates all reporting sections and produces the
    final Sentinel report.

Author : InsightForge
Version : 1.0
"""

from reporting.sections.executive_section import (
    ExecutiveSection
)

from reporting.sections.profile_section import (
    ProfileSection
)

from reporting.sections.schema_section import (
    SchemaSection
)

from reporting.sections.validation_section import (
    ValidationSection
)

from reporting.sections.health_section import (
    HealthSection
)


class SentinelReporter:

    # ==================================================
    # Constructor
    # ==================================================

    def __init__(self):

        self.executive = ExecutiveSection()

        self.profile = ProfileSection()

        self.schema = SchemaSection()

        self.validation = ValidationSection()

        self.health = HealthSection()

    # ==================================================
    # Report
    # ==================================================

    def report(

        self,

        profile,

        schema,

        validation,

        health

    ):

        self.executive.build(

            profile,

            validation,

            health

        )

        self.profile.build(

            profile

        )

        self.schema.build(

            schema

        )

        self.validation.build(

            validation

        )

        self.health.render(

            health

        )