import pandas as pd
import streamlit as st

from stockmind.application.dashboard.use_cases.daily_intelligence_dashboard_use_case import (
    DailyIntelligenceDashboardUseCase,
)


def _format_change(value):
    return "-" if value is None else f"{value:+.1f}"


def _format_signal_change(item):
    if item.previous_signal is None:
        return item.current_signal
    if item.signal_changed:
        return f"{item.previous_signal} → {item.current_signal}"
    return item.current_signal


def _render_opportunity_card(item):
    with st.container(border=True):
        st.subheader(f"{item.company_name} ({item.symbol})")
        st.caption(
            f"{item.relevance_status} | Profil: {item.profile_name}"
        )
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric(
            "Opportunity Score",
            f"{item.current_score:.1f}",
            delta=_format_change(item.score_change),
        )
        col2.metric(
            "Signal",
            item.current_signal,
            delta=(
                f"von {item.previous_signal}"
                if item.signal_changed else None
            ),
        )
        col3.metric("Confidence", f"{item.current_confidence:.1%}")
        col4.metric(
            "Hist. Trefferquote",
            f"{item.target_hit_rate:.1%}",
            help=(
                f"{item.complete_period_count} vollständige BUY-Perioden | "
                f"Sample Quality: {item.sample_quality}"
            ),
        )
        col5.metric("Profil-Konsens", item.profile_consensus)
        if item.active_period_start:
            st.write(
                f"**Aktive BUY-Periode:** seit {item.active_period_start}, "
                f"{item.active_period_duration_days} Kalendertage"
            )
        st.caption(
            f"Stichprobe: {item.complete_period_count} vollständige Perioden | "
            f"Sample Quality: {item.sample_quality} | Risiko: {item.current_risk}"
        )


def render(profile_name: str):
    dashboard = DailyIntelligenceDashboardUseCase().load(profile_name)
    st.subheader("Daily Intelligence")
    st.caption(
        "Relevante Veränderungen über alle aktiven Watchlist-Aktien. "
        "Score-Veränderungen beziehen sich auf den vorherigen verfügbaren Handelstag."
    )
    if dashboard.latest_trading_date:
        st.caption(
            f"Aktueller Replay-Tag: {dashboard.latest_trading_date} | "
            f"Vergleichstag: {dashboard.previous_trading_date or '-'}"
        )

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Aktien", dashboard.stock_count)
    col2.metric("Heute relevant", dashboard.relevant_count)
    col3.metric("Neue BUY-Perioden", dashboard.new_buy_period_count)
    col4.metric("Signaländerungen", dashboard.signal_change_count)
    col5.metric("3/3 BUY", dashboard.consensus_count)

    relevant_items = [
        item for item in dashboard.items
        if item.relevance_priority > 0
    ]
    st.divider()
    st.subheader("Heute relevant")
    if relevant_items:
        for item in relevant_items[:5]:
            _render_opportunity_card(item)
    else:
        st.info("Keine besonderen Veränderungen im vorhandenen Datenstand.")

    st.divider()
    left, right = st.columns(2)
    with left:
        st.subheader("Neue BUY-Perioden")
        new_periods = [item for item in dashboard.items if item.new_buy_period]
        if new_periods:
            st.dataframe(pd.DataFrame([{
                "Symbol": item.symbol,
                "Unternehmen": item.company_name,
                "Profil": item.profile_name,
                "Start": item.active_period_start,
                "Score": round(item.current_score, 1),
                "Trefferquote %": round(item.target_hit_rate * 100, 1),
                "Stichprobe": item.complete_period_count,
            } for item in new_periods]), width="stretch", hide_index=True)
        else:
            st.info("Keine neue BUY-Periode am aktuellen Replay-Tag.")

    with right:
        st.subheader("Signaländerungen")
        signal_changes = [item for item in dashboard.items if item.signal_changed]
        if signal_changes:
            st.dataframe(pd.DataFrame([{
                "Symbol": item.symbol,
                "Unternehmen": item.company_name,
                "Änderung": _format_signal_change(item),
                "Score": round(item.current_score, 1),
                "Δ Score": _format_change(item.score_change),
            } for item in signal_changes]), width="stretch", hide_index=True)
        else:
            st.info("Keine Signaländerungen zum vorherigen Handelstag.")

    st.divider()
    st.subheader("Opportunity Score Movers")
    movers = sorted(
        [item for item in dashboard.items if item.score_change is not None],
        key=lambda item: item.score_change,
        reverse=True,
    )
    if movers:
        st.dataframe(pd.DataFrame([{
            "Symbol": item.symbol,
            "Unternehmen": item.company_name,
            "Score vorher": round(item.previous_score, 1),
            "Score aktuell": round(item.current_score, 1),
            "Δ Score": round(item.score_change, 1),
            "Signal": _format_signal_change(item),
            "Confidence %": round(item.current_confidence * 100, 1),
            "Profil-Konsens": item.profile_consensus,
        } for item in movers]), width="stretch", hide_index=True)
    else:
        st.info("Noch keine zwei Replay-Handelstage für einen Vergleich vorhanden.")

    st.divider()
    st.subheader("Profil-Konsens")
    st.dataframe(pd.DataFrame([{
        "Symbol": item.symbol,
        "Unternehmen": item.company_name,
        "Bestätigung": item.profile_consensus,
        "Aktives Profil": item.profile_name,
        "Signal": item.current_signal,
        "Trefferquote %": round(item.target_hit_rate * 100, 1),
        "Vollständige Perioden": item.complete_period_count,
        "Sample Quality": item.sample_quality,
    } for item in dashboard.items]), width="stretch", hide_index=True)
