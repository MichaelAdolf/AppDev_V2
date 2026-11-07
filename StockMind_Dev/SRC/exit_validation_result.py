from dataclasses import dataclass


@dataclass(frozen=True)
class ExitValidationRow:
    strategy_name: str
    train_sample_count: int
    validation_sample_count: int
    train_average_return_pct: float
    validation_average_return_pct: float
    train_positive_rate: float
    validation_positive_rate: float
    train_average_drawdown_pct: float
    validation_average_drawdown_pct: float
    return_degradation_pct: float
    positive_rate_degradation: float
    robustness_status: str


@dataclass(frozen=True)
class WalkForwardFoldResult:
    fold_number: int
    train_start: str
    train_end: str
    validation_start: str
    validation_end: str
    strategy_name: str
    train_average_return_pct: float
    validation_average_return_pct: float
    validation_positive_rate: float
    validation_sample_count: int
