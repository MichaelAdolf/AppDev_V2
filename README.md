from dataclasses import dataclass


@dataclass(frozen=True)
class HistoricalSetupEntry:

    symbol: str

    profile_name: str

    analysis_period: str

    setup_date: str

    entry_price: float

    target_pct: float

    success: bool

    days_to_target: int | None

    max_gain_pct: float

    max_drawdown_pct: float
