from dataclasses import dataclass

@dataclass(frozen=True)
class PortfolioPurchaseLot:
    id: str
    position_id: str
    symbol: str
    purchase_date: str
    purchase_price: float
    quantity: float
    purchase_fees: float
    entry_profile: str
    entry_signal: str | None
    entry_opportunity_score: float | None
    entry_confidence: float | None
    entry_risk: str | None
    entry_target_hit_rate: float | None
    entry_sample_count: int
    entry_profile_buy_count: int
    entry_buy_period_start: str | None
    note: str
    created_at: str
    updated_at: str
