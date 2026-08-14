from stockmind.application.dashboard.use_cases.historical_setup_dashboard_use_case import (
    HistoricalSetupDashboardUseCase
)


def main():

    result = (
        HistoricalSetupDashboardUseCase()
        .load(
            "NVDA"
        )
    )

    print(result)


if __name__ == "__main__":
    main()
