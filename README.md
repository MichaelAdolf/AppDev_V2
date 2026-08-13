with tab2:

    detail = (
        AnalysisDetailRepository()
        .load(
            symbol=symbol,
            profile_name=profile_name
        )
    )

    if detail is None:

        st.warning(
            "Keine Analyse vorhanden."
        )

    else:

        st.subheader(
            "Zusammenfassung"
        )

        st.write(
            detail.summary
        )

        st.subheader(
            "✅ Stärken"
        )

        for item in detail.strengths.split("|"):

            st.success(
                item
            )

        st.subheader(
            "⚠ Schwächen"
        )

        for item in detail.weaknesses.split("|"):

            st.warning(
                item
            )
