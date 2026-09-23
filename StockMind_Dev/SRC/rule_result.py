from dataclasses import dataclass

@dataclass(frozen=True)
class RuleResult:
    rule_name: str

    triggered: bool

    score: float

    reason: str