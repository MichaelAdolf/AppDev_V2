from stockmind.application.dashboard.models.watchlist_dashboard_result import (
    WatchlistDashboardResult,
    WatchlistDashboardStock
)

from stockmind.infrastructure.history.latest_analysis_repository import (
    LatestAnalysisRepository
)

from stockmind.infrastructure.watchlists.watchlist_repository import (
    WatchlistRepository
)


class WatchlistDashboardUseCase:

    def load(
        self,
        profile_name: str
    ) -> WatchlistDashboardResult:

        latest_results = (
            LatestAnalysisRepository()
            .load_all(
                profile_name
            )
        )

        watchlist_entries = (
            WatchlistRepository()
            .load_all()
        )

        latest_by_symbol = {
            item.symbol.upper(): item
            for item in latest_results
        }

        stocks = []

        for watchlist_entry in watchlist_entries:

            latest = (
                latest_by_symbol.get(
                    watchlist_entry.symbol.upper()
                )
            )

            if latest is None:

                continue

            stocks.append(
                WatchlistDashboardStock(
                    symbol=latest.symbol,
                    company_name=watchlist_entry.company_name,
                    opportunity_score=latest.opportunity_score,
                    confidence=latest.confidence,
                    historical_success_rate=(
                        latest.historical_success_rate
                    ),
                    risk_level=latest.risk_level,
                    signal=latest.signal
                )
            )

        stock_count = len(
            stocks
        )

        buy_count = len(
            [
                item
                for item in stocks
                if item.signal == "BUY"
            ]
        )

        hold_count = len(
            [
                item
                for item in stocks
                if item.signal == "HOLD"
            ]
        )

        sell_count = len(
            [
                item
                for item in stocks
                if item.signal == "SELL"
            ]
        )

        hot_opportunities = len(
            [
                item
                for item in stocks
                if item.opportunity_score >= 80
            ]
        )

        return WatchlistDashboardResult(
            stock_count=stock_count,
            buy_count=buy_count,
            hold_count=hold_count,
            sell_count=sell_count,
            hot_opportunities=hot_opportunities,
            stocks=stocks
        )
