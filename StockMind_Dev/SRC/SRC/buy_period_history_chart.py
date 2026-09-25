import plotly.graph_objects as go
import streamlit as st
from stockmind.application.dashboard.use_cases.buy_period_dashboard_use_case import BuyPeriodDashboardUseCase
from stockmind.infrastructure.history.chart_data_repository import ChartDataRepository

COLORS = {
    "TARGET_HIT": "rgba(0, 160, 70, 0.20)",
    "INCOMPLETE_WINDOW": "rgba(90, 120, 170, 0.18)",
}


def render(symbol: str, profile_name: str, analysis_period: str = "5y"):
    points = ChartDataRepository().load_by_symbol(symbol)
    periods = BuyPeriodDashboardUseCase().load(
        symbol=symbol, profile_name=profile_name,
        analysis_period=analysis_period, max_gap_days=3,
    ).periods
    if not points:
        st.warning("Keine Kursdaten für die Periodendarstellung vorhanden.")
        return
    date_to_price = {p.trading_date: p.close_price for p in points}
    fig = go.Figure(go.Scatter(
        x=[p.trading_date for p in points],
        y=[p.close_price for p in points],
        mode="lines", name="Schlusskurs",
        line=dict(color="#1f77b4", width=2),
    ))
    marker_x=[]; marker_y=[]; custom=[]; marker_colors=[]
    for period in periods:
        color = COLORS.get(period.outcome, "rgba(210, 45, 45, 0.17)")
        fig.add_vrect(
            x0=period.start_date, x1=period.end_date,
            fillcolor=color, opacity=1.0, layer="below", line_width=0,
        )
        if period.start_date in date_to_price:
            marker_x.append(period.start_date)
            marker_y.append(date_to_price[period.start_date])
            marker_colors.append(
                "#00a046" if period.outcome == "TARGET_HIT"
                else "#6078aa" if period.outcome == "INCOMPLETE_WINDOW"
                else "#d22d2d"
            )
            custom.append([
                period.end_date, period.buy_signal_count,
                period.calendar_duration_days, period.outcome,
                period.entry_price, period.days_to_target,
                period.max_gain_pct, period.max_drawdown_pct,
            ])
    if marker_x:
        fig.add_trace(go.Scatter(
            x=marker_x, y=marker_y, mode="markers", name="BUY-Perioden",
            marker=dict(size=8, color=marker_colors), customdata=custom,
            hovertemplate=(
                "Start: %{x}<br>Ende: %{customdata[0]}<br>"
                "BUY-Signaltage: %{customdata[1]}<br>"
                "Kalendertage: %{customdata[2]}<br>"
                "Outcome: %{customdata[3]}<br>"
                "Entry: %{customdata[4]:.2f}<br>"
                "Tage bis Ziel: %{customdata[5]}<br>"
                "Max. Gewinn: %{customdata[6]:.2f}%<br>"
                "Max. Rückgang: %{customdata[7]:.2f}%<extra></extra>"
            ),
        ))
    fig.update_layout(
        title=f"{symbol}: Kursverlauf mit {profile_name}-BUY-Perioden",
        xaxis_title="Datum", yaxis_title="Kurs", hovermode="closest",
    )
    st.plotly_chart(fig, width="stretch")
