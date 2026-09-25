import plotly.graph_objects as go
import streamlit as st
from stockmind.infrastructure.history.chart_data_repository import ChartDataRepository


def render(symbol: str, trading_days: int = 252):
    points = ChartDataRepository().load_by_symbol(symbol)
    if not points:
        st.warning("Keine Kursdaten vorhanden.")
        return
    visible = points[-trading_days:]
    fig = go.Figure(go.Scatter(
        x=[p.trading_date for p in visible],
        y=[p.close_price for p in visible],
        mode="lines", name="Schlusskurs",
        line=dict(color="#1f77b4", width=2),
    ))
    fig.update_layout(
        title="Aktueller Kursverlauf",
        xaxis_title="Datum", yaxis_title="Kurs",
        hovermode="x unified", showlegend=False,
    )
    st.plotly_chart(fig, width="stretch")
