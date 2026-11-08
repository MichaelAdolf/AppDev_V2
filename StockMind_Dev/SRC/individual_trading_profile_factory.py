from stockmind.domain.profiles.trading_profile import TradingProfile
from stockmind.domain.scoring.opportunity_scoring_profile import OpportunityScoreProfile
from stockmind.infrastructure.strategy.fitted_profile_repository import FittedProfileRepository

class IndividualTradingProfileFactory:
    SCORING = OpportunityScoreProfile(
        name="individual",
        quality_weight=0.30,
        confidence_weight=0.40,
        historical_weight=0.20,
        risk_weight=0.10,
    )
    def __init__(self,database_path=None):self._repo=FittedProfileRepository(database_path)
    def create(self,symbol):
        fitted=self._repo.load_active(symbol)
        if fitted is None:raise ValueError(f"Kein aktives Individual-Profil für {symbol.upper()} vorhanden.")
        return TradingProfile(
            name="individual",
            rsi_oversold_threshold=fitted.rsi_oversold_threshold,
            rsi_overbought_threshold=fitted.rsi_overbought_threshold,
            bollinger_lower_threshold=fitted.bollinger_lower_threshold,
            adx_trend_strength_threshold=fitted.adx_trend_strength_threshold,
            stochastic_oversold_threshold=fitted.stochastic_oversold_threshold,
            description=f"Aktienindividuelles, validiertes Profil {symbol.upper()} v{fitted.version}.",
            opportunity_profile=self.SCORING,
        )
