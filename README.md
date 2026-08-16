from stockmind.application.dashboard.use_cases.historical_setup_dashboard_use_case import (
    HistoricalSetupDashboardUseCase
)


def main():

    result = (
        HistoricalSetupDashboardUseCase()
        .load(
            symbol="NVDA",
            profile_name="balanced",
            analysis_period="1y"
        )
    )

    print(
        "\n=== HISTORICAL SETUP DASHBOARD ===\n"
    )

    print(
        f"Setup Count: {result.setup_count}"
    )

    print(
        f"Successful: {result.successful_count}"
    )

    print(
        f"Failed: {result.failed_count}"
    )

    print(
        f"Success Rate: {result.success_rate:.1f}%"
    )

    print(
        f"Average Days: {result.average_days:.1f}"
    )

    print(
        f"Average Gain: {result.average_gain:.1f}%"
    )

    print(
        f"Average Drawdown: {result.average_drawdown:.1f}%"
    )

    print(
        "\nFirst setups:"
    )

    for setup in result.setups[:5]:

        print(setup)


if __name__ == "__main__":

    main()
