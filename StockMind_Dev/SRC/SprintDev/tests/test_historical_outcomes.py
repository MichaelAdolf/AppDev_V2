import unittest
from datetime import datetime, timedelta

import pandas as pd

from stockmind.domain.history.historical_outcome import (
    HistoricalOutcome,
    evaluate_price_window,
)


class HistoricalOutcomeTest(unittest.TestCase):
    def _data(
        self,
        final_return_pct: float,
        target_hit: bool = False,
        total_calendar_days: int = 70,
    ) -> pd.DataFrame:
        start = datetime(2026, 1, 1)
        dates = pd.bdate_range(
            start=start,
            end=start + timedelta(days=total_calendar_days),
        )
        final_close = 100 * (1 + final_return_pct / 100)
        closes = [100.0] * len(dates)
        closes[-1] = final_close
        highs = [101.0] * len(dates)
        if target_hit and len(highs) > 5:
            highs[5] = 108.5
        lows = [99.0] * len(dates)
        return pd.DataFrame(
            {
                "High": highs,
                "Low": lows,
                "Close": closes,
            },
            index=dates,
        )

    def test_target_hit(self):
        result = evaluate_price_window(
            self._data(final_return_pct=2.0, target_hit=True),
            setup_date="2026-01-01",
            entry_price=100.0,
        )
        self.assertEqual(result.outcome, HistoricalOutcome.TARGET_HIT)
        self.assertTrue(result.target_hit)

    def test_below_target(self):
        result = evaluate_price_window(
            self._data(final_return_pct=4.0),
            setup_date="2026-01-01",
            entry_price=100.0,
        )
        self.assertEqual(result.outcome, HistoricalOutcome.BELOW_TARGET)

    def test_flat(self):
        result = evaluate_price_window(
            self._data(final_return_pct=0.5),
            setup_date="2026-01-01",
            entry_price=100.0,
        )
        self.assertEqual(result.outcome, HistoricalOutcome.FLAT)

    def test_negative(self):
        result = evaluate_price_window(
            self._data(final_return_pct=-3.0),
            setup_date="2026-01-01",
            entry_price=100.0,
        )
        self.assertEqual(result.outcome, HistoricalOutcome.NEGATIVE)

    def test_incomplete_window(self):
        result = evaluate_price_window(
            self._data(final_return_pct=2.0, total_calendar_days=20),
            setup_date="2026-01-01",
            entry_price=100.0,
        )
        self.assertEqual(
            result.outcome,
            HistoricalOutcome.INCOMPLETE_WINDOW,
        )
        self.assertFalse(result.is_complete)

    def test_days_to_target_are_calendar_days(self):
        result = evaluate_price_window(
            self._data(final_return_pct=2.0, target_hit=True),
            setup_date="2026-01-01",
            entry_price=100.0,
        )
        self.assertIsNotNone(result.days_to_target)
        self.assertGreaterEqual(result.days_to_target, 1)


if __name__ == "__main__":
    unittest.main()
