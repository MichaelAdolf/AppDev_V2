import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from stockmind.application.portfolio.add_position_use_case import AddPositionUseCase
from stockmind.application.portfolio.sell_position_use_case import SellPositionUseCase
from stockmind.infrastructure.portfolio.portfolio_repository import PortfolioRepository


class PortfolioFoundationTest(unittest.TestCase):
    def test_position_can_be_added_and_fully_closed(self):
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
                position = AddPositionUseCase(database).execute(
                    symbol="NVDA", purchase_date="2026-10-01",
                    purchase_price=100.0, quantity=10,
                    purchase_fees=5.0, entry_profile="balanced",
                )
            repository = PortfolioRepository(database)
            self.assertEqual(len(repository.load_open_positions()), 1)
            trade = SellPositionUseCase(database).execute(
                position_id=position.id, sale_date="2026-10-31",
                sale_price=110.0, sale_fees=5.0, tax_paid=10.0,
                exit_reason="TARGET_REACHED",
            )
            self.assertEqual(trade.gross_profit, 100.0)
            self.assertEqual(trade.profit_after_fees, 90.0)
            self.assertEqual(trade.net_profit, 80.0)
            self.assertEqual(len(repository.load_open_positions()), 0)
            self.assertEqual(len(repository.load_trades()), 1)


if __name__ == "__main__":
    unittest.main()
