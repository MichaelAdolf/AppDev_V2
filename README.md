from stockmind.domain.indicators.indicator_result import ( IndicatorResult )

from stockmind.domain.features.market_feature_snapshot import ( MarketFeatureSnapshot )

class FeatureEngine:

    def build(
        self,
        result: IndicatorResult
    ) -> MarketFeatureSnapshot:

        rsi = result.values["rsi_14"]

        sma = result.values["sma_20"]

        ema = result.values["ema_20"]

        macd = result.values["macd"]

        bollinger_position = result.values["bollinger_position"]

        adx = result.values.get("adx_14")

        return MarketFeatureSnapshot(
            symbol=result.symbol,

            rsi=rsi,

            sma_20=sma,

            ema_20=ema,

            macd=macd,

            bollinger_position=bollinger_position,

            is_oversold=rsi < 30,

            is_overbought=rsi > 70,

            ema_above_sma=ema > sma,
            
            macd_positive=macd > 0,

            near_lower_bollinger=bollinger_position < 0.25,

            adx_14=adx,

            adx_trend_strength=adx is not None and adx > 20
        )
