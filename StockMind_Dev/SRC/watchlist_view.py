import pandas as pd
import streamlit as st
from stockmind.application.dashboard.use_cases.watchlist_dashboard_use_case import WatchlistDashboardUseCase
from stockmind.application.dashboard.use_cases.alerts_dashboard_use_case import AlertsDashboardUseCase


def render_alert(alert):
    message = (
        f"**{alert.title}: {alert.symbol}**  "
        f"{alert.message}  "
        f"Profil: `{alert.profile_name}` | Auslöser: {alert.reason}"
    )
    renderer = {
        "success": st.success,
        "warning": st.warning,
        "error": st.error,
    }.get(alert.severity, st.info)
    renderer(message)


def render(profile_name: str):
    dashboard = WatchlistDashboardUseCase().load(profile_name)
    results = sorted(
        dashboard.stocks,
        key=lambda item: item.opportunity_score,
        reverse=True,
    )
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Aktien", dashboard.stock_count)
    col2.metric("BUY", dashboard.buy_count)
    col3.metric("HOLD", dashboard.hold_count)
    col4.metric("SELL", dashboard.sell_count)
    col5.metric("Hot Opportunities", dashboard.hot_opportunities)

    st.divider()
    st.subheader("📋 Watchlist")
    rows = [{
        "Symbol": item.symbol,
        "Unternehmen": item.company_name,
        "Opportunity Score": round(item.opportunity_score, 2),
        "Signal": item.signal,
        "Confidence %": round(item.confidence * 100, 1),
        "Hist. Evidenz %": round(item.historical_success_rate * 100, 1),
        "Risiko": item.risk_level,
    } for item in results]
    st.dataframe(pd.DataFrame(rows), width="stretch")

    st.divider()
    st.subheader("🔥 Alerts")
    st.caption(
        "Alerts heben auffällige Kennzahlen im gewählten Profil hervor. "
        "Sie sind Beobachtungshinweise und keine eigenständige Kaufempfehlung."
    )
    alerts = AlertsDashboardUseCase().load(profile_name)
    if alerts:
        for alert in alerts[:10]:
            render_alert(alert)
    else:
        st.success("Keine besonderen Alerts vorhanden.")
