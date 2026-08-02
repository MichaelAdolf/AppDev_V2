from stockmind.domain.indicators.indicator_result import (
    IndicatorResult
)

from stockmind.domain.value_objects.market_feature_snapshot import (
    MarketFeatureSnapshot
)


class FeatureEngine:

    def build(
        self,
        result: IndicatorResult
    ) -> MarketFeatureSnapshot:

        rsi = result.values["rsi_14"]

        sma = result.values["sma_20"]

        ema = result.values["ema_20"]

        return MarketFeatureSnapshot(
            symbol=result.symbol,

            rsi=rsi,

            sma_20=sma,

            ema_20=ema,

            is_oversold=rsi < 30,

            is_overbought=rsi > 70,

            ema_above_sma=ema > sma
        )
