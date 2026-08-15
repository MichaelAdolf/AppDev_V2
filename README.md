from dataclasses import dataclass


@dataclass(frozen=True)
class FundamentalDashboardResult:

    symbol: str

    company_name: str | None

    sector: str | None

    industry: str | None

    market_cap: float | None

    trailing_pe: float | None

    forward_pe: float | None

    profit_margins: float | None

    revenue_growth: float | None

    recommendation_key: str | None

    target_mean_price: float | None
