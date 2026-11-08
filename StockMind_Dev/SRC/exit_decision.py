from dataclasses import dataclass

@dataclass(frozen=True)
class ExitDecision:
    position_id: str
    symbol: str
    profile_name: str
    status: str
    strategy_name: str
    strategy_source: str
    validation_status: str
    reasons: list[str]
    action_text: str
