from dataclasses import dataclass

@dataclass(frozen=True)
class WatchlistDashboardResult:

    symbol: str

    company_name: str

    opportunity_score: float

    confidence: float

    historical_success_rate: float

    risk_level: str

    signal: str
    
    stock_count: int
    buy_count: int
    hold_count: int
    sell_count: int
    hot_opportunities: int
    stocks: list