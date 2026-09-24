from datetime import datetime, timedelta

import plotly.graph_objects as go
import streamlit as st

from stockmind.application.dashboard.use_cases.buy_period_dashboard_use_case import (
    BuyPeriodDashboardUseCase,
)
from stockmind.infrastructure.history.chart_data_repository import (
    ChartDataRepository,
)


OUTCOME_COLORS = {
    "TARGET_HIT": "rgba(0, 160, 70, 0.18)",
    "BELOW_TARGET": "rgba(180, 170, 0, 0.18)",
    "FLAT": "rgba(120, 120, 120, 0.15)",
    "NEGATIVE": "rgba(220, 0, 0, 0.16)",
    "INCOMPLETE_WINDOW": "rgba(30, 120, 220, 0.14)",
}

OUTCOME_LABELS = {
    "TARGET_HIT": "Ziel erreicht",
    "BELOW_TARGET": "Positiv unter Ziel",
    "FLAT": "Seitwärts",
    "NEGATIVE": "Negativ",
    "INCOMPLETE_WINDOW": "Noch offen",
}


def render(
    symbol: str,
    profile_name: str = "balanced",
    analysis_period: str = "5y",
    max_gap_days: int = 3,
):
    points = ChartDataRepository().load_by_symbol(symbol)
    buy_periods = BuyPeriodDashboardUseCase().load(
        symbol=symbol,
        profile_name=profile_name,
        analysis_period=analysis_period,
        max_gap_days=max_gap_days,
    )

    st.caption(
        f"BUY-Perioden im Chart: {buy_periods.period_count} | "
        f"Profil: {profile_name} | Historie: {analysis_period}"
    )

    if not points:
        st.warning("Keine Chartdaten vorhanden.")
        return

    dates = [point.trading_date for point in points]
    close_prices = [point.close_price for point in points]
    upper = [point.bollinger_upper for point in points]
    middle = [point.bollinger_middle for point in points]
    lower = [point.bollinger_lower for point in points]

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=dates,
            y=close_prices,
            mode="lines",
            name="Close",
            line=dict(color="#1f77b4", width=2),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=dates,
            y=upper,
            mode="lines",
            name="BB Upper",
            line=dict(dash="dash", color="rgba(120,120,120,0.7)"),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=dates,
            y=middle,
            mode="lines",
            name="BB Middle",
            line=dict(dash="dot", color="rgba(120,120,120,0.7)"),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=dates,
            y=lower,
            mode="lines",
            name="BB Lower",
            line=dict(dash="dash", color="rgba(120,120,120,0.7)"),
        )
    )

    for period in buy_periods.periods:
        fill_color = OUTCOME_COLORS.get(
            period.outcome,
            "rgba(120, 120, 120, 0.12)",
        )
        period_end = (
            datetime.fromisoformat(period.end_date)
            + timedelta(days=max_gap_days)
        )
        fig.add_vrect(
            x0=period.start_date,
            x1=period_end.date().isoformat(),
            fillcolor=fill_color,
            opacity=1.0,
            layer="below",
            line_width=0,
            annotation_text=(
                f"{OUTCOME_LABELS.get(period.outcome, period.outcome)} | "
                f"{period.buy_signal_count} BUY-Tage"
            ),
            annotation_position="top left",
        )

    fig.update_layout(
        title=(
            f"{symbol} Kurschart mit Bollinger und "
            f"{profile_name}-BUY-Perioden"
        ),
        xaxis_title="Datum",
        yaxis_title="Kurs",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5,
        ),
        hovermode="x unified",
    )
    st.plotly_chart(fig, width="stretch")
