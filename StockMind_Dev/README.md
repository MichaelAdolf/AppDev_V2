from datetime import datetime

from refresh_dashboard_data import main as refresh_dashboard
from refresh_chart_data import main as refresh_charts
from refresh_indicator_chart_data import main as refresh_indicators
from refresh_fundamental_data import main as refresh_fundamentals
from refresh_historical_setups import main as refresh_historical
from refresh_historical_opportunities import main as refresh_historical_opportunities


def _run_step(step_number: int, step_count: int, title: str, refresh_function):
    print(f"\n[{step_number}/{step_count}] {title}")
    print("---------------------------------")
    refresh_function()
    print(f"[OK] {title}")


def main():
    started_at = datetime.now()
    steps = [
        (
            "Refresh Dashboard Analysen",
            refresh_dashboard,
        ),
        (
            "Refresh Chart Daten (5 Jahre)",
            refresh_charts,
        ),
        (
            "Refresh Indikator-Chart-Daten",
            refresh_indicators,
        ),
        (
            "Refresh Fundamentaldaten",
            refresh_fundamentals,
        ),
        (
            "Refresh Historical Setups und BUY-Perioden",
            refresh_historical,
        ),
        (
            "Refresh Historical Opportunity Replay",
            refresh_historical_opportunities,
        ),
    ]

    print("\n=================================")
    print(" STOCKMIND FULL REFRESH START")
    print("=================================")
    print(f"Start: {started_at.isoformat(timespec='seconds')}")

    for step_number, (title, refresh_function) in enumerate(steps, start=1):
        _run_step(
            step_number=step_number,
            step_count=len(steps),
            title=title,
            refresh_function=refresh_function,
        )

    finished_at = datetime.now()
    duration = finished_at - started_at

    print("\n=================================")
    print(" STOCKMIND FULL REFRESH DONE")
    print("=================================")
    print(f"Ende: {finished_at.isoformat(timespec='seconds')}")
    print(f"Dauer: {duration}")
    print("=================================\n")


if __name__ == "__main__":
    main()
