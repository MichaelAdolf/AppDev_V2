from stockmind.application.dashboard.use_cases.profile_comparison_dashboard_use_case import (
    ProfileComparisonDashboardUseCase
)


def main():

    result = (
        ProfileComparisonDashboardUseCase()
        .load(
            symbol="NVDA"
        )
    )

    print(result)


if __name__ == "__main__":
    main()
