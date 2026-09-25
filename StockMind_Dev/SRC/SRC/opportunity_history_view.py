import pandas as pd
import plotly.graph_objects as go
import streamlit as st


def render(history, profile_name: str):
    st.caption(f"Aktives Profil: {profile_name}. Pro Datum wird nur der neueste Analysewert verwendet.")
    if not history:
        st.warning("Keine Analysehistorie für dieses Profil vorhanden.")
        return
    rows = [{
        "Datum": h.analysis_date,
        "Opportunity Score": h.opportunity_score,
        "Confidence %": h.confidence * 100,
        "Historische Evidenz %": h.historical_success_rate * 100,
        "Signal": h.signal,
        "Risiko": h.risk_level,
    } for h in history]
    df = pd.DataFrame(rows).sort_values("Datum")
    fig = go.Figure(go.Scatter(
        x=df["Datum"], y=df["Opportunity Score"],
        mode="lines+markers", name="Opportunity Score",
        line=dict(color="#1f77b4", width=3),
    ))
    fig.update_layout(
        title="Opportunity Score im Zeitverlauf",
        xaxis_title="Datum", yaxis_title="Score", yaxis=dict(range=[0,100]),
        hovermode="x unified",
    )
    st.plotly_chart(fig, width="stretch")
    st.dataframe(df, width="stretch")
