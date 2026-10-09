from dataclasses import dataclass
from stockmind.application.refresh.bootstrap_stock_use_case import BootstrapStockUseCase
from stockmind.application.refresh.daily_symbol_refresh_use_case import DailySymbolRefreshUseCase
from stockmind.infrastructure.refresh.refresh_state_repository import RefreshStateRepository
from stockmind.infrastructure.history.chart_data_repository import ChartDataRepository
from stockmind.infrastructure.watchlists.watchlist_repository import WatchlistRepository

@dataclass(frozen=True)
class SymbolRefreshResult:
    symbol:str
    mode:str
    success:bool
    error:str|None=None

class RefreshCoordinator:
    def run_daily(self):
        state=RefreshStateRepository();chart=ChartDataRepository();results=[]
        for symbol in WatchlistRepository().load_active_symbols():
            # Existing installations predate refresh_state; chart history is accepted as bootstrap evidence.
            has_base=chart.get_latest_date(symbol) is not None
            mode="incremental" if state.is_bootstrapped(symbol) or has_base else "bootstrap"
            try:
                if mode=="bootstrap":BootstrapStockUseCase().execute(symbol)
                else:DailySymbolRefreshUseCase().execute(symbol)
                state.mark_success(symbol,mode);results.append(SymbolRefreshResult(symbol,mode,True))
            except Exception as exc:
                state.mark_error(symbol,mode,str(exc));results.append(SymbolRefreshResult(symbol,mode,False,str(exc)))
                raise
        return results
