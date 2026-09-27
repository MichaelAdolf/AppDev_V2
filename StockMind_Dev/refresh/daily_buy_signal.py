from dataclasses import dataclass


@dataclass(frozen=True)
class DailyBuySignal:
    symbol: str
    profile_name: str
    analysis_period: str
    trading_date: str
    is_buy: bool
    quality: str
    quality_score: float
    core_setup_detected: bool
    satisfied_rules: int
    required_rules: int
    reasons: list[str]
    missing_rules: list[str]
    entry_price: float
