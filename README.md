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

    print("\n=== STOCK DETAIL DASHBOARD ===\n")

    print(result)

    print("\nSummary:")
    print(result.summary)

    print("\nStrengths:")
    print(result.strengths)

    print("\nWeaknesses:")
    print(result.weaknesses)

    print("\nHistorical Setup Stats:")
    print(
        f"Setup Count: {result.setup_count}"
    )
    print(
        f"Success Rate: {result.setup_success_rate:.1f}%"
    )
    print(
        f"Average Days: {result.average_setup_days:.1f}"
    )
    print(
        f"Average Gain: {result.average_setup_gain:.1f}%"
    )
    print(
        f"Average Drawdown: {result.average_setup_drawdown:.1f}%"
    )


if __name__ == "__main__":
    main()
