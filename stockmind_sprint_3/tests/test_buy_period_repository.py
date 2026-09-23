import tempfile
import unittest
from pathlib import Path

from stockmind.domain.history.buy_period_entry import BuyPeriodEntry
from stockmind.infrastructure.history.buy_period_repository import BuyPeriodRepository


class BuyPeriodRepositoryTest(unittest.TestCase):
    def test_replace_and_load(self):
        with tempfile.TemporaryDirectory() as directory:
            repository = BuyPeriodRepository(str(Path(directory) / "test.db"))
            period = BuyPeriodEntry(
                symbol="AAPL", profile_name="balanced", analysis_period="5y",
                start_date="2026-01-01", end_date="2026-01-07",
                calendar_duration_days=7, buy_signal_count=4,
                gap_days_total=3, largest_gap_days=3, entry_price=100.0,
                target_pct=0.08, outcome="TARGET_HIT", target_hit=True,
                days_to_target=20, window_end_date="2026-03-02",
                window_end_return_pct=4.0, max_gain_pct=10.0,
                max_drawdown_pct=-3.0, is_complete=True,
            )
            repository.replace_for("AAPL", "balanced", "5y", [period])
            loaded = repository.load_by_symbol("AAPL", "balanced", "5y")
            self.assertEqual(len(loaded), 1)
            self.assertEqual(loaded[0].buy_signal_count, 4)
            self.assertEqual(loaded[0].profile_name, "balanced")


if __name__ == "__main__":
    unittest.main()
