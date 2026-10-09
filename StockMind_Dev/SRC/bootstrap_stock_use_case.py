from stockmind.application.history.historical_opportunity_replay_use_case import HistoricalOpportunityReplayUseCase
from stockmind.application.history.historical_setup_replay_use_case import HistoricalSetupReplayUseCase
from stockmind.application.history.refresh_buy_periods_use_case import RefreshBuyPeriodsUseCase
from stockmind.application.refresh.incremental_market_refresh import refresh_symbol
from stockmind.application.use_cases.run_analysis_use_case import RunAnalysisUseCase

PROFILES=["conservative","balanced","aggressive"]
PERIODS=["1m","6m","1y","3y","5y"]

class BootstrapStockUseCase:
    def execute(self,symbol:str):
        symbol=symbol.upper();refresh_symbol(symbol,full=True)
        replay=HistoricalSetupReplayUseCase();periods=RefreshBuyPeriodsUseCase()
        for profile in PROFILES:
            for analysis_period in PERIODS:
                replay.execute(symbol=symbol,profile_name=profile,analysis_period=analysis_period,target_pct=.08,lookahead_days=60)
                periods.execute(symbol=symbol,profile_name=profile,analysis_period=analysis_period,max_gap_days=3,target_pct=.08)
            HistoricalOpportunityReplayUseCase().execute(symbol=symbol,profile_name=profile,period="5y")
            RunAnalysisUseCase().execute(profile_name=profile,symbol=symbol)
