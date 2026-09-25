import pandas as pd
import streamlit as st
from stockmind.application.dashboard.use_cases.buy_period_dashboard_use_case import BuyPeriodDashboardUseCase

LABELS={
 "TARGET_HIT":"Ziel erreicht", "BELOW_TARGET":"Positiv unter Ziel",
 "FLAT":"Seitwärts", "NEGATIVE":"Negativ",
 "INCOMPLETE_WINDOW":"Beobachtungszeitraum offen",
}

def render(symbol: str, profile_name: str, analysis_period: str="5y", max_gap_days: int=3):
    result=BuyPeriodDashboardUseCase().load(
        symbol=symbol, profile_name=profile_name,
        analysis_period=analysis_period, max_gap_days=max_gap_days,
    )
    stats=result.statistics
    st.info(
        "Eine BUY-Periode fasst profilabhängige BUY-Signaltage zusammen. "
        "Zwischen zwei BUY-Signalen dürfen maximal drei Kalendertage liegen. "
        "Die historische Bewertung beginnt am ersten BUY-Signaltag und "
        "betrachtet die folgenden 60 Kalendertage."
    )
    if result.active_period:
        p=result.active_period
        st.success(f"Aktive BUY-Periode seit {p.start_date}: {p.calendar_duration_days} Kalendertage, {p.buy_signal_count} BUY-Signaltage")
    else:
        st.info("Aktuell besteht für dieses Profil keine aktive BUY-Periode.")
    c1,c2,c3,c4,c5=st.columns(5)
    c1.metric("Perioden",result.period_count)
    c2.metric("Vollständig",stats.complete_period_count)
    c3.metric("Beobachtungszeitraum offen",stats.incomplete_period_count)
    c4.metric("Ziel erreicht",f"{stats.target_hit_rate:.1%}",help="Anteil vollständiger Perioden mit mindestens +8 % innerhalb 60 Kalendertagen.")
    c5.metric("Ø Tage bis Ziel",f"{stats.average_days_to_target:.1f}")
    c1,c2,c3,c4=st.columns(4)
    c1.metric("Positiv unter Ziel",f"{stats.below_target_rate:.1%}")
    c2.metric("Seitwärts",f"{stats.flat_rate:.1%}")
    c3.metric("Negativ",f"{stats.negative_rate:.1%}")
    c4.metric("Ø Periodendauer",f"{stats.average_calendar_duration_days:.1f} Tage")
    if not result.periods:
        st.info("Keine BUY-Perioden für diese Auswahl vorhanden."); return
    rows=[]
    for p in result.periods:
        rows.append({
            "Start":p.start_date,"Ende":p.end_date,
            "Kalendertage":p.calendar_duration_days,
            "BUY-Signaltage":p.buy_signal_count,
            "Tage zwischen BUY-Signalen":p.gap_days_total,
            "Größte Unterbrechung":p.largest_gap_days,
            "Einstiegskurs":round(p.entry_price,2),
            "Ergebnis":LABELS.get(p.outcome,p.outcome),
            "Tage bis Ziel":p.days_to_target,
            "Rendite nach 60 Tagen %":round(p.window_end_return_pct,2) if p.window_end_return_pct is not None else None,
            "Maximaler Kursgewinn %":round(p.max_gain_pct,2) if p.max_gain_pct is not None else None,
            "Maximaler zwischenzeitlicher Rückgang %":round(p.max_drawdown_pct,2) if p.max_drawdown_pct is not None else None,
        })
    st.dataframe(pd.DataFrame(rows),width="stretch")
