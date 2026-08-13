from stockmind.domain.history.top_mover_result import (
    TopMoverResult
)

from stockmind.domain.history.opportunity_trend_engine import (
    OpportunityTrendEngine
)


class WatchlistTrendEngine:

    def analyze(
        self,
        repository,
        symbols: list[str]
    ) -> list[TopMoverResult]:     trend_engine = (
            OpportunityTrendEngine()
        )

        for symbol in symbols:

            history = (
                repository.load_by_symbol(
                    symbol
                )
            )

            if not history:

                continue

            trend_result = (
                trend_engine.analyze(
                    history
                )
            )

            results.append(
                TopMoverResult(
                    symbol=symbol,

                    latest_score=(
                        trend_result.latest_score
                    ),

                    score_change=(
                        trend_result.score_change
                    ),

                    trend=(
                        trend_result.trend
                    )
                )
            )

        results.sort(
            key=lambda item:
                item.score_change,
            reverse=True
        )

        return results
