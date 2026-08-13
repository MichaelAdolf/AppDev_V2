with tab3:

    history = (
        AnalysisHistoryRepository()
        .load_by_symbol(
            symbol
        )
    )

    if not history:

        st.warning(
            "Keine Historie vorhanden."
        )

    else:

        df = pd.DataFrame(
            [
                {
                    "Date": h.analysis_date,
                    "Opportunity Score":
                        h.opportunity_score,
                    "Confidence":
                        h.confidence * 100
                }
                for h in history
            ]
        )

        st.line_chart(
            df.set_index(
                "Date"
            )
        )

        st.dataframe(
            df,
            use_container_width=True
        )
