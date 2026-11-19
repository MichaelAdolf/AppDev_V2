import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from stockmind.application.portfolio.add_position_use_case import AddPositionUseCase
from stockmind.application.portfolio.delete_portfolio_use_cases import DeletePurchaseLotUseCase
from stockmind.infrastructure.portfolio.portfolio_repository import PortfolioRepository


class PortfolioLotsTest(unittest.TestCase):
    def test_two_buys_are_one_aggregated_position_and_lot_can_be_deleted(self):
        with tempfile.TemporaryDirectory() as tmp:
            database = str(Path(tmp) / "portfolio.db")
            comparison = type("Comparison", (), {"entries": []})()

            with patch(
                "stockmind.application.portfolio.add_position_use_case.WatchlistRepository"
            ) as watch, patch(
                "stockmind.application.portfolio.add_position_use_case.ProfileComparisonDashboardUseCase"
            ) as profiles:
                watch.return_value.load_all.return_value = []
                profiles.return_value.load.return_value = comparison

                first_position = AddPositionUseCase(database).execute(
                    "NVDA", "2026-10-01", 100.0, 10.0, 5.0
                )
                second_position = AddPositionUseCase(database).execute(
                    "NVDA", "2026-10-10", 110.0, 5.0, 4.0
                )

            self.assertEqual(first_position.id, second_position.id)

            repository = PortfolioRepository(database)
            positions = repository.load_open_positions()
            self.assertEqual(len(positions), 1)
            self.assertEqual(positions[0].quantity, 15.0)
            self.assertAlmostEqual(positions[0].purchase_price, 103.333333, places=5)
            self.assertEqual(positions[0].purchase_fees, 9.0)

            lots = repository.load_lots_for_position(positions[0].id)
            self.assertEqual(len(lots), 2)

            DeletePurchaseLotUseCase(database).execute(lots[1].id)

            positions = repository.load_open_positions()
            self.assertEqual(len(positions), 1)
            self.assertEqual(positions[0].quantity, 10.0)
            self.assertEqual(
                len(repository.load_lots_for_position(positions[0].id)),
                1,
            )


if __name__ == "__main__":
    unittest.main()
