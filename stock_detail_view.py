import pandas as pd
import streamlit as st

from stockmind.application.dashboard.use_cases.stock_detail_dashboard_use_case import (
    StockDetailDashboardUseCase
)

from components.price_chart import(
    render as render_price_chart
)

from components.indicator_charts import (
    render_rsi_chart,
    render_macd_chart,
    render_adx_chart,
    render_stochastic_chart
)

from stockmind.application.dashboard.use_cases.profile_comparison_dashboard_use_case import (
    ProfileComparisonDashboardUseCase
)

from stockmind.application.dashboard.use_cases.fundamental_dashboard_use_case import (
    FundamentalDashboardUseCase
)

from stockmind.application.dashboard.use_cases.buy_period_dashboard_use_case import (
    BuyPeriodDashboardUseCase
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

    col1, col2, col3, col4, col5 = st.columns(5)

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
            "Risk",
            dashboard.risk_level
        )

    with col5:

        st.metric(
            "Signal",
            dashboard.signal
        )

    st.divider()

    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(
        [
            "📊 Übersicht",
            "🧠 Analyse",
            "📜 Historie",
            "📈 Indikatoren",
            "Profilvergleich",
            "🏦 Fundamentaldaten",
            "Buy-Perioden"
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
                f"**Signal:** {dashboard.signal}"
            )

            st.write(
                f"**Risk:** {dashboard.risk_level}"
            )

            st.write(
                f"**Opportunity Score:** {dashboard.score:.2f}"
            )

        with col2:

            st.write(
                f"**Confidence:** {dashboard.confidence:.1%}"
            )

            st.write(
                f"**Historical Success:** "
                f"{dashboard.historical_success_rate:.1%}"
            )

            st.write(
                f"**Historische Setups:** "
                f"{dashboard.setup_count}"
            )

    #
    # Analyse
    #

    with tab2:

        st.subheader(
            "Zusammenfassung"
        )

        if dashboard.summary:

            st.write(
                dashboard.summary
            )

        else:

            st.warning(
                "Keine Zusammenfassung vorhanden."
            )

        st.subheader(
            "✅ Stärken"
        )

        if dashboard.strengths:

            for item in dashboard.strengths:

                st.success(
                    item
                )

        else:

            st.info(
                "Keine Stärken gespeichert."
            )

        st.subheader(
            "⚠ Schwächen"
        )

        if dashboard.weaknesses:

            for item in dashboard.weaknesses:

                st.warning(
                    item
                )

        else:

            st.info(
                "Keine Schwächen gespeichert."
            )

    #
    # Historie
    #

    with tab3:

        st.subheader(
            "Opportunity Verlauf"
        )

        if dashboard.history:

            history_df = pd.DataFrame(
                [
                    {
                        "Date":
                            h.analysis_date,

                        "Opportunity Score":
                            h.opportunity_score,

                        "Confidence":
                            h.confidence * 100,

                        "Historical Success":
                            h.historical_success_rate * 100
                    }
                    for h in dashboard.history
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

        else:

            st.warning(
                "Keine Analysehistorie vorhanden."
            )

        st.divider()

        st.subheader(
            "📜 Historische Setups"
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "Trefferquote",
                f"{dashboard.setup_success_rate:.1f}%"
            )

        with col2:

            st.metric(
                "Ø Tage",
                f"{dashboard.average_setup_days:.1f}"
            )

        with col3:

            st.metric(
                "Ø Max Gain",
                f"{dashboard.average_setup_gain:.1f}%"
            )

        with col4:

            st.metric(
                "Ø Drawdown",
                f"{dashboard.average_setup_drawdown:.1f}%"
            )

        if dashboard.historical_setups:

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
                    for s in dashboard.historical_setups
                ]
            )

            st.dataframe(
                setup_df,
                use_container_width=True
            )

        else:

            st.info(
                "Keine historischen Setups vorhanden."
            )

    #
    # Indikatoren
    #

    with tab4:

        st.subheader(
            "Kurschart"
        )

        render_price_chart(
            dashboard.symbol
        )

        st.divider()

        render_rsi_chart(
            dashboard.symbol
        )

        st.divider()

        render_macd_chart(
            dashboard.symbol
        )

        st.divider()
        
        render_adx_chart(
            dashboard.symbol
        )

        st.divider()
        
        render_stochastic_chart(
            dashboard.symbol
        )

    with tab5:

        comparison = (
            ProfileComparisonDashboardUseCase()
            .load(
                dashboard.symbol
            )
        )

        rows = []

        for entry in comparison.entries:

            rows.append(
                {
                    "Profil":
                        entry.profile_name,

                    "Score":
                        round(
                            entry.score,
                            2
                        ),

                    "Confidence":
                        round(
                            entry.confidence * 100,
                            1
                        ),

                    "Signal":
                        entry.signal,

                    "Risk":
                        entry.risk_level
                }
            )

        st.dataframe(
            rows,
            use_container_width=True
        )

    with tab6:

        st.subheader(
            "🏦 Fundamentaldaten"
        )

        fundamentals = (
            FundamentalDashboardUseCase()
            .load(
                dashboard.symbol
            )
        )

        if fundamentals is None:
            st.warning(
                "Keine Fundamentaldaten vorhanden"
            )

        else:

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Fundamental Score",
                    f"{fundamentals.fundamental_score:.0f}/100"
                )

            with col2:
                if fundamentals.valuation == "ATTRACTIVE":
                    st.success(
                        "Attraktiv"
                    )

                elif fundamentals.valuation == "FAIR":
                    st.warning(
                        "Fair bewertet"
                    )

                else:
                    st.error(
                        "Teuer / Schwach"
                    )

            if fundamentals is None:

                st.warning(
                    "Keine Fundamentaldaten vorhanden."
                )

            else:

                st.write(
                    f"**Unternehmen:** "
                    f"{fundamentals.company_name or '-'}"
                )

                st.write(
                    f"**Sektor:** "
                    f"{fundamentals.sector or '-'}"
                )

                st.write(
                    f"**Industrie:** "
                    f"{fundamentals.industry or '-'}"
                )

                col1, col2, col3, col4 = st.columns(4)

                with col1:

                    st.metric(
                        "Market Cap",
                        (
                            f"{fundamentals.market_cap:,.0f}"
                            if fundamentals.market_cap
                            else "-"
                        )
                    )

                    st.metric(
                        "Trailing P/E",
                        (
                            f"{fundamentals.trailing_pe:.2f}"
                            if fundamentals.trailing_pe
                            else "-"
                        )
                    )

                with col2:

                    st.metric(
                        "Forward P/E",
                        (
                            f"{fundamentals.forward_pe:.2f}"
                            if fundamentals.forward_pe
                            else "-"
                        )
                    )

                    st.metric(
                        "Profit Margin",
                        (
                            f"{fundamentals.profit_margins:.1%}"
                            if fundamentals.profit_margins
                            else "-"
                        )
                    )

                with col3:

                    st.metric(
                        "Revenue Growth",
                        (
                            f"{fundamentals.revenue_growth:.1%}"
                            if fundamentals.revenue_growth
                            else "-"
                        )
                    )

                    st.metric(
                        "Target Mean Price",
                        (
                            f"{fundamentals.target_mean_price:.2f}"
                            if fundamentals.target_mean_price
                            else "-"
                        )
                    )

                with col4:
                    st.metric( 
                        "Current Price",
                        ( 
                            f"{fundamentals.current_price:.2f}"
                            if fundamentals.current_price 
                            else "-" 
                        )
                    )

                    st.metric(
                        "Target Upside",
                        (
                            f"{fundamentals.target_upside_pct:.1f}%"
                            if fundamentals.target_upside_pct is not None 
                            else "-"
                        ) 
                    )

                st.divider()
                st.subheader( "📣 Analysten Dashboard" )

                col1, col2, col3 = st.columns(3)

                with col1:

                    st.metric(
                        "Current Price",
                        (
                            f"{fundamentals.current_price:.2f}"
                            if fundamentals.current_price is not None
                            else "-"
                        )
                    )

                with col2:

                    st.metric(
                        "Target Mean",
                        (
                            f"{fundamentals.target_mean_price:.2f}"
                            if fundamentals.target_mean_price is not None
                            else "-"
                        )
                    )

                with col3:

                    st.metric(
                        "Upside Potential",
                        (
                            f"{fundamentals.target_upside_pct:.1f}%"
                            if fundamentals.target_upside_pct is not None
                            else "-"
                        )
                    )

                rating = (
                    fundamentals.recommendation_key or ""
                ).lower()

                if rating == "strong_buy":

                    st.success(
                        "🟢 STRONG BUY"
                    )

                elif rating == "buy":

                    st.success(
                        "🟢 BUY"
                    )

                elif rating == "hold":

                    st.warning(
                        "🟡 HOLD"
                    )

                elif rating == "sell":

                    st.error(
                        "🔴 SELL"
                    )

                else:

                    st.info(
                        f"Rating: {rating}"
                    )

    with tab7:

        st.subheader(
            "🎯 Buy-Perioden Analyse"
        )

        buy_periods = (
            BuyPeriodDashboardUseCase()
            .load(
                symbol=dashboard.symbol,
                max_gap_days=3
            )
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "Perioden",
                buy_periods.period_count
            )

        with col2:

            st.metric(
                "Trefferquote",
                f"{buy_periods.overall_success_rate:.1f}%"
            )

        with col3:

            st.metric(
                "Ø Tage",
                f"{buy_periods.average_days_to_target:.1f}"
            )

        with col4:

            st.metric(
                "Ø Max Gain",
                f"{buy_periods.average_max_gain_pct:.1f}%"
            )

        st.divider()

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "✅ Erfolgreich",
                buy_periods.successful_period_count
            )

        with col2:

            st.metric(
                "🔴 Fehlgeschlagen",
                buy_periods.failed_period_count
            )

        with col3:

            st.metric(
                "🟡 Gemischt",
                buy_periods.mixed_period_count
            )

        if buy_periods.periods:

            period_rows = []

            for period in buy_periods.periods:

                period_rows.append(
                    {
                        "Start":
                            period.start_date,

                        "Ende":
                            period.end_date,

                        "Setups":
                            period.setup_count,

                        "Erfolgreich":
                            period.successful_count,

                        "Fehlgeschlagen":
                            period.failed_count,

                        "Trefferquote %":
                            round(
                                period.success_rate,
                                1
                            ),

                        "Ø Tage":
                            round(
                                period.average_days_to_target,
                                1
                            ),

                        "Max Gain %":
                            round(
                                period.max_gain_pct,
                                1
                            ),

                        "Max Drawdown %":
                            round(
                                period.max_drawdown_pct,
                                1
                            ),

                        "Status":
                            period.status
                    }
                )

            period_df = pd.DataFrame(
                period_rows
            )

            st.dataframe(
                period_df,
                use_container_width=True
            )

        else:

            st.info(
                "Keine Buy-Perioden vorhanden."
            )