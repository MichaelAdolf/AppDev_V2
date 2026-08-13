st.subheader(
    "🔍 Detailansicht öffnen"
)

for item in results:

    col1, col2 = st.columns(
        [1, 4]
    )

    with col1:

        if st.button(
            f"{item.symbol}",
            key=f"btn_{item.symbol}"
        ):

            st.session_state[
                "selected_symbol"
            ] = item.symbol
