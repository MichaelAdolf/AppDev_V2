from stockmind.application.refresh.incremental_market_refresh import refresh_symbol
from stockmind.application.refresh.true_incremental_symbol_refresh_use_case import TrueIncrementalSymbolRefreshUseCase


class DailySymbolRefreshUseCase:
    def execute(self, symbol: str):
        symbol=symbol.upper().strip()
        refresh_symbol(symbol, full=False)
        TrueIncrementalSymbolRefreshUseCase().execute(symbol)
