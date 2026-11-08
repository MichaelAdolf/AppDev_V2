from dataclasses import dataclass
from stockmind.infrastructure.strategy.fitted_profile_repository import FittedProfileRepository

@dataclass(frozen=True)
class IndividualDailyRefreshDecision:
    symbol: str
    enabled: bool
    profile_id: str | None
    version: int | None
    reason: str

class IndividualDailyRefreshPolicy:
    def __init__(self,database_path=None):self._repo=FittedProfileRepository(database_path)
    def evaluate(self,symbol):
        profile=self._repo.load_active(symbol)
        if profile is None:
            return IndividualDailyRefreshDecision(symbol.upper(),False,None,None,'NO_ACTIVE_INDIVIDUAL')
        return IndividualDailyRefreshDecision(symbol.upper(),True,profile.id,profile.version,'ACTIVE_INDIVIDUAL')
    def profile_names(self,symbol,standard_profiles=None):
        profiles=list(standard_profiles or ['conservative','balanced','aggressive'])
        if self.evaluate(symbol).enabled:profiles.append('individual')
        return profiles
