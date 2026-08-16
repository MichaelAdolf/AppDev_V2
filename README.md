from scripts.refresh_dashboard_data import (
    main as refresh_dashboard
)

from scripts.refresh_chart_data import (
    main as refresh_charts
)

from scripts.refresh_indicator_chart_data import (
    main as refresh_indicators
)

from scripts.refresh_fundamental_data import (
    main as refresh_fundamentals
)

from scripts.refresh_historical_setups import (
    main as refresh_historical
)


def main():

    print(
        "\n================================="
    )

    print(
        " STOCKMIND DAILY REFRESH START"
    )

    print(
        "=================================\n"
    )

    print(
        "[1/5] Refresh Dashboard Analysen"
    )

    refresh_dashboard()

    print(
        "\n[2/5] Refresh Chart Daten"
    )

    refresh_charts()

    print(
        "\n[3/5] Refresh Indikatoren"
    )

    refresh_indicators()

    print(
        "\n[4/5] Refresh Fundamentaldaten"
    )

    refresh_fundamentals()

    print(
        "\n[5/5] Refresh Historical Setups"
    )

    refresh_historical()

    print(
        "\n================================="
    )

    print(
        " STOCKMIND DAILY REFRESH DONE"
    )

    print(
        "=================================\n"
    )


if __name__ == "__main__":

    main()
