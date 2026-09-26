import plotly.graph_objects as go
import streamlit as st
from stockmind.infrastructure.history.chart_data_repository import ChartDataRepository


def render(symbol: str):
    points = ChartDataRepository().load_by_symbol(symbol)
    if not points:
        st.warning("Keine Chartdaten vorhanden.")
        return
    dates = [point.trading_date for point in points]
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=dates, y=[p.close_price for p in points], mode="lines",
        name="Schlusskurs", line=dict(color="#1f77b4", width=2),
    ))
    for name, values, dash in (
        ("BB Upper", [p.bollinger_upper for p in points], "dash"),
        ("BB Middle", [p.bollinger_middle for p in points], "dot"),
        ("BB Lower", [p.bollinger_lower for p in points], "dash"),
    ):
        fig.add_trace(go.Scatter(
            x=dates, y=values, mode="lines", name=name,
            line=dict(dash=dash, color="rgba(150,150,150,0.75)"),
        ))
    fig.update_layout(
        title=f"{symbol} Kursverlauf mit Bollinger-Bändern",
        xaxis_title="Datum", yaxis_title="Kurs", hovermode="x unified",
        legend=dict(orientation="h", yanchor="bottom", y=1.02,
                    xanchor="center", x=0.5),
    )
    st.plotly_chart(fig, width="stretch")
