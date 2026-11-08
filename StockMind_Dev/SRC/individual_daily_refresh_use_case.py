from dataclasses import dataclass
from stockmind.application.refresh.individual_daily_refresh_policy import IndividualDailyRefreshPolicy
from stockmind.application.strategy.run_individual_analysis_use_case import RunIndividualAnalysisUseCase

@dataclass(frozen=True)
class IndividualDailyRefreshResult:
    symbol: str
    refreshed: bool
    profile_id: str | None
    version: int | None
    reason: str

class IndividualDailyRefreshUseCase:
    """Bootstrap safety net for Individual Latest Analysis.

    The full BUY-signal, period and replay lifecycle is handled by the patched
    TrueIncrementalSymbolRefreshUseCase. This use case guarantees that an
    ACTIVE Individual also receives Latest Analysis immediately after a full
    bootstrap, where no incremental profile loop may have existed before.
    """
    def __init__(self,database_path=None):self._database_path=database_path
    def execute(self,symbol):
        decision=IndividualDailyRefreshPolicy(self._database_path).evaluate(symbol)
        if not decision.enabled:
            return IndividualDailyRefreshResult(decision.symbol,False,None,None,decision.reason)
        RunIndividualAnalysisUseCase(self._database_path).execute(decision.symbol)
        return IndividualDailyRefreshResult(decision.symbol,True,decision.profile_id,decision.version,'INDIVIDUAL_ANALYSIS_REFRESHED')
