from stockmind.application.exit.exit_strategy_selection_use_case import ExitStrategySelectionUseCase
from stockmind.application.exit.productive_exit_engine import ProductiveExitEngine
from stockmind.application.portfolio.portfolio_intelligence_use_case import PortfolioIntelligenceUseCase
from stockmind.infrastructure.history.chart_data_repository import ChartDataRepository

class PortfolioExitUseCase:
    def __init__(self,database_path=None):self._database_path=database_path
    def load(self):
        selector=ExitStrategySelectionUseCase(self._database_path);engine=ProductiveExitEngine();chart=ChartDataRepository(self._database_path);rows=[]
        for item in PortfolioIntelligenceUseCase(self._database_path).load():
            strategy,source,validation=selector.select(item.entry_profile)
            rows.append(engine.evaluate(item,strategy,source,validation,chart.load_by_symbol(item.symbol)))
        order={'EXIT_REVIEW':2,'WATCH':1,'HOLD':0};return sorted(rows,key=lambda x:order[x.status],reverse=True)
