import plotly.graph_objects as go
import streamlit as st

from stockmind.infrastructure.history.chart_data_repository import (
    ChartDataRepository
)

from stockmind.infrastructure.history.historical_setup_repository import (
    HistoricalSetupRepository
)


def render(
    symbol: str
):

    points = (
        ChartDataRepository()
        .load_by_symbol(
            symbol
        )
    )

    setups = (
        HistoricalSetupRepository()
        .load_by_symbol(
            symbol
        )
    )

    if not points:

        st.warning(
            "Keine Chartdaten vorhanden."
        )

        return

    dates = [
        point.trading_date
        for point in points
    ]

    close_prices = [
        point.close_price
        for point in points
    ]

    upper = [
        point.bollinger_upper
        for point in points
    ]

    middle = [
        point.bollinger_middle
        for point in points
    ]

    lower = [
        point.bollinger_lower
        for point in points
    ]

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=dates,
            y=close_prices,
            mode="lines",
            name="Close"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=dates,
            y=upper,
            mode="lines",
            name="BB Upper",
            line=dict(
                dash="dash"
            )
        )
    )

    fig.add_trace(
        go.Scatter(
            x=dates,
            y=middle,
            mode="lines",
            name="BB Middle",
            line=dict(
                dash="dot"
            )
        )
    )

    fig.add_trace(
        go.Scatter(
            x=dates,
            y=lower,
            mode="lines",
            name="BB Lower",
            line=dict(
                dash="dash"
            )
        )
    )

    successful_setups = [
        setup
        for setup in setups
        if setup.success
    ]

    failed_setups = [
        setup
        for setup in setups
        if not setup.success
    ]

    fig.add_trace(
        go.Scatter(
            x=[
                setup.setup_date
                for setup in successful_setups
            ],
            y=[
                setup.entry_price
                for setup in successful_setups
            ],
            mode="markers",
            name="Successful Setup",
            marker=dict(
                color="green",
                size=10,
                symbol="circle"
            )
        )
    )

    fig.add_trace(
        go.Scatter(
            x=[
                setup.setup_date
                for setup in failed_setups
            ],
            y=[
                setup.entry_price
                for setup in failed_setups
            ],
            mode="markers",
            name="Failed Setup",
            marker=dict(
                color="red",
                size=10,
                symbol="x"
            )
        )
    )

    fig.update_layout(
        title=f"{symbol} Kurschart mit Bollinger und Setups",
        xaxis_title="Datum",
        yaxis_title="Kurs",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
