from stockmind.application.dashboard.models.watchlist_dashboard_result import WatchlistDashboardResult,WatchlistDashboardStock
from stockmind.application.strategy.fitted_profile_signal_use_case import FittedProfileSignalUseCase
from stockmind.infrastructure.history.latest_analysis_repository import LatestAnalysisRepository
from stockmind.infrastructure.watchlists.watchlist_repository import WatchlistRepository
class WatchlistDashboardUseCase:
 def load(self,profile_name):
  latest={x.symbol.upper():x for x in LatestAnalysisRepository().load_all(profile_name)};stocks=[];fitted_uc=FittedProfileSignalUseCase()
  for w in WatchlistRepository().load_all():
   x=latest.get(w.symbol.upper())
   if not x:continue
   fitted=fitted_uc.evaluate(w.symbol);stocks.append(WatchlistDashboardStock(x.symbol,w.company_name,x.opportunity_score,x.confidence,x.historical_success_rate,x.risk_level,x.signal,fitted.active,fitted.strategy_name,fitted.signal,fitted.base_profile))
  return WatchlistDashboardResult(len(stocks),sum(x.signal=='BUY' for x in stocks),sum(x.signal=='HOLD' for x in stocks),sum(x.signal=='SELL' for x in stocks),sum(x.opportunity_score>=80 for x in stocks),stocks)
