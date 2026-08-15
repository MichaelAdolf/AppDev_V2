from stockmind.infrastructure.history.indicator_chart_data_repository import (
    IndicatorChartDataRepository
)


def main():

    points = (
        IndicatorChartDataRepository()
        .load_by_symbol(
            "NVDA"
        )
    )

    first = points[0]

    print(first)

    print(hasattr(first, "adx"))
    print(hasattr(first, "stoch_k"))


if __name__ == "__main__":
    main()
