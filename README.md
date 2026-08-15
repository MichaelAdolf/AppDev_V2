from stockmind.infrastructure.history.indicator_chart_data_repository import (
    IndicatorChartDataRepository
)

points = (
    IndicatorChartDataRepository()
    .load_by_symbol(
        "NVDA"
    )
)

first = points[0]

print(type(first))
print(first)

print("adx:", hasattr(first, "adx"))
print("stoch_k:", hasattr(first, "stoch_k"))

print(vars(first))
