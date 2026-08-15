    with tab7:

        st.subheader(
            "🎯 Buy-Perioden Analyse"
        )

        buy_periods = (
            BuyPeriodDashboardUseCase()
            .load(
                symbol=dashboard.symbol,
                max_gap_days=10
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
