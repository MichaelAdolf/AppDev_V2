import pandas as pd
import streamlit as st

from stockmind.application.dashboard.use_cases.stock_detail_dashboard_use_case import (
    StockDetailDashboardUseCase
)

from stockmind.application.dashboard.use_cases.historical_setup_dashboard_use_case import (
    HistoricalSetupDashboardUseCase
)


def render(
    profile_name: str,
    symbol: str
):

    dashboard = (
        StockDetailDashboardUseCase()
        .load(
            profile_name=profile_name,
            symbol=symbol
        )
    )

    st.header(
        f"📈 {dashboard.symbol}"
    )

    #
    # KPI Leiste
    #

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Score",
            round(
                dashboard.score,
                2
            )
        )

    with col2:

        st.metric(
            "Confidence",
            f"{dashboard.confidence:.1%}"
        )

    with col3:

        st.metric(
            "Historical",
            f"{dashboard.historical_success_rate:.1%}"
        )

    with col4:

        st.metric(
            "Signal",
            dashboard.signal
        )

    st.divider()

    #
    # Tabs
    #

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "📊 Übersicht",
            "🧠 Analyse",
            "📜 Historie",
            "📈 Indikatoren"
        ]
    )

    #
    # Übersicht
    #

    with tab1:

        st.subheader(
            "Aktuelle Bewertung"
        )

        col1, col2 = st.columns(2)

        with col1:

            st.write(
                f"Signal: {dashboard.signal}"
            )

            st.write(
                f"Risk: {dashboard.risk_level}"
            )

        with col2:

            st.write(
                f"Historical Success: "
                f"{dashboard.historical_success_rate:.1%}"
            )

            st.write(
                f"Confidence: "
                f"{dashboard.confidence:.1%}"
            )

    #
    # Analyse
    #

    with tab2:

        st.subheader(
            "Zusammenfassung"
        )

        st.write(
            dashboard.summary
        )

        st.subheader(
            "✅ Stärken"
        )

        for item in dashboard.strengths:

            st.success(
                item
            )

        st.subheader(
            "⚠ Schwächen"
        )

        for item in dashboard.weaknesses:

            st.warning(
                item
            )

    #
    # Historie
    #

    with tab3:

        history = (
            dashboard.history
        )

        if history:

            history_df = pd.DataFrame(
                [
                    {
                        "Date":
                            h.analysis_date,

                        "Opportunity Score":
                            h.opportunity_score,

                        "Confidence":
                            h.confidence * 100
                    }
                    for h in history
                ]
            )

            st.line_chart(
                history_df.set_index(
                    "Date"
                )
            )

            st.dataframe(
                history_df,
                use_container_width=True
            )

        setup_dashboard = (
            HistoricalSetupDashboardUseCase()
            .load(
                symbol
            )
        )

        st.divider()

        st.subheader(
            "📜 Historische Setups"
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "Trefferquote",
                f"{setup_dashboard.success_rate:.1f}%"
            )

        with col2:

            st.metric(
                "Ø Tage",
                f"{setup_dashboard.average_days:.1f}"
            )

        with col3:

            st.metric(
                "Ø Max Gain",
                f"{setup_dashboard.average_gain:.1f}%"
            )

        with col4:

            st.metric(
                "Ø Drawdown",
                f"{setup_dashboard.average_drawdown:.1f}%"
            )

        setup_df = pd.DataFrame(
            [
                {
                    "Date":
                        s.setup_date,

                    "Success":
                        "✅"
                        if s.success
                        else "🔴",

                    "Entry":
                        round(
                            s.entry_price,
                            2
                        ),

                    "Days":
                        s.days_to_target,

                    "Gain %":
                        round(
                            s.max_gain_pct,
                            2
                        ),

                    "Drawdown %":
                        round(
                            s.max_drawdown_pct,
                            2
                        )
                }
                for s in setup_dashboard.setups
            ]
        )

        st.dataframe(
            setup_df,
            use_container_width=True
        )

    #
    # Indikatoren
    #

    with tab4:

        st.subheader(
            "Technische Indikatoren"
        )

        st.info(
            (
                "RSI, MACD, ADX, "
                "Bollinger und Stochastic "
                "werden im nächsten Schritt "
                "über Dashboard-UseCases "
                "angebunden."
            )
        )
