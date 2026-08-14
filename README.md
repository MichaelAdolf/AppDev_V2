from stockmind.application.dashboard.models.stock_detail_dashboard_result import (
    StockDetailDashboardResult
)

from stockmind.infrastructure.history.latest_analysis_repository import (
    LatestAnalysisRepository
)

from stockmind.infrastructure.history.analysis_detail_repository import (
    AnalysisDetailRepository
)

from stockmind.infrastructure.history.analysis_history_repository import (
    AnalysisHistoryRepository
)

from stockmind.application.dashboard.use_cases.historical_setup_dashboard_use_case import (
    HistoricalSetupDashboardUseCase
)


class StockDetailDashboardUseCase:

    def load(
        self,
        profile_name: str,
        symbol: str
    ) -> StockDetailDashboardResult:

        latest_entries = (
            LatestAnalysisRepository()
            .load_all(
                profile_name
            )
        )

        stock = next(
            (
                item
                for item in latest_entries
                if item.symbol == symbol
            ),
            None
        )

        if stock is None:

            raise ValueError(
                f"Keine aktuellen Analysedaten für {symbol} gefunden."
            )

        detail = (
            AnalysisDetailRepository()
            .load(
                symbol=symbol,
                profile_name=profile_name
            )
        )

        history = (
            AnalysisHistoryRepository()
            .load_by_symbol(
                symbol
            )
        )

        setup_dashboard = (
            HistoricalSetupDashboardUseCase()
            .load(
                symbol
            )
        )

        return StockDetailDashboardResult(
            symbol=stock.symbol,

            score=stock.opportunity_score,

            confidence=stock.confidence,

            historical_success_rate=(
                stock.historical_success_rate
            ),

            risk_level=stock.risk_level,

            signal=stock.signal,

            summary=(
                detail.summary
                if detail
                else ""
            ),

            strengths=(
                detail.strengths.split("|")
                if detail and detail.strengths
                else []
            ),

            weaknesses=(
                detail.weaknesses.split("|")
                if detail and detail.weaknesses
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
            )
        )
