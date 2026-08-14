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

        #
        # latest_analysis
        #

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
                f"Keine Daten für {symbol} gefunden."
            )

        #
        # explanation
        #

        detail = (
            AnalysisDetailRepository()
            .load(
                symbol=symbol,
                profile_name=profile_name
            )
        )

        #
        # history
        #

        history = (
            AnalysisHistoryRepository()
            .load_by_symbol(
                symbol
            )
        )

        #
        # setups
        #

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

           
