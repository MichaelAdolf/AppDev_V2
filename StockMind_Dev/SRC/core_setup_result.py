from dataclasses import dataclass

@dataclass(frozen=True)
class CoreSetupResult:
    setup_detected: bool
    satisfied_rules: int
    required_rules: int
    core_score: float
    missing_rules: list[str]
    reasons: list[str]