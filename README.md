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

    print(
        f"Found {len(points)} indicator chart points"
    )

    for point in points[:5]:

        print(point)


if __name__ == "__main__":
    main()
