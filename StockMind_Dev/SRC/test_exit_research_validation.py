import unittest
from types import SimpleNamespace

from stockmind.application.exit.exit_simulation_use_case import ExitSimulationUseCase
from stockmind.domain.exit.exit_strategy import ExitStrategy


class ExitResearchValidationTest(unittest.TestCase):
    def test_intraday_high_reaches_target_at_exact_target_price(self):
        period = SimpleNamespace(
            symbol="NVDA", profile_name="balanced",
            start_date="2026-01-01", entry_price=100.0,
        )
        prices = [
            SimpleNamespace(
                trading_date="2026-01-01", close_price=100.0,
                high_price=101.0, low_price=99.0,
            ),
            SimpleNamespace(
                trading_date="2026-01-05", close_price=106.0,
                high_price=109.0, low_price=104.0,
            ),
        ]
        result = ExitSimulationUseCase().simulate(
            period, prices, [], ExitStrategy("BASELINE")
        )
        self.assertEqual(result.exit_reason, "TARGET_REACHED")
        self.assertAlmostEqual(result.exit_price, 108.0)
        self.assertAlmostEqual(result.return_pct, 8.0)

    def test_same_bar_stop_and_target_uses_conservative_stop_order(self):
        period = SimpleNamespace(
            symbol="NVDA", profile_name="balanced",
            start_date="2026-01-01", entry_price=100.0,
        )
        prices = [SimpleNamespace(
            trading_date="2026-01-02", close_price=102.0,
            high_price=109.0, low_price=94.0,
        )]
        result = ExitSimulationUseCase().simulate(
            period, prices, [],
            ExitStrategy("STOP", stop_loss_pct=0.05),
        )
        self.assertEqual(result.exit_reason, "STOP_LOSS")
        self.assertAlmostEqual(result.exit_price, 95.0)


if __name__ == "__main__":
    unittest.main()
