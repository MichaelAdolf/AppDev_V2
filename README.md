import pandas as pd

from stockmind.domain.indicators.base_indicator import (
    BaseIndicator
)


class SMAIndicator(
    BaseIndicator
):

    @property
    def name(self) -> str:
        return "sma_20"

    def calculate(
        self,
        data: pd.DataFrame
    ) -> float:

        return float(
            data["Close"]
            .rolling(20)
            .mean()
            .iloc[-1]
        )
