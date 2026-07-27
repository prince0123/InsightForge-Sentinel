"""
============================================================
Console Renderer
============================================================
"""

from reporting.renderers.base_renderer import (
    BaseRenderer
)


class ConsoleRenderer(BaseRenderer):

    def render(
        self,
        report
    ):

        for section in report:

            print()

            print("=" * 70)

            print(section.title)

            print("=" * 70)

            for key, value in section.content.items():

                print(f"{key:<30}: {value}")