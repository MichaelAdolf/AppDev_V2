from stockmind.application.dashboard.use_cases.daily_intelligence_dashboard_use_case import DailyIntelligenceDashboardUseCase
from stockmind.application.dashboard.use_cases.profile_comparison_dashboard_use_case import ProfileComparisonDashboardUseCase
from stockmind.application.dashboard.use_cases.watchlist_dashboard_use_case import WatchlistDashboardUseCase
from stockmind.application.exit.portfolio_exit_use_case import PortfolioExitUseCase
from stockmind.application.notifications.models.daily_mail_result import DailyMailResult,ProfileSignalMailItem,StockMailItem,PortfolioMailItem
from stockmind.application.portfolio.portfolio_dashboard_use_case import PortfolioDashboardUseCase
from stockmind.application.portfolio.portfolio_intelligence_use_case import PortfolioIntelligenceUseCase
from stockmind.application.portfolio.portfolio_performance_use_case import PortfolioPerformanceUseCase
class DailyMailUseCase:
 def build(self):
  intel=DailyIntelligenceDashboardUseCase().load('balanced');watch=WatchlistDashboardUseCase().load('balanced');rows=[]
  for stock in watch.stocks:
   comp=ProfileComparisonDashboardUseCase().load(stock.symbol,'5y',3);profiles=[ProfileSignalMailItem(e.profile_name,'BUY' if e.current_buy_signal is True else e.signal,e.target_hit_rate,e.complete_period_count,'HIGH' if e.complete_period_count>=50 else 'MEDIUM' if e.complete_period_count>=20 else 'LOW' if e.complete_period_count else 'NO_SAMPLE') for e in comp.entries];rows.append(StockMailItem(stock.symbol,stock.company_name,profiles,any(p.signal=='BUY' for p in profiles)))
  changes=[]
  for x in intel.items:
   if x.new_buy_period:changes.append({'symbol':x.symbol,'company_name':x.company_name,'type':'Neue BUY-Periode','detail':f'Start {x.active_period_start}'})
   if x.signal_changed:changes.append({'symbol':x.symbol,'company_name':x.company_name,'type':'Signaländerung','detail':f'{x.previous_signal} → {x.current_signal}'})
   if x.score_change is not None and abs(x.score_change)>=5:changes.append({'symbol':x.symbol,'company_name':x.company_name,'type':'Opportunity Score','detail':f'{x.previous_score:.1f} → {x.current_score:.1f} ({x.score_change:+.1f})'})
  portfolio=PortfolioDashboardUseCase().load();pi=PortfolioIntelligenceUseCase().load();decisions={x.position_id:x for x in PortfolioExitUseCase().load()};perf=PortfolioPerformanceUseCase().load();mail_items=[]
  for x in pi:
   d=decisions.get(x.position_id);mail_items.append(PortfolioMailItem(x.symbol,x.company_name,x.unrealized_profit,x.unrealized_return_pct,x.holding_days,x.remaining_strategy_days,x.target_reached,x.current_signal,x.current_score,x.score_change,x.attention_level,x.attention_reasons,d.status if d else 'HOLD',d.strategy_name if d else 'BASELINE_8PCT_60D',d.reasons if d else [],d.validation_status if d else 'INSUFFICIENT_VALIDATION'))
  buys=[x for x in rows if x.has_buy_signal];exit_count=sum(x.exit_status=='EXIT_REVIEW' for x in mail_items);subject=f'StockMind Daily Briefing | {len(buys)} BUY | {exit_count} Exit-Prüfungen | {intel.latest_trading_date or "aktueller Stand"}'
  return DailyMailResult(intel.latest_trading_date,intel.previous_trading_date,subject,buys,changes,rows,mail_items,portfolio.invested_amount,portfolio.market_value,portfolio.unrealized_profit,perf['ytd']['net_profit'])
