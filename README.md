import pandas as pd
import streamlit as st

from stockmind.infrastructure.history.latest_analysis_repository import (
    LatestAnalysisRepository
)


def render(
    profile_name: str
):

    results = (
        LatestAnalysisRepository()
        .load_all(
            profile_name
        )
    )

    rows = []

    for item in results:

        rows.append(
            {
                "Symbol": item.symbol,
                "Score": round(
                    item.opportunity_score,
                    2
                ),
                "Signal": item.signal,
                "Confidence": round(
                    item.confidence * 100,
                    1
                ),
                "Historical": round(
                    item.historical_success_rate * 100,
                    1
                ),
                "Risk": item.risk_level
            }
        )

    df = pd.DataFrame(rows)

    st.dataframe(
        df,
        use_container_width=True
    )
