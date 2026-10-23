from stockmind.application.dashboard.use_cases.daily_intelligence_dashboard_use_case import DailyIntelligenceDashboardUseCase
from stockmind.application.dashboard.use_cases.profile_comparison_dashboard_use_case import ProfileComparisonDashboardUseCase
from stockmind.application.dashboard.use_cases.watchlist_dashboard_use_case import WatchlistDashboardUseCase
from stockmind.application.notifications.models.daily_mail_result import DailyMailResult, ProfileSignalMailItem, StockMailItem


class DailyMailUseCase:
    PROFILES=["conservative","balanced","aggressive"]

    def build(self) -> DailyMailResult:
        balanced=DailyIntelligenceDashboardUseCase().load("balanced")
        watch=WatchlistDashboardUseCase().load("balanced")
        company_by_symbol={x.symbol.upper():x.company_name for x in watch.stocks}
        rows=[]
        for stock in watch.stocks:
            comparison=ProfileComparisonDashboardUseCase().load(stock.symbol,"5y",3)
            profiles=[]
            for entry in comparison.entries:
                profiles.append(ProfileSignalMailItem(
                    profile_name=entry.profile_name,
                    signal="BUY" if entry.current_buy_signal is True else entry.signal,
                    target_hit_rate=entry.target_hit_rate,
                    complete_period_count=entry.complete_period_count,
                    sample_quality=self._sample_quality(entry.complete_period_count),
                ))
            rows.append(StockMailItem(
                symbol=stock.symbol,
                company_name=company_by_symbol.get(stock.symbol.upper(),stock.symbol),
                profiles=profiles,
                has_buy_signal=any(p.signal=="BUY" for p in profiles),
            ))

        changes=[]
        for item in balanced.items:
            if item.new_buy_period:
                changes.append({"symbol":item.symbol,"company_name":item.company_name,"type":"Neue BUY-Periode","detail":f"Start {item.active_period_start}"})
            if item.signal_changed:
                changes.append({"symbol":item.symbol,"company_name":item.company_name,"type":"Signaländerung","detail":f"{item.previous_signal} → {item.current_signal}"})
            if item.score_change is not None and abs(item.score_change)>=5:
                changes.append({"symbol":item.symbol,"company_name":item.company_name,"type":"Opportunity Score","detail":f"{item.previous_score:.1f} → {item.current_score:.1f} ({item.score_change:+.1f})"})

        buys=[x for x in rows if x.has_buy_signal]
        date=balanced.latest_trading_date
        subject=(f"StockMind Daily Briefing | {len(buys)} Aktien mit BUY | {date or 'aktueller Stand'}")
        return DailyMailResult(date,balanced.previous_trading_date,subject,buys,changes,rows)

    def _sample_quality(self,n):
        return "HIGH" if n>=50 else "MEDIUM" if n>=20 else "LOW" if n else "NO_SAMPLE"
