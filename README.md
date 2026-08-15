from stockmind.application.dashboard.models.profile_comparison_result import (
    ProfileComparisonResult,
    ProfileComparisonEntry
)

from stockmind.infrastructure.history.latest_analysis_repository import (
    LatestAnalysisRepository
)


class ProfileComparisonDashboardUseCase:

    def load(
        self,
        symbol: str
    ) -> ProfileComparisonResult:

        profiles = [
            "conservative",
            "balanced",
            "aggressive"
        ]

        entries = []

        repository = (
            LatestAnalysisRepository()
        )

        for profile in profiles:

            analyses = (
                repository.load_all(
                    profile
                )
            )

            stock = next(
                (
                    item
                    for item in analyses
                    if item.symbol == symbol
                ),
                None
            )

            if stock is None:

                continue

            entries.append(
                ProfileComparisonEntry(
                    profile_name=profile,
                    score=stock.opportunity_score,
                    confidence=stock.confidence,
                    signal=stock.signal,
                    risk_level=stock.risk_level
                )
            )

        return ProfileComparisonResult(
            symbol=symbol,
            entries=entries
        )
