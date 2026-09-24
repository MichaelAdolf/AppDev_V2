from dataclasses import dataclass

@dataclass(frozen=True)
class ExplanationResult:

    title: str

    summary: str

    strengths: list[str]

    weaknesses: list[str]

    opportunity_score: float