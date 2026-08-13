import streamlit as st

from stockmind.infrastructure.history.analysis_history_repository import (
    AnalysisHistoryRepository
)


def render(
    symbol: str
):

    st.header(
        f"📈 {symbol}"
    )

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

        return

    latest = history[-1]

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Opportunity Score",
            round(
                latest.opportunity_score,
                2
            )
        )

    with col2:

        st.metric(
            "Confidence",
            f"{latest.confidence:.1%}"
        )

    with col3:

        st.metric(
            "Signal",
            latest.signal
        )

    st.divider()

    tab1, tab2 = st.tabs(
        [
            "📊 Übersicht",
            "📜 Historie"
        ]
    )

    with tab1:

        st.write(
            "Detailanalyse folgt im nächsten Schritt."
        )

    with tab2:

        st.write(history)
