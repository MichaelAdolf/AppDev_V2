from dataclasses import dataclass

@dataclass(frozen=True)
class CrossStockStrategyRow:
    profile_name: str
    strategy_name: str
    eligible_stock_count: int
    stable_stock_count: int
    degraded_stock_count: int
    failed_stock_count: int
    insufficient_stock_count: int
    stable_rate: float
    average_validation_return_pct: float
    median_validation_return_pct: float
    average_validation_positive_rate: float
    average_validation_drawdown_pct: float
    worst_stock_validation_return_pct: float
    average_return_degradation_pct: float
    walk_forward_fold_count: int
    walk_forward_positive_fold_rate: float
    robustness_score: float
    recommendation_status: str

@dataclass(frozen=True)
class StockStrategyValidationRow:
    symbol: str
    company_name: str
    profile_name: str
    strategy_name: str
    robustness_status: str
    train_sample_count: int
    validation_sample_count: int
    validation_average_return_pct: float
    validation_positive_rate: float
    validation_average_drawdown_pct: float
    return_degradation_pct: float
