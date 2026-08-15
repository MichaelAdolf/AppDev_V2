from stockmind.infrastructure.history.indicator_chart_data_repository import (
    IndicatorChartDataRepository
)

repo = IndicatorChartDataRepository()

points = repo.load_by_symbol("NVDA")

print(
    f"Anzahl Punkte: {len(points)}"
)
