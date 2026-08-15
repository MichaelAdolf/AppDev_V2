from stockmind.application.dashboard.use_cases.fundamental_dashboard_use_case import (
    FundamentalDashboardUseCase
)


def main():

    result = (
        FundamentalDashboardUseCase()
        .load(
            "NVDA"
        )
    )

    print(result)


if __name__ == "__main__":
    main()
