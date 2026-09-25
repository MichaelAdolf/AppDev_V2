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

        score, valuation = (
            self._calculate_score(
                entry
            )
        )

        target_upside_pct = None

        if(
            entry.current_price is not None
            and entry.target_mean_price is not None
            and entry.current_price > 0
        ):
            target_upside_pct = (
                (
                entry.target_mean_price
                - entry.current_price
                )
                / entry.current_price
                *100
            )

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
            target_mean_price=entry.target_mean_price,
            fundamental_score=score,
            valuation=valuation,
            current_price=entry.current_price,
            target_upside_pct=target_upside_pct
        )

    def _calculate_score( self, entry ) -> tuple[float, str]:

        score = 50.0

        #
        # Revenue Growth
        #

        if entry.revenue_growth:

            if entry.revenue_growth > 0.20:

                score += 15

            elif entry.revenue_growth > 0.10:

                score += 10

        #
        # Profit Margin
        #

        if entry.profit_margins:

            if entry.profit_margins > 0.20:

                score += 15

            elif entry.profit_margins > 0.10:

                score += 10

        #
        # Forward PE
        #

        if entry.forward_pe:

            if entry.forward_pe < 20:

                score += 10

            elif entry.forward_pe > 40:

                score -= 10

        #
        # Analysten
        #

        recommendation = (
            entry.recommendation_key or ""
        ).lower()

        if recommendation == "strong_buy":

            score += 10

        elif recommendation == "buy":

            score += 5

        elif recommendation == "sell":

            score -= 10

        score = max(
            0,
            min(
                100,
                score
            )
        )

        if score >= 70:

            valuation = "ATTRACTIVE"

        elif score >= 50:

            valuation = "FAIR"

        else:

            valuation = "EXPENSIVE"

        return score, valuation
