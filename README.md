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
        "\n=== STOCKMIND DAILY REFRESH ===\n"
    )

    print(
        "\n[1/5] Dashboard Analysen"
    )

    refresh_dashboard()

    print(
        "\n[2/5] Kursdaten"
    )

    refresh_charts()

    print(
        "\n[3/5] Indikatoren"
    )

    refresh_indicators()

    print(
        "\n[4/5] Fundamentaldaten"
    )

    refresh_fundamentals()

    print(
        "\n[5/5] Historische Setups"
    )

    refresh_historical()

    print(
        "\n✅ Daily Refresh erfolgreich abgeschlossen."
    )


if __name__ == "__main__":

    main()
