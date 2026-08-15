st.divider()

st.subheader(
    "📣 Analysten Dashboard"
)

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Current Price",
        (
            f"{fundamentals.current_price:.2f}"
            if fundamentals.current_price is not None
            else "-"
        )
    )

with col2:

    st.metric(
        "Target Mean",
        (
            f"{fundamentals.target_mean_price:.2f}"
            if fundamentals.target_mean_price is not None
            else "-"
        )
    )

with col3:

    st.metric(
        "Upside Potential",
        (
            f"{fundamentals.target_upside_pct:.1f}%"
            if fundamentals.target_upside_pct is not None
            else "-"
        )
    )
