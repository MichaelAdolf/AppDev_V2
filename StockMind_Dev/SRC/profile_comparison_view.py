import pandas as pd
import streamlit as st
from stockmind.application.dashboard.use_cases.profile_comparison_dashboard_use_case import ProfileComparisonDashboardUseCase


def render(symbol: str, analysis_period: str = "5y", max_gap_days: int = 3):
    comparison = ProfileComparisonDashboardUseCase().load(
        symbol=symbol, analysis_period=analysis_period,
        max_gap_days=max_gap_days,
    )
    if not comparison.entries:
        st.info("Keine Daten für den Profilvergleich vorhanden.")
        return
    rows=[]
    for e in comparison.entries:
        rows.append({
            "Profil": e.profile_name,
            "Signal": e.signal,
            "BUY heute": "BUY" if e.current_buy_signal is True else "Kein BUY" if e.current_buy_signal is False else "Keine Daten",
            "Aktive Periode seit": e.active_period_start or "-",
            "Aktive Dauer": e.active_period_duration_days or 0,
            "BUY-Perioden Trefferquote %": round(e.target_hit_rate*100,1),
            "Score": round(e.score,2),
            "Confidence %": round(e.confidence*100,1),
            "Risiko": e.risk_level,
            "Perioden": e.period_count,
            "Vollständig": e.complete_period_count,
            "Offen": e.incomplete_period_count,
            "Positiv unter Ziel %": round(e.below_target_rate*100,1),
            "Seitwärts %": round(e.flat_rate*100,1),
            "Negativ %": round(e.negative_rate*100,1),
        })
    st.dataframe(pd.DataFrame(rows), width="stretch")
