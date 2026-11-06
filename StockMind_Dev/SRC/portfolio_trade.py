from dataclasses import dataclass


@dataclass(frozen=True)
class PortfolioTrade:
    id: str
    position_id: str
    symbol: str
    company_name: str
    purchase_date: str
    purchase_price: float
    sale_date: str
    sale_price: float
    quantity: float
    purchase_fees: float
    sale_fees: float
    tax_paid: float
    gross_profit: float
    profit_after_fees: float
    net_profit: float
    gross_return_pct: float
    net_return_pct: float
    holding_days: int
    entry_profile: str
    entry_signal: str | None
    entry_opportunity_score: float | None
    exit_reason: str
    note: str
    created_at: str
