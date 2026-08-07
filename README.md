from dataclasses import dataclass


@dataclass(frozen=True)
class TradingProfile:

    name: str

    rsi_oversold_threshold: float

    rsi_overbought_threshold: float

    bollinger_lower_threshold: float

    adx_trend_strength_threshold: float

    description: str = ""

    @staticmethod
    def conservative() -> "TradingProfile":

        return TradingProfile(
            name="conservative",
            rsi_oversold_threshold=25,
            rsi_overbought_threshold=70,
            bollinger_lower_threshold=0.15,
            adx_trend_strength_threshold=25,
            description=(
                "Strengeres Profil mit weniger Signalen "
                "und höherer technischer Qualität."
            )
        )

    @staticmethod
    def balanced() -> "TradingProfile":

        return TradingProfile(
            name="balanced",
            rsi_oversold_threshold=30,
            rsi_overbought_threshold=70,
            bollinger_lower_threshold=0.25,
            adx_trend_strength_threshold=20,
            description=(
                "Ausgewogenes Profil zwischen Signalqualität "
                "und Signalanzahl."
            )
        )

    @staticmethod
    def aggressive() -> "TradingProfile":

        return TradingProfile(
            name="aggressive",
            rsi_oversold_threshold=35,
            rsi_overbought_threshold=75,
            bollinger_lower_threshold=0.35,
            adx_trend_strength_threshold=15,
            description=(
                "Früheres Profil mit mehr Signalen "
                "und höherer Fehlertoleranz."
            )
        )
