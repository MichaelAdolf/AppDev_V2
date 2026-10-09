import logging
from dataclasses import dataclass

from stockmind.application.refresh.bootstrap_stock_use_case import BootstrapStockUseCase
from stockmind.application.refresh.daily_symbol_refresh_use_case import DailySymbolRefreshUseCase
from stockmind.infrastructure.refresh.refresh_state_repository import RefreshStateRepository
from stockmind.infrastructure.history.chart_data_repository import ChartDataRepository
from stockmind.infrastructure.watchlists.watchlist_repository import WatchlistRepository

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class SymbolRefreshResult:
    symbol: str
    mode: str
    success: bool
    error: str | None = None


class RefreshCoordinator:
    def run_daily(self):
        state = RefreshStateRepository()
        chart = ChartDataRepository()
        results = []
        symbols = WatchlistRepository().load_active_symbols()

        logger.info("StockMind refresh started for %d active symbols", len(symbols))

        for position, symbol in enumerate(symbols, start=1):
            has_base = chart.get_latest_date(symbol) is not None
            mode = (
                "incremental"
                if state.is_bootstrapped(symbol) or has_base
                else "bootstrap"
            )

            logger.info(
                "Refresh [%d/%d] symbol=%s mode=%s has_base=%s",
                position,
                len(symbols),
                symbol,
                mode,
                has_base,
            )

            try:
                if mode == "bootstrap":
                    BootstrapStockUseCase().execute(symbol)
                else:
                    DailySymbolRefreshUseCase().execute(symbol)

                state.mark_success(symbol, mode)
                results.append(SymbolRefreshResult(symbol, mode, True))
                logger.info(
                    "Refresh succeeded symbol=%s mode=%s",
                    symbol,
                    mode,
                )

            except Exception as exc:
                state.mark_error(symbol, mode, str(exc))
                results.append(
                    SymbolRefreshResult(
                        symbol=symbol,
                        mode=mode,
                        success=False,
                        error=str(exc),
                    )
                )
                logger.exception(
                    "Refresh failed symbol=%s mode=%s",
                    symbol,
                    mode,
                )
                raise

        logger.info("StockMind refresh completed successfully")
        return results
