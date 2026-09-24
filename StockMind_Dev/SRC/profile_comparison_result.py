from dataclasses import dataclass

@dataclass(frozen=True)
class ProfileComparisonEntry:

    profile_name: str

    score: float

    confidence: float

    signal: str

    risk_level: str

@dataclass(frozen=True)
class ProfileComparisonResult:

    symbol: str

    entries: list[ProfileComparisonEntry]