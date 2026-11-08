from datetime import datetime
from uuid import uuid4
from stockmind.domain.strategy.fitted_profile import FittedProfile
from stockmind.infrastructure.strategy.fitted_profile_repository import FittedProfileRepository
class SaveFittedProfileCandidateUseCase:
 def __init__(self,database_path=None):self._repo=FittedProfileRepository(database_path)
 def execute(self,candidate):
  p=FittedProfile(str(uuid4()),candidate.symbol,self._repo.next_version(candidate.symbol),'CANDIDATE',candidate.base_profile,candidate.rsi_oversold_threshold,candidate.rsi_overbought_threshold,candidate.bollinger_lower_threshold,candidate.adx_trend_strength_threshold,candidate.stochastic_oversold_threshold,datetime.now().isoformat(timespec='seconds'));self._repo.save(p);return p
