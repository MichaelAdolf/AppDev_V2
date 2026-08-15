Python
1
from stockmind.infrastructure.history.indicator_chart_data_repository import (
2
IndicatorChartDataRepository
3
)
4
 
5
repo = IndicatorChartDataRepository()
6
 
7
points = repo.load_by_symbol("NVDA")
8
 
9
print(
10
f"Anzahl Punkte: {len(points)}"
11
)
