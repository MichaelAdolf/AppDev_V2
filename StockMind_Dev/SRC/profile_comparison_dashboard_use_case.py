from stockmind.application.dashboard.models.profile_comparison_result import (
    ProfileComparisonEntry,
    ProfileComparisonResult,
)
from stockmind.application.dashboard.use_cases.buy_period_dashboard_use_case import (
    BuyPeriodDashboardUseCase,
)
from stockmind.infrastructure.history.daily_buy_signal_repository import (
    DailyBuySignalRepository,
)
from stockmind.infrastructure.history.latest_analysis_repository import (
    LatestAnalysisRepository,
)


class ProfileComparisonDashboardUseCase:
    PROFILES = ["conservative", "balanced", "aggressive"]

    def load(
        self,
        symbol: str,
        analysis_period: str = "5y",
        max_gap_days: int = 3,
    ) -> ProfileComparisonResult:
        symbol = symbol.upper()
        entries = []
        analysis_repository = LatestAnalysisRepository()
        signal_repository = DailyBuySignalRepository()
        period_use_case = BuyPeriodDashboardUseCase()

        for profile_name in self.PROFILES:
            analyses = analysis_repository.load_all(profile_name)
            stock = next(
                (item for item in analyses if item.symbol == symbol),
                None,
            )
            if stock is None:
                continue

            latest_signal = signal_repository.load_latest(
                symbol=symbol,
                profile_name=profile_name,
                analysis_period=analysis_period,
            )
            period_result = period_use_case.load(
                symbol=symbol,
                profile_name=profile_name,
                analysis_period=analysis_period,
                max_gap_days=max_gap_days,
            )
            active_period = period_result.active_period
            statistics = period_result.statistics

            entries.append(
                ProfileComparisonEntry(
                    profile_name=profile_name,
                    score=stock.opportunity_score,
                    confidence=stock.confidence,
                    signal=stock.signal,
                    risk_level=stock.risk_level,
                    current_buy_signal=(
                        latest_signal.is_buy if latest_signal else None
                    ),
                    active_period_start=(
                        active_period.start_date if active_period else None
                    ),
                    active_period_duration_days=(
                        active_period.calendar_duration_days
                        if active_period else None
                    ),
                    period_count=period_result.period_count,
                    complete_period_count=statistics.complete_period_count,
                    incomplete_period_count=statistics.incomplete_period_count,
                    target_hit_rate=statistics.target_hit_rate,
                    below_target_rate=statistics.below_target_rate,
                    flat_rate=statistics.flat_rate,
                    negative_rate=statistics.negative_rate,
                )
            )

        return ProfileComparisonResult(
            symbol=symbol,
            analysis_period=analysis_period,
            entries=entries,
        )
