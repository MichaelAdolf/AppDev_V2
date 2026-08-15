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
