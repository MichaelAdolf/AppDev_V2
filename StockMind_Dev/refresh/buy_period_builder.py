from datetime import date

from stockmind.domain.history.buy_period_entry import BuyPeriodEntry
from stockmind.domain.history.daily_buy_signal import DailyBuySignal
from stockmind.domain.history.historical_outcome import HistoricalOutcome
from stockmind.domain.history.historical_setup_entry import HistoricalSetupEntry


class BuyPeriodBuilder:
    def build(
        self,
        signals: list[DailyBuySignal],
        setups: list[HistoricalSetupEntry],
        max_gap_days: int = 3,
        target_pct: float = 0.08,
    ) -> list[BuyPeriodEntry]:
        if max_gap_days < 0:
            raise ValueError("max_gap_days must not be negative")

        buy_signals = sorted(
            (signal for signal in signals if signal.is_buy),
            key=lambda item: item.trading_date,
        )
        if not buy_signals:
            return []

        setup_by_date = {setup.setup_date: setup for setup in setups}
        clusters: list[list[DailyBuySignal]] = []
        current_cluster = [buy_signals[0]]

        for signal in buy_signals[1:]:
            previous = current_cluster[-1]
            calendar_gap = (
                date.fromisoformat(signal.trading_date)
                - date.fromisoformat(previous.trading_date)
            ).days - 1
            if calendar_gap <= max_gap_days:
                current_cluster.append(signal)
            else:
                clusters.append(current_cluster)
                current_cluster = [signal]
        clusters.append(current_cluster)

        return [
            self._build_period(
                cluster=cluster,
                setup_by_date=setup_by_date,
                target_pct=target_pct,
            )
            for cluster in clusters
        ]

    def _build_period(
        self,
        cluster: list[DailyBuySignal],
        setup_by_date: dict[str, HistoricalSetupEntry],
        target_pct: float,
    ) -> BuyPeriodEntry:
        first = cluster[0]
        start = date.fromisoformat(first.trading_date)
        end = date.fromisoformat(cluster[-1].trading_date)
        gaps = []
        for previous, current in zip(cluster, cluster[1:]):
            gap = (
                date.fromisoformat(current.trading_date)
                - date.fromisoformat(previous.trading_date)
            ).days - 1
            gaps.append(max(gap, 0))

        setup = setup_by_date.get(first.trading_date)
        if setup is None:
            outcome = HistoricalOutcome.INCOMPLETE_WINDOW.value
            target_hit = False
            days_to_target = None
            window_end_date = None
            window_end_return_pct = None
            max_gain_pct = None
            max_drawdown_pct = None
            is_complete = False
        else:
            outcome = setup.outcome
            target_hit = setup.success
            days_to_target = setup.days_to_target
            window_end_date = setup.window_end_date
            window_end_return_pct = setup.window_end_return_pct
            max_gain_pct = setup.max_gain_pct
            max_drawdown_pct = setup.max_drawdown_pct
            is_complete = setup.is_complete

        return BuyPeriodEntry(
            symbol=first.symbol,
            profile_name=first.profile_name,
            analysis_period=first.analysis_period,
            start_date=first.trading_date,
            end_date=cluster[-1].trading_date,
            calendar_duration_days=(end - start).days + 1,
            buy_signal_count=len(cluster),
            gap_days_total=sum(gaps),
            largest_gap_days=max(gaps, default=0),
            entry_price=first.entry_price,
            target_pct=target_pct,
            outcome=outcome,
            target_hit=target_hit,
            days_to_target=days_to_target,
            window_end_date=window_end_date,
            window_end_return_pct=window_end_return_pct,
            max_gain_pct=max_gain_pct,
            max_drawdown_pct=max_drawdown_pct,
            is_complete=is_complete,
        )
