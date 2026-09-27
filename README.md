from stockmind.application.dashboard.models.historical_setup_dashboard_result import (
    HistoricalSetupDashboardResult,
)
from stockmind.infrastructure.history.historical_setup_repository import (
    HistoricalSetupRepository,
)


class HistoricalSetupDashboardUseCase:
    def load(
        self,
        symbol: str,
        profile_name: str = "balanced",
        analysis_period: str = "5y",
    ) -> HistoricalSetupDashboardResult:
        setups = HistoricalSetupRepository().load_by_symbol(
            symbol=symbol,
            profile_name=profile_name,
            analysis_period=analysis_period,
        )

        if not setups:
            return HistoricalSetupDashboardResult(
                setup_count=0,
                successful_count=0,
                failed_count=0,
                success_rate=0.0,
                average_days=0.0,
                average_gain=0.0,
                average_drawdown=0.0,
                setups=[],
            )

        successful_count = len([
            setup
            for setup in setups
            if setup.success
        ])

        failed_count = len(setups) - successful_count

        success_rate = (
            successful_count
            / len(setups)
            * 100
        )

        valid_days = [
            setup.days_to_target
            for setup in setups
            if setup.days_to_target is not None
        ]

        average_days = (
            sum(valid_days) / len(valid_days)
            if valid_days
            else 0.0
        )

        # Incomplete historical windows can legitimately have no max-gain value.
        # Missing values are excluded instead of being interpreted as 0 percent.
        valid_gains = [
            setup.max_gain_pct
            for setup in setups
            if setup.max_gain_pct is not None
        ]

        average_gain = (
            sum(valid_gains) / len(valid_gains)
            if valid_gains
            else 0.0
        )

        # The same applies to max drawdown: None means not yet evaluable,
        # not a drawdown of 0 percent.
        valid_drawdowns = [
            setup.max_drawdown_pct
            for setup in setups
            if setup.max_drawdown_pct is not None
        ]

        average_drawdown = (
            sum(valid_drawdowns) / len(valid_drawdowns)
            if valid_drawdowns
            else 0.0
        )

        return HistoricalSetupDashboardResult(
            setup_count=len(setups),
            successful_count=successful_count,
            failed_count=failed_count,
            success_rate=success_rate,
            average_days=average_days,
            average_gain=average_gain,
            average_drawdown=average_drawdown,
            setups=setups,
        )
