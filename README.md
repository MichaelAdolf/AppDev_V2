from stockmind.application.dashboard.use_cases.alerts_dashboard_use_case import (
    AlertsDashboardUseCase
)


def main():

    alerts = (
        AlertsDashboardUseCase()
        .load(
            "balanced"
        )
    )

    print(
        "\n=== ALERTS ===\n"
    )

    for alert in alerts:

        print(alert)


if __name__ == "__main__":
    main()
