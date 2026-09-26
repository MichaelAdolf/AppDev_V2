import plotly.graph_objects as go
import streamlit as st
from stockmind.application.dashboard.use_cases.buy_period_dashboard_use_case import BuyPeriodDashboardUseCase
from stockmind.infrastructure.history.chart_data_repository import ChartDataRepository


def render(symbol: str, profile_name: str, analysis_period: str = "5y"):
    points = ChartDataRepository().load_by_symbol(symbol)
    periods = BuyPeriodDashboardUseCase().load(
        symbol=symbol, profile_name=profile_name,
        analysis_period=analysis_period, max_gap_days=3,
    ).periods
    if not points:
        st.warning("Keine Kursdaten für die Periodendarstellung vorhanden.")
        return
    fig = go.Figure(go.Scatter(
        x=[p.trading_date for p in points],
        y=[p.close_price for p in points],
        mode="lines", name="Schlusskurs",
        line=dict(color="#1f77b4", width=2),
    ))
    for period in periods:
        if period.outcome == "TARGET_HIT":
            color = "rgba(0, 160, 70, 0.22)"
        elif period.outcome == "INCOMPLETE_WINDOW":
            color = "rgba(120, 120, 120, 0.18)"
        else:
            color = "rgba(210, 45, 45, 0.20)"
        fig.add_vrect(
            x0=period.start_date, x1=period.end_date,
            fillcolor=color, opacity=1.0, layer="below", line_width=0,
        )
    fig.update_layout(
        title=(f"{symbol}: Historische BUY-Perioden ({profile_name}) | "
               "Grün = Ziel erreicht, Rot = Ziel nicht erreicht, Grau = offen"),
        xaxis_title="Datum", yaxis_title="Kurs", hovermode="x unified",
    )
    st.plotly_chart(fig, width="stretch")
