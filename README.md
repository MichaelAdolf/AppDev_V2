@dataclass(frozen=True)
class WatchlistDashboardStock:

    symbol: str

    company_name: str

    opportunity_score: float

    confidence: float

    historical_success_rate: float

    risk_level: str

    signal: str
