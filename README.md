from stockmind.application.dashboard.use_cases.stock_detail_dashboard_use_case import (
    StockDetailDashboardUseCase
)


def main():

    result = (
        StockDetailDashboardUseCase()
        .load(
            profile_name="balanced",
            symbol="NVDA"
        )
    )

    print(result)


if __name__ == "__main__":
    main()
