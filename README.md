import pandas as pd

from stockmind.domain.indicators.base_indicator import (
    BaseIndicator
)


class ADXIndicator(
    BaseIndicator
):

    @property
    def name(self) -> str:
        return "adx_14"

    def calculate(
        self,
        data: pd.DataFrame
    ) -> float:

        high = data["High"]
        low = data["Low"]
        close = data["Close"]

        plus_dm = high.diff()
        minus_dm = low.diff() * -1

        plus_dm = plus_dm.where(
            (plus_dm > minus_dm) & (plus_dm > 0),
            0.0
        )

        minus_dm = minus_dm.where(
            (minus_dm > plus_dm) & (minus_dm > 0),
            0.0
        )

        previous_close = close.shift(1)

        true_range = pd.concat(
            [
                high - low,
                (high - previous_close).abs(),
                (low - previous_close).abs(),
            ],
            axis=1
        ).max(axis=1)

        atr = true_range.rolling(
            window=14
        ).mean()

        plus_di = 100 * (
            plus_dm.rolling(
                window=14
            ).mean()
            / atr
        )

        minus_di = 100 * (
            minus_dm.rolling(
                window=14
            ).mean()
            / atr
        )

        dx = 100 * (
            (plus_di - minus_di).abs()
            / (plus_di + minus_di)
        )

        adx = dx.rolling(
            window=14
        ).mean()

        value = adx.iloc[-1]

        if pd.isna(value):
            return 0.0

        return float(value)
