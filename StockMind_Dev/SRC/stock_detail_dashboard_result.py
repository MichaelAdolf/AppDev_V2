from dataclasses import dataclass

from stockmind.domain.history.analysis_history_entry import AnalysisHistoryEntry
from stockmind.domain.history.historical_setup_entry import HistoricalSetupEntry
from stockmind.domain.history.buy_period_entry import BuyPeriodEntry


@dataclass(frozen=True)
class StockDetailDashboardResult:
    symbol: str
    profile_name: str
    score: float
    confidence: float
    historical_success_rate: float
    historical_source: str
    risk_level: str
    signal: str
    summary: str
    strengths: list[str]
    weaknesses: list[str]
    history: list[AnalysisHistoryEntry]
    historical_setups: list[HistoricalSetupEntry]
    setup_count: int
    successful_setup_count: int
    failed_setup_count: int
    setup_success_rate: float
    average_setup_days: float
    average_setup_gain: float
    average_setup_drawdown: float
    active_buy_period: BuyPeriodEntry | None
    buy_period_count: int
    complete_buy_period_count: int
    incomplete_buy_period_count: int
    period_target_hit_rate: float
    period_below_target_rate: float
    period_flat_rate: float
    period_negative_rate: float
