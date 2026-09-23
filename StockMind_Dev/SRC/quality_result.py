from dataclasses import dataclass

@dataclass(frozen=True)
class QualityResult:
    quality: str
    score: float
    reasons: list[str]