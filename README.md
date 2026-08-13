import streamlit as st
import pandas as pd

from stockmind.application.use_cases.run_analysis_use_case import (
    RunAnalysisUseCase
)

from stockmind.application.use_cases.manage_watchlist_use_case import (
    ManageWatchlistUseCase
)

st.title("🏆 Opportunity Ranking")

watchlist = (
    ManageWatchlistUseCase()
    .load("tech_stocks")
)

symbols = [
    entry.symbol
    for entry in watchlist.entries
]

result = (
    RunAnalysisUseCase()
    .execute(
        symbols=symbols,
        profile_name="balanced"
    )
)

rows = []

for stock in result.stock_results:

    rows.append(
        {
            "Symbol": stock.symbol,
            "Score": round(
                stock.opportunity_score,
                2
            ),
            "Signal": stock.signal.signal.value,
            "Confidence": round(
                stock.confidence * 100,
                1
            ),
            "Historical Success": round(
                stock.historical_success_rate
                * 100,
                1
            ),
            "Risk": stock.risk_level
        }
    )

df = pd.DataFrame(rows)

st.dataframe(
    df,
    use_container_width=True
)
