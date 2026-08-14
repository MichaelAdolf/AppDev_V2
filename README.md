import pandas as pd
import streamlit as st

from stockmind.application.dashboard.use_cases.watchlist_dashboard_use_case import (
    WatchlistDashboardUseCase
)


def render(
    profile_name: str
):

    dashboard = (
        WatchlistDashboardUseCase()
        .load(
            profile_name
        )
    )

    results = (
        dashboard.stocks
    )

    #
    # Info Cards
    #

    col1, col2, col3, col4, col5 = (
        st.columns(5)
    )

    with col1:

        st.metric(
            "Aktien",
            dashboard.stock_count
        )

    with col2:

        st.metric(
            "BUY",
            dashboard.buy_count
        )

    with col3:

        st.metric(
            "HOLD",
            dashboard.hold_count
        )

    with col4:

        st.metric(
            "SELL",
            dashboard.sell_count
        )

    with col5:

        st.metric(
            "Hot Opps",
            dashboard.hot_opportunities
        )

    st.divider()

    #
    # Alerts
    #

    st.subheader(
        "🔥 Alerts"
    )

    #
    # Platzhalter
    # Kommt später aus
    # AlertsDashboardUseCase
    #

    st.info(
        "Alerts Dashboard folgt im nächsten Schritt."
    )

    st.divider()

    #
    # Watchlist Tabelle
    #

    rows = []

    for item in results:

        rows.append(
            {
                "Symbol":
                    item.symbol,

                "Score":
                    round(
                        item.opportunity_score,
                        2
                    ),

                "Signal":
                    item.signal,

                "Confidence":
                    round(
                        item.confidence
                        * 100,
                        1
                    ),

                "Historical":
                    round(
                        item.historical_success_rate
                        * 100,
                        1
                    ),

                "Risk":
                    item.risk_level
            }
        )

    df = pd.DataFrame(
        rows
    )

    st.subheader(
        "📋 Watchlist"
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    st.divider()

    #
    # Aktienauswahl
    #

    st.subheader(
        "🔍 Detailansicht öffnen"
    )

    for item in results:

        if st.button(
            item.symbol,
            key=f"btn_{item.symbol}"
        ):

            st.session_state[
                "selected_symbol"
            ] = item.symbol
