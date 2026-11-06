from dataclasses import dataclass

@dataclass(frozen=True)
class ExitStrategy:
    name: str
    target_pct: float = 0.08
    max_holding_days: int = 60
    stop_loss_pct: float | None = None
    trailing_stop_pct: float | None = None
    score_drop: float | None = None
    confidence_drop: float | None = None
    exit_on_hold: bool = False
    exit_on_sell: bool = False
    exit_on_high_risk: bool = False

    @staticmethod
    def research_candidates():
        return [
            ExitStrategy('BASELINE_8PCT_60D'),
            ExitStrategy('STOP_LOSS_5PCT',stop_loss_pct=0.05),
            ExitStrategy('STOP_LOSS_8PCT',stop_loss_pct=0.08),
            ExitStrategy('TRAILING_4PCT',trailing_stop_pct=0.04),
            ExitStrategy('TRAILING_6PCT',trailing_stop_pct=0.06),
            ExitStrategy('SCORE_DROP_10',score_drop=10.0),
            ExitStrategy('SCORE_DROP_15',score_drop=15.0),
            ExitStrategy('CONFIDENCE_DROP_15P',confidence_drop=0.15),
            ExitStrategy('SIGNAL_HOLD',exit_on_hold=True),
            ExitStrategy('SIGNAL_SELL',exit_on_sell=True),
            ExitStrategy('RISK_HIGH',exit_on_high_risk=True),
        ]
