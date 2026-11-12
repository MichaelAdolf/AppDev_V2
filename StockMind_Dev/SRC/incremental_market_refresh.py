import yfinance as yf
from stockmind.infrastructure.history.chart_data_repository import ChartDataRepository
from stockmind.infrastructure.history.indicator_chart_data_repository import IndicatorChartDataRepository

try:
    from scripts.refresh_chart_data import build_chart_points
    from scripts.refresh_indicator_chart_data import build_indicator_points

except ModuleNotFoundError:
    from refresh_chart_data import build_chart_points
    from refresh_indicator_chart_data import build_indicator_points


def refresh_symbol(symbol: str, full: bool = False):
    chart_repo=ChartDataRepository(); indicator_repo=IndicatorChartDataRepository()
    if full or chart_repo.get_latest_date(symbol) is None:
        chart_repo.replace_for_symbol(symbol, build_chart_points(symbol))
        indicator_repo.replace_for_symbol(symbol, build_indicator_points(symbol))
        return
    latest=chart_repo.get_latest_date(symbol)
    # Existing builder retains exact indicator formulas; obtain 5y then persist only rows after latest.
    # This minimizes DB writes while keeping indicator continuity identical to the validated implementation.
    chart_points=[p for p in build_chart_points(symbol) if p.trading_date > latest]
    indicator_points=[p for p in build_indicator_points(symbol) if p.trading_date > latest]
    chart_repo.upsert_points(chart_points)
    indicator_repo.upsert_points(indicator_points)
