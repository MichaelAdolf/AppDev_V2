from stockmind.application.dashboard.models.stock_detail_dashboard_result import StockDetailDashboardResult
from stockmind.application.dashboard.use_cases.buy_period_dashboard_use_case import BuyPeriodDashboardUseCase
from stockmind.application.dashboard.use_cases.fundamental_dashboard_use_case import FundamentalDashboardUseCase
from stockmind.application.dashboard.use_cases.historical_setup_dashboard_use_case import HistoricalSetupDashboardUseCase
from stockmind.application.dashboard.use_cases.profile_comparison_dashboard_use_case import ProfileComparisonDashboardUseCase
from stockmind.application.dashboard.use_cases.score_calibration_use_case import ScoreCalibrationUseCase
from stockmind.infrastructure.history.analysis_detail_repository import AnalysisDetailRepository
from stockmind.infrastructure.history.historical_opportunity_repository import HistoricalOpportunityRepository
from stockmind.infrastructure.history.latest_analysis_repository import LatestAnalysisRepository
from stockmind.infrastructure.watchlists.watchlist_repository import WatchlistRepository

class StockDetailDashboardUseCase:
    def load(self,profile_name,symbol):
        symbol=symbol.upper();latest=LatestAnalysisRepository().load_all(profile_name);stock=next((x for x in latest if x.symbol.upper()==symbol),None)
        if stock is None:raise ValueError(f"Keine aktuellen Analysedaten für {symbol} gefunden.")
        detail=AnalysisDetailRepository().load(symbol=symbol,profile_name=profile_name)
        history=HistoricalOpportunityRepository().load_by_symbol(symbol,profile_name)
        watch=next((x for x in WatchlistRepository().load_all() if x.symbol.upper()==symbol),None)
        setups=HistoricalSetupDashboardUseCase().load(symbol,profile_name=profile_name,analysis_period="5y")
        periods=BuyPeriodDashboardUseCase().load(symbol,profile_name,"5y",3);stats=periods.statistics
        comparison=ProfileComparisonDashboardUseCase().load(symbol,"5y",3)
        buys=[e.profile_name for e in comparison.entries if e.signal=="BUY" or e.current_buy_signal is True]
        consensus=("Profil-Konsens: alle drei Profile bestätigen BUY." if len(set(buys))==3 else
                   f"Profil-Divergenz: {', '.join(buys)} bestätigen BUY." if buys else "Kein Profil bestätigt aktuell BUY.")
        previous=history[-2] if len(history)>=2 else None;current=history[-1] if history else None
        score_components={"quality":current.quality_component if current else 0.0,"confidence":current.confidence_component if current else 0.0,"historical":current.historical_component if current else 0.0,"risk":current.risk_component if current else 0.0}
        fundamental=FundamentalDashboardUseCase().load(symbol)
        diff=(fundamental.target_upside_pct-8.0 if fundamental and fundamental.target_upside_pct is not None else None)
        data_status={"market_data":history[-1].trading_date if history else None,"opportunity_replay":history[-1].trading_date if history else None,"buy_periods":max((p.end_date for p in periods.periods),default=None),"current_analysis":history[-1].trading_date if history else None,"fundamentals":"verfügbar" if fundamental else None}
        return StockDetailDashboardResult(symbol,watch.company_name if watch and watch.company_name else symbol,profile_name,stock.opportunity_score,stock.confidence,stock.historical_success_rate,"BUY_PERIODS" if stats.complete_period_count else "SETUP_FALLBACK",stock.risk_level,stock.signal,detail.summary if detail else "",detail.strengths.split("|") if detail and detail.strengths else [],detail.weaknesses.split("|") if detail and detail.weaknesses else [],history,setups.setups,setups.setup_count,setups.successful_count,setups.failed_count,setups.success_rate,setups.average_days,setups.average_gain,setups.average_drawdown,periods.active_period,periods.period_count,stats.complete_period_count,stats.incomplete_period_count,stats.target_hit_rate,stats.below_target_rate,stats.flat_rate,stats.negative_rate,stats,periods.active_period_phase,consensus,len(set(buys)),score_components,previous.opportunity_score if previous else None,(current.opportunity_score-previous.opportunity_score) if current and previous else None,previous.signal if previous else None,previous.confidence if previous else None,(current.confidence-previous.confidence) if current and previous else None,previous.risk_level if previous else None,ScoreCalibrationUseCase().load(symbol,profile_name),fundamental,diff,data_status)
