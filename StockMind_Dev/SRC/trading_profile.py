from dataclasses import dataclass

from stockmind.domain.scoring.opportunity_scoring_profile import OpportunityScoreProfile

@dataclass(frozen=True) 
class TradingProfile:

    name: str

    rsi_oversold_threshold: float

    rsi_overbought_threshold: float

    bollinger_lower_threshold: float

    adx_trend_strength_threshold: float

    stochastic_oversold_threshold: float

    description: str = ""

    opportunity_profile: OpportunityScoreProfile

    opportunity_profile=OpportunityScoreProfile(
            name="conservative",
            quality_weight=0.25,
            confidence_weight=0.35,
            historical_weight=0.35,
            risk_weight=0.15
        )

    opportunity_profile=OpportunityScoreProfile(
            name="balanced",
            quality_weight=0.30,
            confidence_weight=0.40,
            historical_weight=0.20,
            risk_weight=0.10
        )

    opportunity_profile=OpportunityScoreProfile(
                name="aggressive",
                quality_weight=0.35,
                confidence_weight=0.45,
                historical_weight=0.15,
                risk_weight=0.05
            )

    @staticmethod
    def conservative() -> "TradingProfile":

        return TradingProfile(
            name="conservative",
            rsi_oversold_threshold=25,
            rsi_overbought_threshold=70,
            bollinger_lower_threshold=0.15,
            adx_trend_strength_threshold=25,
            stochastic_oversold_threshold=15,
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
            stochastic_oversold_threshold=20,
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
            stochastic_oversold_threshold=25,
            description=(
                "Früheres Profil mit mehr Signalen "
                "und höherer Fehlertoleranz."
            )
        )