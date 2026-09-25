from datetime import date

from stockmind.application.dashboard.models.buy_period_dashboard_result import (
    BuyPeriodDashboardResult,
    BuyPeriodStatistics,
)
from stockmind.domain.history.historical_outcome import HistoricalOutcome
from stockmind.infrastructure.history.buy_period_repository import BuyPeriodRepository


class BuyPeriodDashboardUseCase:
    def load(
        self,
        symbol: str,
        profile_name: str = "balanced",
        analysis_period: str = "5y",
        max_gap_days: int = 3,
    ) -> BuyPeriodDashboardResult:
        periods = BuyPeriodRepository().load_by_symbol(
            symbol=symbol,
            profile_name=profile_name,
            analysis_period=analysis_period,
        )
        complete = [period for period in periods if period.is_complete]
        incomplete = [period for period in periods if not period.is_complete]
        count = lambda outcome: sum(
            1 for period in complete if period.outcome == outcome.value
        )
        target_hit_count = count(HistoricalOutcome.TARGET_HIT)
        below_target_count = count(HistoricalOutcome.BELOW_TARGET)
        flat_count = count(HistoricalOutcome.FLAT)
        negative_count = count(HistoricalOutcome.NEGATIVE)
        complete_count = len(complete)

        statistics = BuyPeriodStatistics(
            complete_period_count=complete_count,
            incomplete_period_count=len(incomplete),
            target_hit_count=target_hit_count,
            below_target_count=below_target_count,
            flat_count=flat_count,
            negative_count=negative_count,
            target_hit_rate=self._rate(target_hit_count, complete_count),
            below_target_rate=self._rate(below_target_count, complete_count),
            flat_rate=self._rate(flat_count, complete_count),
            negative_rate=self._rate(negative_count, complete_count),
            average_days_to_target=self._average([
                period.days_to_target
                for period in complete
                if period.days_to_target is not None
            ]),
            average_calendar_duration_days=self._average([
                period.calendar_duration_days for period in periods
            ]),
            average_buy_signal_count=self._average([
                period.buy_signal_count for period in periods
            ]),
            average_max_gain_pct=self._average([
                period.max_gain_pct
                for period in complete
                if period.max_gain_pct is not None
            ]),
            average_max_drawdown_pct=self._average([
                period.max_drawdown_pct
                for period in complete
                if period.max_drawdown_pct is not None
            ]),
        )

        active_period = self._active_period(periods, max_gap_days)
        return BuyPeriodDashboardResult(
            symbol=symbol.upper(),
            profile_name=profile_name,
            analysis_period=analysis_period,
            max_gap_days=max_gap_days,
            period_count=len(periods),
            statistics=statistics,
            active_period=active_period,
            periods=periods,
        )

    def _active_period(self, periods, max_gap_days):
        if not periods:
            return None
        latest = max(periods, key=lambda item: item.end_date)
        calendar_gap = (date.today() - date.fromisoformat(latest.end_date)).days - 1
        return latest if calendar_gap <= max_gap_days else None

    def _rate(self, count, total):
        return count / total if total else 0.0

    def _average(self, values):
        return sum(values) / len(values) if values else 0.0
