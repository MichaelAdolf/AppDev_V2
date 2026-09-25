import pandas as pd
import plotly.graph_objects as go
import streamlit as st


def render(history, profile_name: str):
    st.caption(
        f"Historischer Replay des aktuellen Modells für {profile_name}. "
        "Jeder Punkt verwendet nur Daten, die am jeweiligen Handelstag verfügbar waren."
    )
    if not history:
        st.warning(
            "Noch kein historischer Opportunity-Replay vorhanden. "
            "Bitte scripts/refresh_historical_opportunities.py ausführen."
        )
        return
    rows = [{
        "Datum": item.trading_date,
        "Opportunity Score": item.opportunity_score,
        "Confidence %": item.confidence * 100,
        "Hist. Trefferquote %": item.historical_success_rate * 100,
        "Hist. Stichprobe": item.historical_sample_count,
        "Signal": item.signal,
        "Risiko": item.risk_level,
        "Qualität": item.quality,
    } for item in history]
    df = pd.DataFrame(rows).sort_values("Datum")
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df["Datum"], y=df["Opportunity Score"],
        mode="lines", name="Opportunity Score",
        line=dict(color="#1f77b4", width=2),
    ))
    buy_rows = df[df["Signal"] == "BUY"]
    if not buy_rows.empty:
        fig.add_trace(go.Scatter(
            x=buy_rows["Datum"], y=buy_rows["Opportunity Score"],
            mode="markers", name="BUY-Signal",
            marker=dict(color="#00a046", size=6),
        ))
    fig.update_layout(
        title="Historische Opportunity-Entwicklung über 5 Jahre",
        xaxis_title="Datum", yaxis_title="Opportunity Score",
        yaxis=dict(range=[0, 100]), hovermode="x unified",
    )
    st.plotly_chart(fig, width="stretch")
    st.dataframe(df, width="stretch", hide_index=True)
