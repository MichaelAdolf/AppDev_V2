import streamlit as st

from stockmind.infrastructure.history.latest_analysis_repository import (
    LatestAnalysisRepository
)


def render(
    profile_name: str
):

    st.subheader(
        "🔍 Aktie auswählen"
    )

    results = (
        LatestAnalysisRepository()
        .load_all(
            profile_name
        )
    )

    symbols = [
        item.symbol
        for item in results
    ]

    if not symbols:

        st.warning(
            "Keine Aktien vorhanden."
        )

        return

    selected = st.selectbox(
        "Aktie",
        symbols,
        index=0
    )

    st.session_state[
        "selected_symbol"
    ] = selected

    return selected
