import unittest
from datetime import datetime, timedelta

import pandas as pd

from stockmind.domain.history.historical_outcome import (
    HistoricalOutcome,
    evaluate_price_window,
)


class HistoricalOutcomeTest(unittest.TestCase):

    SETUP_DATE = datetime(2026, 1, 1)
    LOOKAHEAD_DAYS = 60

    def _data(
        self,
        final_return_pct: float,
        target_hit: bool = False,
        total_calendar_days: int = 70,
    ) -> pd.DataFrame:

        end_date = (
            self.SETUP_DATE
            + timedelta(days=total_calendar_days)
        )

        dates = pd.bdate_range(
            start=self.SETUP_DATE,
            end=end_date,
        )

        data = pd.DataFrame(
            {
                "High": [101.0] * len(dates),
                "Low": [99.0] * len(dates),
                "Close": [100.0] * len(dates),
            },
            index=dates,
        )

        window_end = (
            self.SETUP_DATE
            + timedelta(days=self.LOOKAHEAD_DAYS)
        )

        rows_inside_window = data.index[
            data.index <= window_end
        ]

        if len(rows_inside_window) > 0:

            last_trading_day_in_window = (
                rows_inside_window[-1]
            )

            final_close = (
                100.0
                * (
                    1
                    + final_return_pct / 100
                )
            )

            data.loc[
                last_trading_day_in_window,
                "Close",
            ] = final_close

        if target_hit:

            target_candidates = data.index[
                (
                    data.index
                    > self.SETUP_DATE
                    + timedelta(days=5)
                )
                & (
                    data.index
                    <= window_end
                )
            ]

            if len(target_candidates) > 0:

                target_date = target_candidates[0]

                data.loc[
                    target_date,
                    "High",
                ] = 108.5

        return data

    def test_target_hit(self):

        result = evaluate_price_window(
            self._data(
                final_return_pct=2.0,
                target_hit=True,
            ),
            setup_date=self.SETUP_DATE,
            entry_price=100.0,
        )

        self.assertEqual(
            result.outcome,
            HistoricalOutcome.TARGET_HIT,
        )

        self.assertTrue(
            result.target_hit
        )

        self.assertTrue(
            result.is_complete
        )

    def test_below_target(self):

        result = evaluate_price_window(
            self._data(
                final_return_pct=4.0,
            ),
            setup_date=self.SETUP_DATE,
            entry_price=100.0,
        )

        self.assertEqual(
            result.outcome,
            HistoricalOutcome.BELOW_TARGET,
        )

        self.assertAlmostEqual(
            result.window_end_return_pct,
            4.0,
            places=5,
        )

    def test_flat(self):

        result = evaluate_price_window(
            self._data(
                final_return_pct=0.5,
            ),
            setup_date=self.SETUP_DATE,
            entry_price=100.0,
        )

        self.assertEqual(
            result.outcome,
            HistoricalOutcome.FLAT,
        )

        self.assertAlmostEqual(
            result.window_end_return_pct,
            0.5,
            places=5,
        )

    def test_negative(self):

        result = evaluate_price_window(
            self._data(
                final_return_pct=-3.0,
            ),
            setup_date=self.SETUP_DATE,
            entry_price=100.0,
        )

        self.assertEqual(
            result.outcome,
            HistoricalOutcome.NEGATIVE,
        )

        self.assertAlmostEqual(
            result.window_end_return_pct,
            -3.0,
            places=5,
        )

    def test_incomplete_window(self):

        result = evaluate_price_window(
            self._data(
                final_return_pct=2.0,
                total_calendar_days=20,
            ),
            setup_date=self.SETUP_DATE,
            entry_price=100.0,
        )

        self.assertEqual(
            result.outcome,
            HistoricalOutcome.INCOMPLETE_WINDOW,
        )

        self.assertFalse(
            result.is_complete
        )

    def test_days_to_target_are_calendar_days(self):

        data = self._data(
            final_return_pct=2.0,
            target_hit=False,
        )

        target_date = datetime(
            2026,
            1,
            14,
        )

        data.loc[
            pd.Timestamp(target_date),
            "High",
        ] = 108.5

        result = evaluate_price_window(
            data,
            setup_date=self.SETUP_DATE,
            entry_price=100.0,
        )

        self.assertEqual(
            result.outcome,
            HistoricalOutcome.TARGET_HIT,
        )

        self.assertEqual(
            result.days_to_target,
            13,
        )


if __name__ == "__main__":
    unittest.main()
