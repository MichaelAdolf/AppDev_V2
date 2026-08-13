import pandas as pd
import streamlit as st

from stockmind.infrastructure.history.latest_analysis_repository import (
    LatestAnalysisRepository
)


def render(
    profile_name: str
):

    results = (
        LatestAnalysisRepository()
        .load_all(
            profile_name
        )
    )

    #
    # Info Cards
    #

    stock_count = len(
        results
    )

    buy_count = len(
        [
            item
            for item in results
            if item.signal == "BUY"
        ]
    )

    hold_count = len(
        [
            item
            for item in results
            if item.signal == "HOLD"
        ]
    )

    sell_count = len(
        [
            item
            for item in results
            if item.signal == "SELL"
        ]
    )

    hot_opportunities = len(
        [
            item
            for item in results
            if item.opportunity_score >= 80
        ]
    )

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:

        st.metric(
            "Aktien",
            stock_count
        )

    with col2:

        st.metric(
            "BUY",
            buy_count
        )

    with col3:

        st.metric(
            "HOLD",
            hold_count
        )

    with col4:

        st.metric(
            "SELL",
            sell_count
        )

    with col5:

        st.metric(
            "Hot Opps",
            hot_opportunities
        )

    st.divider()

    #
    # Alerts
    #

    st.subheader(
        "🔥 Alerts"
    )

    alerts = []

    for item in results:

        if item.opportunity_score >= 85:

            alerts.append(
                f"🔥 {item.symbol} Opportunity Score {item.opportunity_score:.1f}"
            )

        if item.confidence >= 0.75:

            alerts.append(
                f"🟢 {item.symbol} Confidence {item.confidence:.1%}"
            )

    if alerts:

        for alert in alerts[:10]:

            st.info(
                alert
            )

    else:

        st.success(
            "Keine besonderen Alerts vorhanden."
        )

    st.divider()

    #
    # Tabelle
    #

    rows = []

    for item in results:

        rows.append(
            {
                "Symbol": item.symbol,
                "Score": round(
                    item.opportunity_score,
                    2
                ),
                "Signal": item.signal,
                "Confidence": round(
                    item.confidence * 100,
                    1
                ),
                "Historical": round(
                    item.historical_success_rate * 100,
                    1
                ),
                "Risk": item.risk_level
            }
        )

    df = pd.DataFrame(rows)

    st.subheader(
        "📋 Watchlist"
    )

    st.dataframe(
        df,
        use_container_width=True
    )
