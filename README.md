from stockmind.application.dashboard.use_cases.watchlist_dashboard_use_case import (
    WatchlistDashboardUseCase
)


def main():

    result = (
        WatchlistDashboardUseCase()
        .load(
            "balanced"
        )
    )

    print(result)


if __name__ == "__main__":
    main()
