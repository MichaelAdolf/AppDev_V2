import pandas as pd

from stockmind.domain.indicators.base_indicator import (
    BaseIndicator
)


class EMAIndicator(
    BaseIndicator
):

    @property
    def name(self) -> str:
        return "ema_20"

    def calculate(
        self,
        data: pd.DataFrame
    ) -> float:

        return float(
            data["Close"]
            .ewm(span=20)
            .mean()
            .iloc[-1]
        )
