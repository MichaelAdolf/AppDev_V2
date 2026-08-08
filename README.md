import pandas as pd

from stockmind.domain.indicators.base_indicator import (
    BaseIndicator
)


class StochasticIndicator(
    BaseIndicator
):

    @property
    def name(self) -> str:
        return "stoch_k_14"

    def calculate(
        self,
        data: pd.DataFrame
    ) -> float:

        low_14 = (
            data["Low"]
            .rolling(
                window=14
            )
            .min()
        )

        high_14 = (
            data["High"]
            .rolling(
                window=14
            )
            .max()
        )

        stoch_k = 100 * (
            (
                data["Close"]
                - low_14
            )
            /
            (
                high_14
                - low_14
            )
        )

        value = stoch_k.iloc[-1]

        if pd.isna(
            value
        ):

            return 0.0

        return float(
            value
        )
