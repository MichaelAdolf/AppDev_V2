from dataclasses import dataclass

@dataclass(frozen=True)
class AlertResult:
    title: str
    message: str
    severity: str