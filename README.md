from dataclasses import dataclass

from stockmind.domain.history.analysis_history_entry import (
    AnalysisHistoryEntry
)

from stockmind.domain.history.historical_setup_entry import (
    HistoricalSetupEntry
)


@dataclass(frozen=True)
class StockDetailDashboardResult:

    symbol: str

    score: float

    confidence: float

    historical_success_rate: float

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
