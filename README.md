if rating == "strong_buy":

    st.success(
        "🟢 STRONG BUY"
    )

elif rating == "buy":

    st.success(
        "🟢 BUY"
    )

elif rating == "hold":

    st.warning(
        "🟡 HOLD"
    )

elif rating == "sell":

    st.error(
        "🔴 SELL"
    )

else:

    st.info(
        f"Rating: {rating}"
    )
