from rich.progress_bar import ProgressBar

from rich.panel import Panel

from reporting.ui.widgets.base_widget import BaseWidget


class ScoreBar(BaseWidget):

    def render(

        self,

        title,

        score

    ):

        bar = ProgressBar(

            total=100,

            completed=score

        )

        return Panel(

            bar,

            title=f"{title} ({score:.1f}%)",

            border_style=self.theme.colors.BORDER

        )