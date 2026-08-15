stoch = (
    ta.momentum.StochasticOscillator(
        high=data["High"],
        low=data["Low"],
        close=data["Close"],
        window=14,
        smooth_window=3
    )
)

data["STOCH_K"] = (
    stoch.stoch()
)

data["STOCH_D"] = (
    stoch.stoch_signal()
)
