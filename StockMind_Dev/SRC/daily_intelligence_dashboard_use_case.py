from stockmind.application.dashboard.models.daily_intelligence_result import (
    DailyIntelligenceItem,
    DailyIntelligenceResult,
)
from stockmind.application.dashboard.use_cases.buy_period_dashboard_use_case import (
    BuyPeriodDashboardUseCase,
)
from stockmind.application.dashboard.use_cases.profile_comparison_dashboard_use_case import (
    ProfileComparisonDashboardUseCase,
)
from stockmind.infrastructure.history.historical_opportunity_repository import (
    HistoricalOpportunityRepository,
)
from stockmind.infrastructure.history.latest_analysis_repository import (
    LatestAnalysisRepository,
)
from stockmind.infrastructure.watchlists.watchlist_repository import WatchlistRepository


class DailyIntelligenceDashboardUseCase:
    SIGNIFICANT_SCORE_CHANGE = 5.0

    def load(self, profile_name: str) -> DailyIntelligenceResult:
        latest_results = LatestAnalysisRepository().load_all(profile_name)
        latest_by_symbol = {item.symbol.upper(): item for item in latest_results}
        watchlist_entries = [entry for entry in WatchlistRepository().load_all() if entry.active]
        history_repository = HistoricalOpportunityRepository()
        period_use_case = BuyPeriodDashboardUseCase()
        comparison_use_case = ProfileComparisonDashboardUseCase()
        items = []
        all_latest_dates = []
        all_previous_dates = []

        for watchlist_entry in watchlist_entries:
            symbol = watchlist_entry.symbol.upper()
            latest = latest_by_symbol.get(symbol)
            if latest is None:
                continue
            history = history_repository.load_by_symbol(symbol, profile_name)
            current_history = history[-1] if history else None
            previous_history = history[-2] if len(history) >= 2 else None
            if current_history:
                all_latest_dates.append(current_history.trading_date)
            if previous_history:
                all_previous_dates.append(previous_history.trading_date)

            period_result = period_use_case.load(
                symbol=symbol,
                profile_name=profile_name,
                analysis_period="5y",
                max_gap_days=3,
            )
            comparison = comparison_use_case.load(
                symbol=symbol,
                analysis_period="5y",
                max_gap_days=3,
            )
            profile_buy_count = len({
                entry.profile_name
                for entry in comparison.entries
                if entry.signal == "BUY" or entry.current_buy_signal is True
            })
            profile_consensus = f"{profile_buy_count}/3 BUY"

            current_score = latest.opportunity_score
            previous_score = (
                previous_history.opportunity_score
                if previous_history else None
            )
            score_change = (
                current_score - previous_score
                if previous_score is not None else None
            )
            previous_signal = previous_history.signal if previous_history else None
            signal_changed = (
                previous_signal is not None
                and previous_signal != latest.signal
            )
            previous_confidence = (
                previous_history.confidence if previous_history else None
            )
            confidence_change = (
                latest.confidence - previous_confidence
                if previous_confidence is not None else None
            )
            previous_risk = previous_history.risk_level if previous_history else None
            active_period = period_result.active_period
            new_buy_period = (
                active_period is not None
                and current_history is not None
                and active_period.start_date == current_history.trading_date
            )
            relevance_status, relevance_priority = self._relevance(
                new_buy_period=new_buy_period,
                signal_changed=signal_changed,
                current_signal=latest.signal,
                profile_buy_count=profile_buy_count,
                score_change=score_change,
                confidence=latest.confidence,
                has_active_period=active_period is not None,
            )
            stats = period_result.statistics
            items.append(DailyIntelligenceItem(
                symbol=symbol,
                company_name=watchlist_entry.company_name,
                profile_name=profile_name,
                current_score=current_score,
                previous_score=previous_score,
                score_change=score_change,
                current_confidence=latest.confidence,
                confidence_change=confidence_change,
                current_signal=latest.signal,
                previous_signal=previous_signal,
                signal_changed=signal_changed,
                current_risk=latest.risk_level,
                previous_risk=previous_risk,
                active_period_start=(active_period.start_date if active_period else None),
                active_period_duration_days=(active_period.calendar_duration_days if active_period else None),
                new_buy_period=new_buy_period,
                target_hit_rate=stats.target_hit_rate,
                complete_period_count=stats.complete_period_count,
                sample_quality=stats.sample_quality,
                profile_buy_count=profile_buy_count,
                profile_consensus=profile_consensus,
                relevance_status=relevance_status,
                relevance_priority=relevance_priority,
            ))

        items.sort(
            key=lambda item: (
                item.relevance_priority,
                item.score_change if item.score_change is not None else -999.0,
                item.current_score,
            ),
            reverse=True,
        )
        return DailyIntelligenceResult(
            profile_name=profile_name,
            latest_trading_date=max(all_latest_dates) if all_latest_dates else None,
            previous_trading_date=max(all_previous_dates) if all_previous_dates else None,
            stock_count=len(items),
            relevant_count=sum(item.relevance_priority > 0 for item in items),
            new_buy_period_count=sum(item.new_buy_period for item in items),
            signal_change_count=sum(item.signal_changed for item in items),
            consensus_count=sum(item.profile_buy_count == 3 for item in items),
            score_gainer_count=sum(
                item.score_change is not None
                and item.score_change >= self.SIGNIFICANT_SCORE_CHANGE
                for item in items
            ),
            items=items,
        )

    def _relevance(
        self,
        new_buy_period: bool,
        signal_changed: bool,
        current_signal: str,
        profile_buy_count: int,
        score_change: float | None,
        confidence: float,
        has_active_period: bool,
    ) -> tuple[str, int]:
        if new_buy_period:
            return "Neue BUY-Periode", 100
        if signal_changed and current_signal == "BUY":
            return "Neues BUY-Signal", 90
        if profile_buy_count == 3:
            return "Profil-Konsens 3/3 BUY", 80
        if score_change is not None and score_change >= self.SIGNIFICANT_SCORE_CHANGE:
            return "Opportunity Score stark gestiegen", 70
        if has_active_period:
            return "BUY-Periode läuft", 60
        if signal_changed:
            return "Signal geändert", 50
        if confidence >= 0.75:
            return "Hohe Confidence", 40
        return "Kein aktuelles Ereignis", 0
