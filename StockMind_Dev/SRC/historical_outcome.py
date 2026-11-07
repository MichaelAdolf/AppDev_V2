from dataclasses import dataclass
from datetime import date, datetime, timedelta
from enum import Enum

import pandas as pd


class HistoricalOutcome(str, Enum):
    TARGET_HIT = "TARGET_HIT"
    BELOW_TARGET = "BELOW_TARGET"
    FLAT = "FLAT"
    NEGATIVE = "NEGATIVE"
    INCOMPLETE_WINDOW = "INCOMPLETE_WINDOW"


@dataclass(frozen=True)
class HistoricalOutcomeEvaluation:
    outcome: HistoricalOutcome
    target_hit: bool
    is_complete: bool
    window_start_date: str
    window_end_date: str
    days_to_target: int | None
    window_end_return_pct: float | None
    max_gain_pct: float | None
    max_drawdown_pct: float | None


def _to_timestamp(value) -> pd.Timestamp:
    timestamp = pd.Timestamp(value)
    if timestamp.tzinfo is not None:
        timestamp = timestamp.tz_localize(None)
    return timestamp.normalize()


def evaluate_price_window(
    data: pd.DataFrame,
    setup_date,
    entry_price: float,
    target_pct: float = 0.08,
    lookahead_calendar_days: int = 60,
    flat_threshold_pct: float = 1.0,
) -> HistoricalOutcomeEvaluation:
    """Evaluate one setup over a calendar-day window.

    Entry is the setup day's close. A target is considered hit when a later
    daily high reaches entry_price * (1 + target_pct). BELOW_TARGET, FLAT and
    NEGATIVE are determined from the final available close inside a complete
    calendar window. An incomplete window is excluded from aggregate rates.
    """
    if entry_price <= 0:
        raise ValueError("entry_price must be greater than zero")
    if lookahead_calendar_days <= 0:
        raise ValueError("lookahead_calendar_days must be greater than zero")
    if flat_threshold_pct < 0:
        raise ValueError("flat_threshold_pct must not be negative")
    if data.empty:
        setup_ts = _to_timestamp(setup_date)
        end_ts = setup_ts + timedelta(days=lookahead_calendar_days)
        return HistoricalOutcomeEvaluation(
            outcome=HistoricalOutcome.INCOMPLETE_WINDOW,
            target_hit=False,
            is_complete=False,
            window_start_date=setup_ts.date().isoformat(),
            window_end_date=end_ts.date().isoformat(),
            days_to_target=None,
            window_end_return_pct=None,
            max_gain_pct=None,
            max_drawdown_pct=None,
        )

    prepared = data.copy()
    if "Date" in prepared.columns:
        timestamps = pd.to_datetime(prepared["Date"])
        prepared = prepared.drop(columns=["Date"])
        prepared.index = timestamps

    prepared.index = pd.DatetimeIndex([
        _to_timestamp(value) for value in prepared.index
    ])
    prepared = prepared.sort_index()

    setup_ts = _to_timestamp(setup_date)
    window_end_ts = setup_ts + timedelta(days=lookahead_calendar_days)
    latest_ts = _to_timestamp(prepared.index.max())
    is_complete = latest_ts >= window_end_ts

    future = prepared.loc[
        (prepared.index > setup_ts)
        & (prepared.index <= window_end_ts)
    ]

    if future.empty:
        return HistoricalOutcomeEvaluation(
            outcome=HistoricalOutcome.INCOMPLETE_WINDOW,
            target_hit=False,
            is_complete=False,
            window_start_date=setup_ts.date().isoformat(),
            window_end_date=window_end_ts.date().isoformat(),
            days_to_target=None,
            window_end_return_pct=None,
            max_gain_pct=None,
            max_drawdown_pct=None,
        )

    target_price = entry_price * (1 + target_pct)
    target_rows = future.loc[future["High"].astype(float) >= target_price]
    target_hit = not target_rows.empty
    days_to_target = None
    if target_hit:
        target_date = _to_timestamp(target_rows.index[0])
        days_to_target = (target_date - setup_ts).days

    max_high = float(future["High"].max())
    min_low = float(future["Low"].min())
    final_close = float(future["Close"].iloc[-1])

    max_gain_pct = ((max_high - entry_price) / entry_price) * 100
    max_drawdown_pct = ((min_low - entry_price) / entry_price) * 100
    window_end_return_pct = ((final_close - entry_price) / entry_price) * 100

    if not is_complete:
        outcome = HistoricalOutcome.INCOMPLETE_WINDOW
    elif target_hit:
        outcome = HistoricalOutcome.TARGET_HIT
    elif window_end_return_pct > flat_threshold_pct:
        outcome = HistoricalOutcome.BELOW_TARGET
    elif window_end_return_pct >= -flat_threshold_pct:
        outcome = HistoricalOutcome.FLAT
    else:
        outcome = HistoricalOutcome.NEGATIVE

    return HistoricalOutcomeEvaluation(
        outcome=outcome,
        target_hit=target_hit,
        is_complete=is_complete,
        window_start_date=setup_ts.date().isoformat(),
        window_end_date=window_end_ts.date().isoformat(),
        days_to_target=days_to_target,
        window_end_return_pct=window_end_return_pct,
        max_gain_pct=max_gain_pct,
        max_drawdown_pct=max_drawdown_pct,
    )
