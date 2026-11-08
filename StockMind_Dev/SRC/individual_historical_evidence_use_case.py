from stockmind.domain.historical_success.historical_evidence_result import HistoricalEvidenceResult
from stockmind.infrastructure.strategy.fitted_profile_repository import FittedProfileRepository

class IndividualHistoricalEvidenceUseCase:
    def __init__(self,database_path=None):self._repo=FittedProfileRepository(database_path)
    def load(self,symbol):
        profile=self._repo.load_active(symbol)
        if profile is None:raise ValueError(f"Kein aktives Individual-Profil für {symbol.upper()} vorhanden.")
        validation=self._repo.load_validation(profile.id)
        if not validation:return HistoricalEvidenceResult(0.0,"NO_SAMPLE","INDIVIDUAL_VALIDATION",0,0.0,0.0,0.0,0.0,0,None,None,None,None)
        count=int(validation['validation_sample_count']);rate=float(validation['validation_target_hit_rate']);quality='HIGH' if count>=50 else 'MEDIUM' if count>=20 else 'LOW' if count>0 else 'NO_SAMPLE'
        return HistoricalEvidenceResult(
            success_rate=rate,sample_quality=quality,source="INDIVIDUAL_VALIDATION",sample_count=count,
            target_hit_rate=rate,below_target_rate=0.0,flat_rate=0.0,negative_rate=max(0.0,1-rate),
            incomplete_count=0,average_similarity=None,active_period_start=None,
            active_period_duration_days=None,active_period_buy_signal_count=None,
        )
