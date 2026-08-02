import pandas as pd

from stockmind.domain.indicators.base_indicator import (
    BaseIndicator
)


class MACDIndicator(
    BaseIndicator
):

    @property
    def name(self) -> str:
        return "macd"

    def calculate(
        self,
        data: pd.DataFrame
    ) -> float:

        ema12 = data["Close"].ewm(
            span=12
        ).mean()

        ema26 = data["Close"].ewm(
            span=26
        ).mean()

        macd = ema12 - ema26

        return float(
            macd.iloc[-1]
        )
