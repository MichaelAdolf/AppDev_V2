from stockmind.application.dashboard.models.stock_detail_dashboard_result import (
    StockDetailDashboardResult,
)

from stockmind.application.dashboard.use_cases.buy_period_dashboard_use_case import (
    BuyPeriodDashboardUseCase,
)

from stockmind.application.dashboard.use_cases.historical_setup_dashboard_use_case import (
    HistoricalSetupDashboardUseCase,
)

from stockmind.infrastructure.watchlists.watchlist_repository import (
    WatchlistRepository,
)

from stockmind.infrastructure.history.analysis_detail_repository import (
    AnalysisDetailRepository,
)

from stockmind.infrastructure.history.analysis_history_repository import (
    AnalysisHistoryRepository,
)

from stockmind.infrastructure.history.latest_analysis_repository import (
    LatestAnalysisRepository,
)


class StockDetailDashboardUseCase:

    def load(
        self,
        profile_name: str,
        symbol: str,
    ) -> StockDetailDashboardResult:

        symbol = symbol.upper()

        #
        # Aktuelle Analyse
        #

        latest_entries = (
            LatestAnalysisRepository()
            .load_all(profile_name)
        )

        stock = next(
            (
                item
                for item in latest_entries
                if item.symbol.upper() == symbol
            ),
            None,
        )

        if stock is None:
            raise ValueError(
                f"Keine aktuellen Analysedaten "
                f"für {symbol} gefunden."
            )

        #
        # Firmenname aus Watchlist
        #

        watchlist_entries = (
            WatchlistRepository()
            .load_all()
        )

        watchlist_entry = next(
            (
                entry
                for entry in watchlist_entries
                if entry.symbol.upper() == symbol
            ),
            None,
        )

        company_name = (
            watchlist_entry.company_name
            if (
                watchlist_entry is not None
                and watchlist_entry.company_name
            )
            else symbol
        )

        #
        # Analyse-Details
        #

        detail = (
            AnalysisDetailRepository()
            .load(
                symbol=symbol,
                profile_name=profile_name,
            )
        )

        #
        # Opportunity-Historie
        #
        # Wichtig:
        # Nur das aktuell gewählte Profil laden.
        #

        history = (
            AnalysisHistoryRepository()
            .load_by_symbol(
                symbol=symbol,
                profile_name=profile_name,
            )
        )

        #
        # Historische Einzel-Setups
        #

        setup_dashboard = (
            HistoricalSetupDashboardUseCase()
            .load(
                symbol,
                profile_name=profile_name,
                analysis_period="1y",
            )
        )

        #
        # BUY-Perioden
        #

        period_dashboard = (
            BuyPeriodDashboardUseCase()
            .load(
                symbol=symbol,
                profile_name=profile_name,
                analysis_period="5y",
                max_gap_days=3,
            )
        )

        stats = period_dashboard.statistics

        historical_source = (
            "BUY_PERIODS"
            if stats.complete_period_count > 0
            else "SETUP_FALLBACK"
        )

        #
        # Dashboard Result
        #

        return StockDetailDashboardResult(
            symbol=stock.symbol,

            company_name=company_name,

            profile_name=profile_name,

            score=stock.opportunity_score,

            confidence=stock.confidence,

            historical_success_rate=(
                stock.historical_success_rate
            ),

            historical_source=historical_source,

            risk_level=stock.risk_level,

            signal=stock.signal,

            summary=(
                detail.summary
                if detail
                else ""
            ),

            strengths=(
                detail.strengths.split("|")
                if (
                    detail
                    and detail.strengths
                )
                else []
            ),

            weaknesses=(
                detail.weaknesses.split("|")
                if (
                    detail
                    and detail.weaknesses
                )
                else []
            ),

            history=history,

            historical_setups=(
                setup_dashboard.setups
            ),

            setup_count=(
                setup_dashboard.setup_count
            ),

            successful_setup_count=(
                setup_dashboard.successful_count
            ),

            failed_setup_count=(
                setup_dashboard.failed_count
            ),

            setup_success_rate=(
                setup_dashboard.success_rate
            ),

            average_setup_days=(
                setup_dashboard.average_days
            ),

            average_setup_gain=(
                setup_dashboard.average_gain
            ),

            average_setup_drawdown=(
                setup_dashboard.average_drawdown
            ),

            active_buy_period=(
                period_dashboard.active_period
            ),

            buy_period_count=(
                period_dashboard.period_count
            ),

            complete_buy_period_count=(
                stats.complete_period_count
            ),

            incomplete_buy_period_count=(
                stats.incomplete_period_count
            ),

            period_target_hit_rate=(
                stats.target_hit_rate
            ),

            period_below_target_rate=(
                stats.below_target_rate
            ),

            period_flat_rate=(
                stats.flat_rate
            ),

            period_negative_rate=(
                stats.negative_rate
            ),
        )