import streamlit as st

from stockmind.infrastructure.history.latest_analysis_repository import (
    LatestAnalysisRepository
)


def render(
    profile_name: str,
    symbol: str
):

    results = (
        LatestAnalysisRepository()
        .load_all(
            profile_name
        )
    )

    stock = None

    for item in results:

        if item.symbol == symbol:

            stock = item

            break

    if stock is None:

        st.warning(
            "Keine Daten gefunden."
        )

        return

    st.header(
        f"📈 {symbol}"
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Score",
            round(
                stock.opportunity_score,
                2
            )
        )

    with col2:

        st.metric(
            "Confidence",
            f"{stock.confidence:.1%}"
        )

    with col3:

        st.metric(
            "Historical",
            f"{stock.historical_success_rate:.1%}"
        )

    with col4:

        st.metric(
            "Signal",
            stock.signal
        )

    st.info(
        "Detailanalyse folgt in Phase 11.4"
    )
