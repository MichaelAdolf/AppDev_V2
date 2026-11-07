from stockmind.application.exit.exit_simulation_use_case import ExitSimulationUseCase
from stockmind.domain.exit.exit_strategy import ExitStrategy
from stockmind.infrastructure.history.buy_period_repository import BuyPeriodRepository
from stockmind.infrastructure.history.chart_data_repository import ChartDataRepository
from stockmind.infrastructure.history.historical_opportunity_repository import HistoricalOpportunityRepository

class ExitStrategyResearchUseCase:
    PROFILES=('conservative','balanced','aggressive')
    def __init__(self,database_path=None):self._database_path=database_path
    def analyze(self,symbol,profile_name='balanced'):
        periods=[p for p in BuyPeriodRepository(self._database_path).load_by_symbol(symbol,profile_name,'5y') if p.is_complete]
        prices=ChartDataRepository(self._database_path).load_by_symbol(symbol);opps=HistoricalOpportunityRepository(self._database_path).load_by_symbol(symbol,profile_name);sim=ExitSimulationUseCase();details={};summaries=[]
        for strategy in ExitStrategy.research_candidates():
            results=[sim.simulate(p,prices,opps,strategy) for p in periods];details[strategy.name]=[x for x in results if x];summaries.append(sim.summarize(strategy.name,results))
        return {'symbol':symbol.upper(),'profile_name':profile_name,'period_count':len(periods),'summaries':sorted(summaries,key=lambda x:(x.average_return_pct,x.positive_rate),reverse=True),'details':details}
    def analyze_all_profiles(self,symbol):return {p:self.analyze(symbol,p) for p in self.PROFILES}
