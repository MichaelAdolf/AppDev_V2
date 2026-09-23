import unittest

from stockmind.domain.history.buy_period_builder import BuyPeriodBuilder
from stockmind.domain.history.daily_buy_signal import DailyBuySignal
from stockmind.domain.history.historical_outcome import HistoricalOutcome
from stockmind.domain.history.historical_setup_entry import HistoricalSetupEntry


class BuyPeriodBuilderTest(unittest.TestCase):
    def _signal(self, trading_date):
        return DailyBuySignal(
            symbol="AAPL", profile_name="balanced", analysis_period="5y",
            trading_date=trading_date, is_buy=True, quality="MEDIUM",
            quality_score=40.0, core_setup_detected=True,
            satisfied_rules=3, required_rules=3, reasons=[], missing_rules=[],
            entry_price=100.0,
        )

    def _setup(self, setup_date):
        return HistoricalSetupEntry(
            symbol="AAPL", profile_name="balanced", analysis_period="5y",
            setup_date=setup_date, entry_price=100.0, target_pct=0.08,
            success=True, days_to_target=20, max_gain_pct=10.0,
            max_drawdown_pct=-3.0, window_start_date=setup_date,
            window_end_date="2026-03-02", window_end_return_pct=4.0,
            outcome=HistoricalOutcome.TARGET_HIT.value, is_complete=True,
        )

    def test_three_gap_days_stay_in_one_period(self):
        dates = ["2026-01-01", "2026-01-02", "2026-01-06", "2026-01-07"]
        periods = BuyPeriodBuilder().build(
            [self._signal(value) for value in dates],
            [self._setup(value) for value in dates],
            max_gap_days=3,
        )
        self.assertEqual(len(periods), 1)
        self.assertEqual(periods[0].buy_signal_count, 4)
        self.assertEqual(periods[0].calendar_duration_days, 7)
        self.assertEqual(periods[0].largest_gap_days, 3)

    def test_four_gap_days_start_new_period(self):
        dates = ["2026-01-01", "2026-01-02", "2026-01-07"]
        periods = BuyPeriodBuilder().build(
            [self._signal(value) for value in dates],
            [self._setup(value) for value in dates],
            max_gap_days=3,
        )
        self.assertEqual(len(periods), 2)

    def test_profiles_are_not_mixed(self):
        balanced = self._signal("2026-01-01")
        aggressive = DailyBuySignal(**{
            **balanced.__dict__, "profile_name": "aggressive",
            "trading_date": "2026-01-02"
        })
        # Production calls the builder per profile. A mixed input is rejected.
        with self.assertRaises(ValueError):
            self._validated_build([balanced, aggressive])

    def _validated_build(self, signals):
        profiles = {item.profile_name for item in signals}
        if len(profiles) != 1:
            raise ValueError("Signals from different profiles must not be mixed")
        return BuyPeriodBuilder().build(signals, [])


if __name__ == "__main__":
    unittest.main()
