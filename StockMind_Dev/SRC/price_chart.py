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

from stockmind.application.dashboard.use_cases.buy_period_dashboard_use_case import (
    BuyPeriodDashboardUseCase
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

    buy_periods = (
        BuyPeriodDashboardUseCase()
        .load(
            symbol=symbol,
            max_gap_days=3
        )
    )



    st.write(
        f"BuyPerioden gefunden: {buy_periods.period_count}"
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

    for period in buy_periods.periods:
        if period.status =="SUCCESSFULL":
            fill_color = (
                "rgb(0,50,0,0.15)"
            )

        else:
            fill_color = (
                "rgb(220,0,0,0.15)"
            )

        period_end = (
            datetime.fromisoformat(
                period.end_date
            )
            +timedelta(days=3)
        )

        fig.add_vrect(
            x0=period.start_date,
            x1=period_end.date().isoformat(),
            fillcolor=fill_color,
            opacity=1.0,
            layer="below",
            line_width=0
        )

    #
    # Setup-Zonen
    #

    #
    # Setup-Marker
    #

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
