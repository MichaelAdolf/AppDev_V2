from stockmind.application.dashboard.use_cases.buy_period_dashboard_use_case import (
    BuyPeriodDashboardUseCase,
)
from stockmind.domain.historical_success.historical_evidence_result import (
    HistoricalEvidenceResult,
)


class HistoricalEvidenceService:
    def build(
        self,
        symbol: str,
        profile_name: str,
        setup_result,
        analysis_period: str = "5y",
        max_gap_days: int = 3,
    ) -> HistoricalEvidenceResult:
        period_result = BuyPeriodDashboardUseCase().load(
            symbol=symbol,
            profile_name=profile_name,
            analysis_period=analysis_period,
            max_gap_days=max_gap_days,
        )
        statistics = period_result.statistics
        active_period = period_result.active_period

        if statistics.complete_period_count > 0:
            return HistoricalEvidenceResult(
                success_rate=statistics.target_hit_rate,
                sample_quality=self._sample_quality(
                    statistics.complete_period_count
                ),
                source="BUY_PERIODS",
                sample_count=statistics.complete_period_count,
                target_hit_rate=statistics.target_hit_rate,
                below_target_rate=statistics.below_target_rate,
                flat_rate=statistics.flat_rate,
                negative_rate=statistics.negative_rate,
                incomplete_count=statistics.incomplete_period_count,
                average_similarity=None,
                active_period_start=(
                    active_period.start_date if active_period else None
                ),
                active_period_duration_days=(
                    active_period.calendar_duration_days
                    if active_period else None
                ),
                active_period_buy_signal_count=(
                    active_period.buy_signal_count if active_period else None
                ),
            )

        return HistoricalEvidenceResult(
            success_rate=setup_result.success_rate,
            sample_quality=setup_result.sample_quality,
            source="SETUP_FALLBACK",
            sample_count=setup_result.complete_count,
            target_hit_rate=setup_result.target_hit_rate,
            below_target_rate=setup_result.below_target_rate,
            flat_rate=setup_result.flat_rate,
            negative_rate=setup_result.negative_rate,
            incomplete_count=setup_result.incomplete_count,
            average_similarity=setup_result.average_similarity,
            active_period_start=(
                active_period.start_date if active_period else None
            ),
            active_period_duration_days=(
                active_period.calendar_duration_days
                if active_period else None
            ),
            active_period_buy_signal_count=(
                active_period.buy_signal_count if active_period else None
            ),
        )

    def _sample_quality(self, sample_count: int) -> str:
        if sample_count >= 50:
            return "HIGH"
        if sample_count >= 20:
            return "MEDIUM"
        if sample_count > 0:
            return "LOW"
        return "NO_SAMPLE"
