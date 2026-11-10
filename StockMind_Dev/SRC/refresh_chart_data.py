import yfinance as yf

from stockmind.domain.history.chart_point import ChartPoint
from stockmind.infrastructure.history.chart_data_repository import ChartDataRepository
from stockmind.infrastructure.watchlists.watchlist_repository import WatchlistRepository


def get_symbols():
    return WatchlistRepository().load_active_symbols()


def _number(value):
    return None if value != value else float(value)


def build_chart_points(symbol: str) -> list[ChartPoint]:
    data = yf.Ticker(symbol).history(period="5y").copy()
    if data.empty:
        return []
    data["BB_Middle"] = data["Close"].rolling(window=20).mean()
    data["BB_Std"] = data["Close"].rolling(window=20).std()
    data["BB_Upper"] = data["BB_Middle"] + data["BB_Std"] * 2
    data["BB_Lower"] = data["BB_Middle"] - data["BB_Std"] * 2
    return [ChartPoint(
        symbol=symbol.upper(),
        trading_date=index.date().isoformat(),
        close_price=float(row["Close"]),
        bollinger_upper=_number(row["BB_Upper"]),
        bollinger_middle=_number(row["BB_Middle"]),
        bollinger_lower=_number(row["BB_Lower"]),
        open_price=_number(row["Open"]),
        high_price=_number(row["High"]),
        low_price=_number(row["Low"]),
    ) for index, row in data.iterrows()]


def main():
    repository = ChartDataRepository()
    for symbol in get_symbols():
        print(f"Refreshing OHLC chart data for {symbol}")
        repository.replace_for_symbol(symbol, build_chart_points(symbol))
    print("OHLC chart data refresh complete.")


if __name__ == "__main__":
    main()
