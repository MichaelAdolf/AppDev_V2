from dataclasses import dataclass

@dataclass(frozen=True)
class ExitSimulationResult:
    symbol: str
    profile_name: str
    period_start: str
    strategy_name: str
    exit_date: str
    exit_reason: str
    entry_price: float
    exit_price: float
    return_pct: float
    holding_days: int
    max_gain_pct: float
    max_drawdown_pct: float
    target_reached_before_exit: bool

@dataclass(frozen=True)
class ExitStrategySummary:
    strategy_name: str
    sample_count: int
    positive_count: int
    target_reached_count: int
    positive_rate: float
    target_reached_rate: float
    average_return_pct: float
    median_return_pct: float
    average_holding_days: float
    average_max_drawdown_pct: float
    worst_return_pct: float
    best_return_pct: float
