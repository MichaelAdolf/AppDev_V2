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

        col1, col2, col3 = st.columns(3)

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

        st.divider()

        st.subheader(
            "📣 Analysten / Empfehlung"
        )

        st.write(
            f"**Recommendation:** "
            f"{fundamentals.recommendation_key or '-'}"
        )
