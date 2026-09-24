from dataclasses import dataclass

@dataclass(frozen=True)
class RiskResult:
    level: str
    score: float
    reasons: list[str]