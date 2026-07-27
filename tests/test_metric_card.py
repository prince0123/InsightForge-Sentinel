from reporting.renderers.rich_renderer import (
    RichRenderer
)

from reporting.widgets.metric_card import (
    MetricCard
)

from reporting.design.theme import SentinelTheme

theme = SentinelTheme()

renderer = RichRenderer()

card = MetricCard(

    title="Data Trust Index",

    value="91 / 100",

    subtitle="HIGH CONFIDENCE",

    icon=theme.icons.TRUST

)

renderer.display(

    card.build()

)