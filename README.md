from stockmind.application.dashboard.models.fundamental_dashboard_result import (
    FundamentalDashboardResult
)

from stockmind.infrastructure.history.fundamental_data_repository import (
    FundamentalDataRepository
)


class FundamentalDashboardUseCase:

    def load(
        self,
        symbol: str
    ) -> FundamentalDashboardResult | None:

        entry = (
            FundamentalDataRepository()
            .load(
                symbol
            )
        )

        if entry is None:

            return None

        return FundamentalDashboardResult(
            symbol=entry.symbol,
            company_name=entry.company_name,
            sector=entry.sector,
            industry=entry.industry,
            market_cap=entry.market_cap,
            trailing_pe=entry.trailing_pe,
            forward_pe=entry.forward_pe,
            profit_margins=entry.profit_margins,
            revenue_growth=entry.revenue_growth,
            recommendation_key=entry.recommendation_key,
            target_mean_price=entry.target_mean_price
        )
