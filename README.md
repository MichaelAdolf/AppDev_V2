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
