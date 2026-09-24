import pandas as pd
import streamlit as st

from stockmind.application.dashboard.use_cases.profile_comparison_dashboard_use_case import (
    ProfileComparisonDashboardUseCase,
)


def render(
    symbol: str,
    analysis_period: str = "5y",
    max_gap_days: int = 3,
):
    comparison = ProfileComparisonDashboardUseCase().load(
        symbol=symbol,
        analysis_period=analysis_period,
        max_gap_days=max_gap_days,
    )
    if not comparison.entries:
        st.info("Keine Daten für den Profilvergleich vorhanden.")
        return

    rows = []
    for entry in comparison.entries:
        rows.append({
            "Profil": entry.profile_name,
            "Signal": entry.signal,
            "BUY heute": (
                "BUY" if entry.current_buy_signal is True
                else "Kein BUY" if entry.current_buy_signal is False
                else "Keine Daten"
            ),
            "Aktive Periode seit": entry.active_period_start or "-",
            "Aktive Dauer": entry.active_period_duration_days or 0,
            "Score": round(entry.score, 2),
            "Confidence %": round(entry.confidence * 100, 1),
            "Risk": entry.risk_level,
            "Perioden": entry.period_count,
            "Vollständig": entry.complete_period_count,
            "Offen": entry.incomplete_period_count,
            "Target Hit %": round(entry.target_hit_rate * 100, 1),
            "Unter Ziel %": round(entry.below_target_rate * 100, 1),
            "Flat %": round(entry.flat_rate * 100, 1),
            "Negativ %": round(entry.negative_rate * 100, 1),
        })
    st.dataframe(pd.DataFrame(rows), use_container_width=True)
