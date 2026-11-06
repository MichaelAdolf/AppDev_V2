from datetime import date, timedelta

from stockmind.infrastructure.portfolio.portfolio_repository import PortfolioRepository


class PortfolioPerformanceUseCase:
    def __init__(self, database_path: str | None = None):
        self._repository = PortfolioRepository(database_path)

    def load(self):
        trades = self._repository.load_trades()
        today = date.today()
        starts = {
            "month": today.replace(day=1),
            "six_months": today - timedelta(days=183),
            "ytd": date(today.year, 1, 1),
            "twelve_months": today - timedelta(days=365),
        }
        result = {"all": self._aggregate(trades)}
        for key, start in starts.items():
            result[key] = self._aggregate([
                t for t in trades if date.fromisoformat(t.sale_date) >= start
            ])
        return result

    def _aggregate(self, trades):
        winners = [t for t in trades if t.net_profit > 0]
        return {
            "trade_count": len(trades),
            "net_profit": sum(t.net_profit for t in trades),
            "gross_profit": sum(t.gross_profit for t in trades),
            "profit_after_fees": sum(t.profit_after_fees for t in trades),
            "tax_paid": sum(t.tax_paid for t in trades),
            "winner_count": len(winners),
            "win_rate": len(winners) / len(trades) if trades else 0.0,
            "average_holding_days": sum(t.holding_days for t in trades) / len(trades) if trades else 0.0,
        }
