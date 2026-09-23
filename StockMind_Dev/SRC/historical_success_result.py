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