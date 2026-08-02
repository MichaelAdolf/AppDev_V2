import pandas as pd

from stockmind.domain.indicators.base_indicator import (
    BaseIndicator
)


class BollingerIndicator(
    BaseIndicator
):

    @property
    def name(self) -> str:
        return "bollinger_position"

    def calculate(
        self,
        data: pd.DataFrame
    ) -> float:

        sma = (
            data["Close"]
            .rolling(20)
            .mean()
        )

        std = (
            data["Close"]
            .rolling(20)
            .std()
        )

        upper = sma + (std * 2)

        lower = sma - (std * 2)

        close = data["Close"].iloc[-1]

        position = (
            (close - lower.iloc[-1])
            /
            (upper.iloc[-1] - lower.iloc[-1])
        )

        return float(position)
