from stockmind.application.dashboard.use_cases.buy_period_dashboard_use_case import (
    BuyPeriodDashboardUseCase
)


def main():

    result = (
        BuyPeriodDashboardUseCase()
        .load(
            symbol="NVDA",
            profile_name="balanced",
            analysis_period="5y",
            max_gap_days=3
        )
    )

    print(
        "\n=== BUY PERIOD DASHBOARD ===\n"
    )

    print(
        f"Symbol: {result.symbol}"
    )

    print(
        f"Period Count: {result.period_count}"
    )

    print(
        f"Successful Periods: {result.successful_period_count}"
    )

    print(
        f"Failed Periods: {result.failed_period_count}"
    )

    print(
        f"Overall Success Rate: {result.overall_success_rate:.1f}%"
    )

    print(
        f"Average Days: {result.average_days_to_target:.1f}"
    )

    print(
        f"Average Max Gain: {result.average_max_gain_pct:.1f}%"
    )

    print(
        f"Average Max Drawdown: {result.average_max_drawdown_pct:.1f}%"
    )

    print(
        "\nFirst periods:"
    )

    for period in result.periods[:10]:

        print(period)


if __name__ == "__main__":

    main()
