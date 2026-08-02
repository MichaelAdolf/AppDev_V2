from stockmind.domain.indicators.indicator_result import (
    IndicatorResult
)


class IndicatorEngine:

    def __init__(
        self,
        indicators
    ):
        self._indicators = indicators

    def calculate(
        self,
        symbol: str,
        data
    ) -> IndicatorResult:

        values = {}

        for indicator in self._indicators:

            values[
                indicator.name
            ] = indicator.calculate(
                data
            )

        return IndicatorResult(
            symbol=symbol,
            values=values
        )
