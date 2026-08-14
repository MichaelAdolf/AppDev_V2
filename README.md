from stockmind.infrastructure.history.chart_data_repository import (
    ChartDataRepository
)


def main():

    points = (
        ChartDataRepository()
        .load_by_symbol(
            "NVDA"
        )
    )

    print(
        f"Found {len(points)} chart points"
    )

    for point in points[:5]:

        print(point)


if __name__ == "__main__":
    main()
