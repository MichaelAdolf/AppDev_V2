from stockmind.domain.indicators.indicator_result import ( IndicatorResult )

from stockmind.domain.features.market_feature_snapshot import ( MarketFeatureSnapshot )

from stockmind.domain.profiles.trading_profile import ( TradingProfile )

class FeatureEngine:

    def build(
        self,
        result: IndicatorResult,
        profile: TradingProfile | None = None
    ) -> MarketFeatureSnapshot:

        if profile is None:
            profile = TradingProfile.balanced()

        rsi = result.values["rsi_14"]

        sma = result.values["sma_20"]

        ema = result.values["ema_20"]

        macd = result.values["macd"]

        bollinger_position = result.values["bollinger_position"]

        adx = result.values.get("adx_14")

        stoch_k = result.values.get("stoch_k_14")

        return MarketFeatureSnapshot(
            symbol=result.symbol,

            rsi=rsi,

            sma_20=sma,

            ema_20=ema,

            macd=macd,

            bollinger_position=bollinger_position,

            is_oversold=(rsi <= profile.rsi_oversold_threshold),

            is_overbought=rsi >= profile.rsi_overbought_threshold,

            ema_above_sma=ema > sma,
            
            macd_positive=macd > 0,

            near_lower_bollinger=bollinger_position <= profile.bollinger_lower_threshold,

            adx_14=adx,

            adx_trend_strength=adx is not None and adx >= profile.adx_trend_strength_threshold,

            stoch_k_14=stoch_k,

            stoch_oversold=(
                stoch_k is not None
                and stoch_k
                <= profile.stochastic_oversold_threshold
            )
        )
