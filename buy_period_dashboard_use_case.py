from datetime import datetime

from stockmind.application.dashboard.models.buy_period_dashboard_result import (
    BuyPeriodDashboardResult,
    BuyPeriodEntry
)

from stockmind.infrastructure.history.historical_setup_repository import (
    HistoricalSetupRepository
)


class BuyPeriodDashboardUseCase:

    def load(
        self,
        symbol: str,
        max_gap_days: int = 10
    ) -> BuyPeriodDashboardResult:

        setups = (
            HistoricalSetupRepository()
            .load_by_symbol(
                symbol
            )
        )

        if not setups:

            return BuyPeriodDashboardResult(
                symbol=symbol,
                period_count=0,
                successful_period_count=0,
                failed_period_count=0,
                mixed_period_count=0,
                overall_success_rate=0.0,
                average_days_to_target=0.0,
                average_max_gain_pct=0.0,
                average_max_drawdown_pct=0.0,
                periods=[]
            )

        sorted_setups = sorted(
            setups,
            key=lambda item:
                item.setup_date
        )

        clusters = self._cluster_setups(
            sorted_setups=sorted_setups,
            max_gap_days=max_gap_days
        )

        periods = [
            self._build_period_entry(
                cluster
            )
            for cluster in clusters
        ]

        successful_period_count = len(
            [
                p
                for p in periods
                if p.status == "SUCCESSFUL"
            ]
        )

        failed_period_count = len(
            [
                p
                for p in periods
                if p.status == "FAILED"
            ]
        )

        mixed_period_count = len(
            [
                p
                for p in periods
                if p.status == "MIXED"
            ]
        )

        total_setups = sum(
            p.setup_count
            for p in periods
        )

        total_successful = sum(
            p.successful_count
            for p in periods
        )

        overall_success_rate = (
            total_successful
            / total_setups
            * 100
            if total_setups > 0
            else 0.0
        )

        average_days = self._average(
            [
                p.average_days_to_target
                for p in periods
                if p.average_days_to_target > 0
            ]
        )

        average_gain = self._average(
            [
                p.max_gain_pct
                for p in periods
            ]
        )

        average_drawdown = self._average(
            [
                p.max_drawdown_pct
                for p in periods
            ]
        )

        return BuyPeriodDashboardResult(
            symbol=symbol,
            period_count=len(periods),
            successful_period_count=successful_period_count,
            failed_period_count=failed_period_count,
            mixed_period_count=mixed_period_count,
            overall_success_rate=overall_success_rate,
            average_days_to_target=average_days,
            average_max_gain_pct=average_gain,
            average_max_drawdown_pct=average_drawdown,
            periods=periods
        )

    def _cluster_setups(
        self,
        sorted_setups,
        max_gap_days: int
    ) -> list:
        clusters = []

        current_cluster = []

        previous_date = None

        for setup in sorted_setups:

            setup_date = datetime.fromisoformat(
                setup.setup_date
            ).date()

            if previous_date is None:

                current_cluster.append(
                    setup
                )

            else:

                gap = (
                    setup_date
                    - previous_date
                ).days

                if gap <= max_gap_days:

                    current_cluster.append(
                        setup
                    )

                else:

                    clusters.append(
                        current_cluster
                    )

                    current_cluster = [
                        setup
                    ]

            previous_date = setup_date

        if current_cluster:

            clusters.append(
                current_cluster
            )

        return clusters

    def _build_period_entry(
        self,
        cluster
    ) -> BuyPeriodEntry:

        start_date = cluster[0].setup_date

        end_date = cluster[-1].setup_date

        setup_count = len(
            cluster
        )

        successful_count = len(
            [
                setup
                for setup in cluster
                if setup.success
            ]
        )

        failed_count = (
            setup_count
            - successful_count
        )

        success_rate = (
            successful_count
            / setup_count
            * 100
            if setup_count > 0
            else 0.0
        )

        days_values = [
            setup.days_to_target
            for setup in cluster
            if setup.days_to_target is not None
        ]

        average_days = self._average(
            days_values
        )

        max_gain_pct = max(
            [
                setup.max_gain_pct
                for setup in cluster
            ]
        )

        max_drawdown_pct = min(
            [
                setup.max_drawdown_pct
                for setup in cluster
            ]
        )

        status = self._determine_status(
            successful_count=successful_count,
            failed_count=failed_count
        )

        return BuyPeriodEntry(
            start_date=start_date,
            end_date=end_date,
            setup_count=setup_count,
            successful_count=successful_count,
            failed_count=failed_count,
            success_rate=success_rate,
            average_days_to_target=average_days,
            max_gain_pct=max_gain_pct,
            max_drawdown_pct=max_drawdown_pct,
            status=status
        )

    def _determine_status(
        self,
        successful_count: int,
        failed_count: int
    ) -> str:

        total = (
            successful_count
            + failed_count
        )

        if total == 0:
            return "FAILED"

        success_rate = (
            successful_count
            / total
            *100
        )

        if success_rate >= 50:
            return "SUCCESSFULL"

        return "FAILED"

    def _average(
        self,
        values
    ) -> float:

        if not values:

            return 0.0

        return (
            sum(values)
            / len(values)
        )