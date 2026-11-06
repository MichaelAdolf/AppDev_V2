from dataclasses import dataclass
from stockmind.domain.portfolio.portfolio_purchase_lot import PortfolioPurchaseLot

@dataclass(frozen=True)
class PortfolioIntelligenceItem:
    position_id: str
    symbol: str
    company_name: str
    lots: list[PortfolioPurchaseLot]
    quantity: float
    weighted_purchase_price: float
    purchase_fees: float
    invested_amount: float
    current_price: float | None
    market_value: float | None
    unrealized_profit: float | None
    unrealized_return_pct: float | None
    target_price: float
    target_reached: bool
    target_distance_pct: float | None
    first_purchase_date: str
    holding_days: int
    remaining_strategy_days: int
    time_window_status: str
    entry_profile: str
    entry_score: float | None
    current_score: float | None
    score_change: float | None
    entry_confidence: float | None
    current_confidence: float | None
    confidence_change: float | None
    entry_risk: str | None
    current_risk: str | None
    entry_signal: str | None
    current_signal: str | None
    attention_reasons: list[str]
    attention_level: str
