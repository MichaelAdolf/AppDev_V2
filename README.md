from datetime import datetime
from datetime import timedelta

import plotly.graph_objects as go
import streamlit as st

from stockmind.infrastructure.history.chart_data_repository import (
    ChartDataRepository
)

from stockmind.infrastructure.history.historical_setup_repository import (
    HistoricalSetupRepository
)


def _parse_date(
    value: str
):

    return datetime.fromisoformat(
        value
    )


def _setup_end_date(
    setup
):

    start = _parse_date(
        setup.setup_date
    )

    days = (
        setup.days_to_target
        if setup.days_to_target is not None
        else 60
    )

    return (
        start
        + timedelta(
            days=days
        )
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

    #
    # Kurs
    #

    fig.add_trace(
        go.Scatter(
            x=dates,
            y=close_prices,
            mode="lines",
            name="Close",
            line=dict(
                color="#1f77b4",
                width=2
            )
        )
    )

    #
    # Bollinger
    #

    fig.add_trace(
        go.Scatter(
            x=dates,
            y=upper,
            mode="lines",
            name="BB Upper",
            line=dict(
                dash="dash",
                color="rgba(120,120,120,0.7)"
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
                dash="dot",
                color="rgba(120,120,120,0.7)"
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
                dash="dash",
                color="rgba(120,120,120,0.7)"
            )
        )
    )

    #
    # Setup-Zonen
    #

    for setup in setups:

        x0 = setup.setup_date

        x1 = (
            _setup_end_date(
                setup
            )
            .date()
            .isoformat()
        )

        fill_color = (
            "rgba(0, 160, 0, 0.16)"
            if setup.success
            else "rgba(220, 0, 0, 0.14)"
        )

        fig.add_vrect(
            x0=x0,
            x1=x1,
            fillcolor=fill_color,
            opacity=1.0,
            layer="below",
            line_width=0
        )

    #
    # Setup-Marker
    #

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
            ),
            text=[
                (
                    f"Success<br>"
                    f"Entry: {setup.entry_price:.2f}<br>"
                    f"Days: {setup.days_to_target}<br>"
                    f"Max Gain: {setup.max_gain_pct:.1f}%<br>"
                    f"Drawdown: {setup.max_drawdown_pct:.1f}%"
                )
                for setup in successful_setups
            ],
            hoverinfo="text"
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
            ),
            text=[
                (
                    f"Failed<br>"
                    f"Entry: {setup.entry_price:.2f}<br>"
                    f"Days: {setup.days_to_target}<br>"
                    f"Max Gain: {setup.max_gain_pct:.1f}%<br>"
                    f"Drawdown: {setup.max_drawdown_pct:.1f}%"
                )
                for setup in failed_setups
            ],
            hoverinfo="text"
        )
    )

    fig.update_layout(
        title=f"{symbol} Kurschart mit Bollinger und historischen Setups",
        xaxis_title="Datum",
        yaxis_title="Kurs",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5
        ),
        hovermode="x unified"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
