from dataclasses import dataclass
from stockmind.domain.history.historical_opportunity_entry import HistoricalOpportunityEntry
from stockmind.domain.history.historical_setup_entry import HistoricalSetupEntry
from stockmind.domain.history.buy_period_entry import BuyPeriodEntry
from stockmind.application.dashboard.models.buy_period_dashboard_result import BuyPeriodStatistics
from stockmind.application.dashboard.models.score_calibration_result import ScoreBandResult

@dataclass(frozen=True)
class StockDetailDashboardResult:
    symbol:str; company_name:str; profile_name:str; score:float; confidence:float
    historical_success_rate:float; historical_source:str; risk_level:str; signal:str
    summary:str; strengths:list[str]; weaknesses:list[str]; history:list[HistoricalOpportunityEntry]
    historical_setups:list[HistoricalSetupEntry]; setup_count:int; successful_setup_count:int
    failed_setup_count:int; setup_success_rate:float; average_setup_days:float
    average_setup_gain:float; average_setup_drawdown:float; active_buy_period:BuyPeriodEntry|None
    buy_period_count:int; complete_buy_period_count:int; incomplete_buy_period_count:int
    period_target_hit_rate:float; period_below_target_rate:float; period_flat_rate:float
    period_negative_rate:float; period_statistics:BuyPeriodStatistics; active_period_phase:str
    profile_consensus:str; profile_buy_count:int; score_components:dict[str,float]
    previous_score:float|None; score_change:float|None; previous_signal:str|None
    previous_confidence:float|None; confidence_change:float|None; previous_risk:str|None
    calibration:list[ScoreBandResult]; fundamental:object|None; analyst_target_difference_pct:float|None
    data_status:dict[str,str|None]
