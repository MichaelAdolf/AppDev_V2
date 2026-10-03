from stockmind.application.refresh.refresh_coordinator import RefreshCoordinator
from stockmind.application.jarvis.query_service import JarvisQueryService
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

from stockmind.application.watchlists.add_stock_use_case import (
    AddStockUseCase
)

from stockmind.application.watchlists.remove_stock_use_case import (
    RemoveStockUseCase
)

from stockmind.infrastructure.watchlists.watchlist_repository import (
    WatchlistRepository
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
            "weaknesses": result.weaknesses,
            "historical_source": result.historical_source,
            "active_buy_period": to_json(result.active_buy_period),
            "buy_period_count": result.buy_period_count,
            "complete_buy_period_count": result.complete_buy_period_count,
            "period_target_hit_rate": result.period_target_hit_rate,
            "period_below_target_rate": result.period_below_target_rate,
            "period_flat_rate": result.period_flat_rate,
            "period_negative_rate": result.period_negative_rate
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
    profile_name: str = Query(default="balanced"),
    analysis_period: str = Query(default="5y"),
    max_gap_days: int = Query(default=3, ge=0, le=30),
):
    result = BuyPeriodDashboardUseCase().load(
        symbol=symbol.upper(),
        profile_name=profile_name,
        analysis_period=analysis_period,
        max_gap_days=max_gap_days,
    )
    return to_json(result)


@app.get(
    "/stock/{symbol}/buy-periods/profile-comparison",
    tags=[
        "Stock Detail"
    ]
)
def get_buy_period_profile_comparison(
    symbol: str,
    analysis_period: str = Query(default="5y"),
    max_gap_days: int = Query(default=3, ge=0, le=30),
):
    result = ProfileComparisonDashboardUseCase().load(
        symbol=symbol.upper(),
        analysis_period=analysis_period,
        max_gap_days=max_gap_days,
    )
    return to_json(result)


@app.get("/jarvis/watchlist-summary", tags=["Jarvis"])
def jarvis_watchlist_summary(profile_name: str = Query(default="balanced")):
    return to_json(JarvisQueryService().watchlist(profile_name))

@app.get("/jarvis/top-opportunities", tags=["Jarvis"])
def jarvis_top_opportunities(profile_name: str = Query(default="balanced"), limit: int = Query(default=3, ge=1, le=10)):
    return to_json(JarvisQueryService().top_opportunities(profile_name,limit))

@app.get("/jarvis/daily-changes", tags=["Jarvis"])
def jarvis_daily_changes(profile_name: str = Query(default="balanced")):
    return to_json(JarvisQueryService().daily_changes(profile_name))

@app.get("/jarvis/morning-briefing", tags=["Jarvis"])
def jarvis_morning_briefing(profile_name: str = Query(default="balanced"), limit: int = Query(default=3, ge=1, le=5)):
    return to_json(JarvisQueryService().morning_briefing(profile_name,limit))

@app.get("/jarvis/stock-analysis/{symbol}", tags=["Jarvis"])
def jarvis_stock_analysis(symbol: str, profile_name: str = Query(default="balanced")):
    try:return to_json(JarvisQueryService().stock_analysis(symbol,profile_name))
    except ValueError as error:raise HTTPException(status_code=404,detail=str(error))

@app.get("/jarvis/buy-period/{symbol}", tags=["Jarvis"])
def jarvis_buy_period(symbol: str, profile_name: str = Query(default="balanced")):
    return to_json(JarvisQueryService().buy_period(symbol,profile_name))

@app.get("/jarvis/historical-quality/{symbol}", tags=["Jarvis"])
def jarvis_historical_quality(symbol: str, profile_name: str = Query(default="balanced")):
    return to_json(JarvisQueryService().historical_quality(symbol,profile_name))

@app.get("/jarvis/profile-comparison/{symbol}", tags=["Jarvis"])
def jarvis_profile_comparison(symbol: str):
    return to_json(JarvisQueryService().profiles(symbol))

@app.get("/jarvis/explain/{symbol}", tags=["Jarvis"])
def jarvis_explain(symbol: str, profile_name: str = Query(default="balanced")):
    try:return to_json(JarvisQueryService().explain(symbol,profile_name))
    except ValueError as error:raise HTTPException(status_code=404,detail=str(error))

@app.get("/jarvis/indicator/{symbol}", tags=["Jarvis"])
def jarvis_indicator(symbol: str, indicator: str = Query(...)):
    try:return to_json(JarvisQueryService().indicator(symbol,indicator))
    except ValueError as error:raise HTTPException(status_code=400,detail=str(error))

@app.get("/jarvis/fundamentals/{symbol}", tags=["Jarvis"])
def jarvis_fundamentals(symbol: str):
    try:return to_json(JarvisQueryService().fundamentals(symbol))
    except ValueError as error:raise HTTPException(status_code=404,detail=str(error))

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


@app.get(
    "/watchlist"
)
def get_managed_watchlist():

    entries = (
        WatchlistRepository()
        .load_all()
    )
    return {
        "entities":[
            {
                "symbol":
                    item.symbol,

                "company_name":
                    item.company_name,

                "active":
                    item.active,

                "created_at":
                    item.created_at
            }
            for item in entries
        ]

    }

@app.post(
    "/watchlist/{symbol}"
)
def add_stock(
    symbol: str
):

    added = (
        AddStockUseCase()
        .execute(
            symbol
        )
    )

    return {
        "symbol": symbol,
        "added": added
    }

@app.delete(
    "/watchlist/{symbol}"
)
def remove_stock(
    symbol: str
):

    RemoveStockUseCase().execute(
        symbol
    )

    return {
        "removed": symbol
    }

@app.post("/refresh", tags=["System"])
def refresh_stockmind():
    try:
        results=RefreshCoordinator().run_daily()
        return {"status":"ok","results":[{"symbol":r.symbol,"mode":r.mode,"success":r.success,"error":r.error} for r in results]}
    except Exception as error:
        raise HTTPException(status_code=500,detail=str(error))
