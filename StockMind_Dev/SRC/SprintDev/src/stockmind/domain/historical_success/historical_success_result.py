from dataclasses import dataclass


@dataclass(frozen=True)
class HistoricalSuccessResult:
    symbol: str
    profile_name: str
    rule_set_name: str
    setup_count: int
    success_count: int
    failure_count: int
    success_rate: float
    target_pct: float
    lookahead_days: int
    min_quality: str
    sample_quality: str
    similarity_mode: bool = False
    top_n_similar: int | None = None
    average_similarity: float | None = None
    complete_count: int = 0
    target_hit_count: int = 0
    below_target_count: int = 0
    flat_count: int = 0
    negative_count: int = 0
    incomplete_count: int = 0
    target_hit_rate: float = 0.0
    below_target_rate: float = 0.0
    flat_rate: float = 0.0
    negative_rate: float = 0.0
