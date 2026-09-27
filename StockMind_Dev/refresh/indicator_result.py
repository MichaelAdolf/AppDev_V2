from dataclasses import dataclass

@dataclass(frozen=True)
class IndicatorResult:
    symbol: str

    values: dict[str, float | int | bool | None]