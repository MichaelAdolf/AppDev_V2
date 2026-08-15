st.metric(
    "Current Price",
    (
        f"{fundamentals.current_price:.2f}"
        if fundamentals.current_price
        else "-"
    )
)

st.metric(
    "Target Upside",
    (
        f"{fundamentals.target_upside_pct:.1f}%"
        if fundamentals.target_upside_pct is not None
        else "-"
    )
)
