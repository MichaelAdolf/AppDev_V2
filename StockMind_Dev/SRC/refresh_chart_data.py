import math

import yfinance as yf

from stockmind.domain.history.chart_point import ChartPoint
from stockmind.infrastructure.history.chart_data_repository import ChartDataRepository
from stockmind.infrastructure.watchlists.watchlist_repository import WatchlistRepository


def get_symbols():
    return WatchlistRepository().load_active_symbols()


def _number(value):
    if value is None:
        return None
    try:
        numeric = float(value)
    except (TypeError, ValueError):
        return None
    return numeric if math.isfinite(numeric) else None


def build_chart_points(symbol: str) -> list[ChartPoint]:
    data = yf.Ticker(symbol).history(period="5y").copy()
    if data.empty:
        return []

    data["BB_Middle"] = data["Close"].rolling(window=20).mean()
    data["BB_Std"] = data["Close"].rolling(window=20).std()
    data["BB_Upper"] = data["BB_Middle"] + data["BB_Std"] * 2
    data["BB_Lower"] = data["BB_Middle"] - data["BB_Std"] * 2

    points = []
    for index, row in data.iterrows():
        close_price = _number(row.get("Close"))
        if close_price is None:
            continue
        points.append(ChartPoint(
            symbol=symbol.upper(),
            trading_date=index.date().isoformat(),
            close_price=close_price,
            bollinger_upper=_number(row.get("BB_Upper")),
            bollinger_middle=_number(row.get("BB_Middle")),
            bollinger_lower=_number(row.get("BB_Lower")),
            open_price=_number(row.get("Open")),
            high_price=_number(row.get("High")),
            low_price=_number(row.get("Low")),
        ))
    return points


def main():
    repository = ChartDataRepository()
    for symbol in get_symbols():
        print(f"Refreshing OHLC chart data for {symbol}")
        points = build_chart_points(symbol)
        if not points:
            print(f"Skipping {symbol}: no valid chart data returned")
            continue
        repository.replace_for_symbol(symbol, points)
    print("OHLC chart data refresh complete.")


if __name__ == "__main__":
    main()
