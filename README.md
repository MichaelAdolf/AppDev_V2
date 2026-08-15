adx_indicator = (
    ta.trend.ADXIndicator(
        high=data["High"],
        low=data["Low"],
        close=data["Close"],
        window=14
    )
)

data["ADX"] = (
    adx_indicator.adx()
)

data["+DI"] = (
    adx_indicator.adx_pos()
)

data["-DI"] = (
    adx_indicator.adx_neg()
)
``
