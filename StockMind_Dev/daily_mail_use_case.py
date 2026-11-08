from stockmind.application.dashboard.use_cases.daily_intelligence_dashboard_use_case import DailyIntelligenceDashboardUseCase
from stockmind.application.dashboard.use_cases.profile_comparison_dashboard_use_case import ProfileComparisonDashboardUseCase
from stockmind.application.dashboard.use_cases.watchlist_dashboard_use_case import WatchlistDashboardUseCase
from stockmind.application.exit.portfolio_exit_use_case import PortfolioExitUseCase
from stockmind.application.notifications.models.daily_mail_result import DailyMailResult,ProfileSignalMailItem,StockMailItem,PortfolioMailItem
from stockmind.application.portfolio.portfolio_dashboard_use_case import PortfolioDashboardUseCase
from stockmind.application.portfolio.portfolio_intelligence_use_case import PortfolioIntelligenceUseCase
from stockmind.application.portfolio.portfolio_performance_use_case import PortfolioPerformanceUseCase

class DailyMailUseCase:
    PROFILE_ORDER={'individual':0,'balanced':1,'conservative':2,'aggressive':3}
    def build(self):
        intel=DailyIntelligenceDashboardUseCase().load('balanced')
        watch=WatchlistDashboardUseCase().load('balanced')
        rows=[]
        for stock in watch.stocks:
            comparison=ProfileComparisonDashboardUseCase().load(stock.symbol,'5y',3)
            profiles=[]
            for entry in comparison.entries:
                signal='BUY' if entry.current_buy_signal is True else entry.signal
                count=entry.complete_period_count
                quality='HIGH' if count>=50 else 'MEDIUM' if count>=20 else 'LOW' if count else 'NO_SAMPLE'
                profiles.append(ProfileSignalMailItem(profile_name=entry.profile_name,signal=signal,target_hit_rate=entry.target_hit_rate,complete_period_count=count,sample_quality=quality,opportunity_score=getattr(entry,'score',None),confidence=getattr(entry,'confidence',None),risk_level=getattr(entry,'risk_level',None)))
            buy_profiles=[x.profile_name for x in profiles if x.signal=='BUY']
            primary=sorted((x for x in profiles if x.signal=='BUY'),key=lambda x:(self.PROFILE_ORDER.get(x.profile_name,9),-(x.opportunity_score or 0)))[0].profile_name if buy_profiles else None
            rows.append(StockMailItem(stock.symbol,stock.company_name,profiles,bool(buy_profiles),buy_profiles,primary))
        changes=[]
        for item in intel.items:
            if item.new_buy_period:changes.append({'symbol':item.symbol,'company_name':item.company_name,'type':'Neue BUY-Periode','detail':f'Start {item.active_period_start}','priority':100})
            if item.signal_changed:changes.append({'symbol':item.symbol,'company_name':item.company_name,'type':'Signaländerung','detail':f'{item.previous_signal} → {item.current_signal}','priority':90})
            if item.score_change is not None and abs(item.score_change)>=5:changes.append({'symbol':item.symbol,'company_name':item.company_name,'type':'Opportunity Score','detail':f'{item.previous_score:.1f} → {item.current_score:.1f} ({item.score_change:+.1f})','priority':70})
        changes.sort(key=lambda x:x['priority'],reverse=True)
        portfolio=PortfolioDashboardUseCase().load();intelligence=PortfolioIntelligenceUseCase().load();decisions={x.position_id:x for x in PortfolioExitUseCase().load()};performance=PortfolioPerformanceUseCase().load();portfolio_items=[]
        for item in intelligence:
            decision=decisions.get(item.position_id)
            portfolio_items.append(PortfolioMailItem(item.symbol,item.company_name,item.unrealized_profit,item.unrealized_return_pct,item.holding_days,item.remaining_strategy_days,item.target_reached,item.current_signal,item.current_score,item.score_change,item.attention_level,item.attention_reasons,decision.status if decision else 'HOLD',decision.strategy_name if decision else 'BASELINE_8PCT_60D',decision.reasons if decision else [],decision.validation_status if decision else 'INSUFFICIENT_VALIDATION'))
        buys=[x for x in rows if x.has_buy_signal]
        exits=sum(x.exit_status=='EXIT_REVIEW' for x in portfolio_items);watches=sum(x.exit_status=='WATCH' for x in portfolio_items)
        subject=f'StockMind Daily | {len(buys)} Entry | {exits} Exit Review | {watches} Watch | {intel.latest_trading_date or "aktueller Stand"}'
        return DailyMailResult(intel.latest_trading_date,intel.previous_trading_date,subject,buys,changes,rows,portfolio_items,portfolio.invested_amount,portfolio.market_value,portfolio.unrealized_profit,performance['ytd']['net_profit'])
