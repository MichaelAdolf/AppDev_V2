from stockmind.domain.history.buy_period_builder import BuyPeriodBuilder
from stockmind.infrastructure.history.buy_period_repository import BuyPeriodRepository
from stockmind.infrastructure.history.daily_buy_signal_repository import DailyBuySignalRepository
from stockmind.infrastructure.history.historical_setup_repository import HistoricalSetupRepository


class RefreshBuyPeriodsUseCase:
    def execute(
        self,
        symbol: str,
        profile_name: str,
        analysis_period: str,
        max_gap_days: int = 3,
        target_pct: float = 0.08,
    ):
        signals = DailyBuySignalRepository().load_by_symbol(
            symbol=symbol,
            profile_name=profile_name,
            analysis_period=analysis_period,
            buy_only=True,
        )
        setups = HistoricalSetupRepository().load_by_symbol(
            symbol=symbol,
            profile_name=profile_name,
            analysis_period=analysis_period,
        )
        periods = BuyPeriodBuilder().build(
            signals=signals,
            setups=setups,
            max_gap_days=max_gap_days,
            target_pct=target_pct,
        )
        BuyPeriodRepository().replace_for(
            symbol=symbol,
            profile_name=profile_name,
            analysis_period=analysis_period,
            periods=periods,
        )
        return periods
