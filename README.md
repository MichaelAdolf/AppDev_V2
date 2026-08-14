class WatchlistDashboardUseCase:

    def load(
        self,
        profile_name: str
    ) -> WatchlistDashboardResult:

        results = (
            LatestAnalysisRepository()
            .load_all(
                profile_name
            )
        )

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
