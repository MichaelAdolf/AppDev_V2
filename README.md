from stockmind.application.dashboard.models.watchlist_dashboard_result import (
    WatchlistDashboardResult
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

        watchlist_symbols = {
            entry.symbol.upper()
            for entry in watchlist_entries
            if entry.active
        }

        results = [
            item
            for item in latest_results
            if item.symbol.upper()
            in watchlist_symbols
        ]

        stock_count = len(
            results
        )

        buy_count = len(
            [
                item
                for item in results
                if item.signal == "BUY"
            ]
        )

        hold_count = len(
            [
                item
                for item in results
                if item.signal == "HOLD"
            ]
        )

        sell_count = len(
            [
                item
                for item in results
                if item.signal == "SELL"
            ]
        )

        hot_opportunities = len(
            [
                item
                for item in results
                if item.opportunity_score >= 80
            ]
        )

        return WatchlistDashboardResult(
            stock_count=stock_count,
            buy_count=buy_count,
            hold_count=hold_count,
            sell_count=sell_count,
            hot_opportunities=hot_opportunities,
            stocks=results
        )
