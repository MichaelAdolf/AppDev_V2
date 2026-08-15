from stockmind.application.dashboard.use_cases.buy_period_dashboard_use_case import (
    BuyPeriodDashboardUseCase
)


def main():

    result = (
        BuyPeriodDashboardUseCase()
        .load(
            symbol="NVDA",
            max_gap_days=10
        )
    )

    print(
        "\n=== BUY PERIOD DASHBOARD ===\n"
    )

    print(result)

    print(
        f"\nPerioden: {result.period_count}"
    )

    print(
        f"Trefferquote: {result.overall_success_rate:.1f}%"
    )

    print(
        "\nErste Perioden:"
    )

    for period in result.periods[:5]:

        print(period)


if __name__ == "__main__":
    main()
