from dataclasses import asdict
from dataclasses import is_dataclass

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Query

from stockmind.application.dashboard.use_cases.watchlist_dashboard_use_case import (
    WatchlistDashboardUseCase
)

from stockmind.application.dashboard.use_cases.alerts_dashboard_use_case import (
    AlertsDashboardUseCase
)

from stockmind.application.dashboard.use_cases.stock_detail_dashboard_use_case import (
    StockDetailDashboardUseCase
)

from stockmind.application.dashboard.use_cases.profile_comparison_dashboard_use_case import (
    ProfileComparisonDashboardUseCase
)

from stockmind.application.dashboard.use_cases.fundamental_dashboard_use_case import (
    FundamentalDashboardUseCase
)

from stockmind.application.dashboard.use_cases.buy_period_dashboard_use_case import (
    BuyPeriodDashboardUseCase
)

from stockmind.infrastructure.history.latest_analysis_repository import (
    LatestAnalysisRepository
)


app = FastAPI(
    title="StockMind API",
    version="0.1.0",
    description=(
        "Read-only API for StockMind dashboard data, "
        "Home Assistant and Jarvis integrations."
    )
)


def to_json(
    value
):

    if is_dataclass(
        value
    ):

        return asdict(
            value
        )

    if isinstance(
        value,
        list
    ):

        return [
            to_json(
                item
            )
            for item in value
        ]

    if isinstance(
        value,
        dict
    ):

        return {
            key: to_json(
                item
            )
            for key, item in value.items()
        }

    return value


@app.get(
    "/health",
    tags=[
        "System"
    ]
)
def health():

    return {
        "status": "ok",
        "service": "stockmind-api"
    }


@app.get(
    "/profiles",
    tags=[
        "System"
    ]
)
def get_profiles():

    return {
        "profiles": [
            "conservative",
            "balanced",
            "aggressive"
        ]
    }


@app.get(
    "/watchlist/{profile_name}",
    tags=[
        "Watchlist"
    ]
)
def get_watchlist(
    profile_name: str
):

    result = (
        WatchlistDashboardUseCase()
        .load(
            profile_name
        )
    )

    return to_json(
        result
    )


@app.get(
    "/top-opportunities/{profile_name}",
    tags=[
        "Watchlist"
    ]
)
def get_top_opportunities(
    profile_name: str,
    limit: int = Query(
        default=5,
        ge=1,
        le=50
    )
):

    result = (
        WatchlistDashboardUseCase()
        .load(
            profile_name
        )
    )

    stocks = sorted(
        result.stocks,
        key=lambda item:
            item.opportunity_score,
        reverse=True
    )

    top_stocks = stocks[:limit]

    return {
        "profile_name": profile_name,
        "limit": limit,
        "stocks": to_json(
            top_stocks
        )
    }


@app.get(
    "/alerts/{profile_name}",
    tags=[
        "Alerts"
    ]
)
def get_alerts(
    profile_name: str
):

    alerts = (
        AlertsDashboardUseCase()
        .load(
            profile_name
        )
    )

    return {
        "profile_name": profile_name,
        "alerts": to_json(
            alerts
        )
    }


@app.get(
    "/stock/{symbol}",
    tags=[
        "Stock Detail"
    ]
)
def get_stock_detail(
    symbol: str,
    profile_name: str = Query(
        default="balanced"
    )
):

    try:

        result = (
            StockDetailDashboardUseCase()
            .load(
                profile_name=profile_name,
                symbol=symbol.upper()
            )
        )

        return to_json(
            result
        )

    except ValueError as error:

        raise HTTPException(
            status_code=404,
            detail=str(
                error
            )
        )


@app.get(
    "/stock/{symbol}/summary",
    tags=[
        "Stock Detail"
    ]
)
def get_stock_summary(
    symbol: str,
    profile_name: str = Query(
        default="balanced"
    )
):

    try:

        result = (
            StockDetailDashboardUseCase()
            .load(
                profile_name=profile_name,
                symbol=symbol.upper()
            )
        )

        return {
            "symbol": result.symbol,
            "profile_name": profile_name,
            "score": result.score,
            "confidence": result.confidence,
            "historical_success_rate": (
                result.historical_success_rate
            ),
            "risk_level": result.risk_level,
            "signal": result.signal,
            "summary": result.summary,
            "strengths": result.strengths,
            "weaknesses": result.weaknesses
        }

    except ValueError as error:

        raise HTTPException(
            status_code=404,
            detail=str(
                error
            )
        )


@app.get(
    "/stock/{symbol}/fundamentals",
    tags=[
        "Fundamentals"
    ]
)
def get_stock_fundamentals(
    symbol: str
):

    fundamentals = (
        FundamentalDashboardUseCase()
        .load(
            symbol.upper()
        )
    )

    if fundamentals is None:

        raise HTTPException(
            status_code=404,
            detail=(
                f"No fundamental data found for "
                f"{symbol.upper()}."
            )
        )

    return to_json(
        fundamentals
    )


@app.get(
    "/stock/{symbol}/profile-comparison",
    tags=[
        "Stock Detail"
    ]
)
def get_profile_comparison(
    symbol: str
):

    result = (
        ProfileComparisonDashboardUseCase()
        .load(
            symbol.upper()
        )
    )

    return to_json(
        result
    )


@app.get(
    "/stock/{symbol}/buy-periods",
    tags=[
        "Stock Detail"
    ]
)
def get_buy_periods(
    symbol: str,
    max_gap_days: int = Query(
        default=3,
        ge=1,
        le=30
    )
):

    result = (
        BuyPeriodDashboardUseCase()
        .load(
            symbol=symbol.upper(),
            max_gap_days=max_gap_days
        )
    )

    return to_json(
        result
    )


@app.get(
    "/jarvis/daily-briefing",
    tags=[
        "Jarvis"
    ]
)
def get_jarvis_daily_briefing(
    profile_name: str = Query(
        default="balanced"
    ),
    limit: int = Query(
        default=3,
        ge=1,
        le=10
    )
):

    dashboard = (
        WatchlistDashboardUseCase()
        .load(
            profile_name
        )
    )

    stocks = sorted(
        dashboard.stocks,
        key=lambda item:
            item.opportunity_score,
        reverse=True
    )

    top_stocks = stocks[:limit]

    briefing_items = []

    for stock in top_stocks:

        briefing_items.append(
            {
                "symbol": stock.symbol,
                "score": stock.opportunity_score,
                "signal": stock.signal,
                "confidence": stock.confidence,
                "risk_level": stock.risk_level
            }
        )

    return {
        "profile_name": profile_name,
        "message": (
            "Hier sind die aktuell interessantesten "
            "StockMind-Kandidaten."
        ),
        "top_stocks": briefing_items
    }


@app.get(
    "/raw/latest-analysis/{profile_name}",
    tags=[
        "Raw"
    ]
)
def get_raw_latest_analysis(
    profile_name: str
):

    entries = (
        LatestAnalysisRepository()
        .load_all(
            profile_name
        )
    )

    return {
        "profile_name": profile_name,
        "entries": to_json(
            entries
        )
    }
