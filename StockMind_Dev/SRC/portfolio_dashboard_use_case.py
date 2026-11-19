from datetime import date
from stockmind.application.portfolio.models.portfolio_dashboard_result import PortfolioDashboardResult,PortfolioPositionView
from stockmind.infrastructure.history.chart_data_repository import ChartDataRepository
from stockmind.infrastructure.history.latest_analysis_repository import LatestAnalysisRepository
from stockmind.infrastructure.portfolio.portfolio_repository import PortfolioRepository
class PortfolioDashboardUseCase:
 def __init__(self,database_path=None):self._database_path=database_path
 def load(self):
  repo=PortfolioRepository(self._database_path);chart=ChartDataRepository(self._database_path);latest={p:{x.symbol.upper():x for x in LatestAnalysisRepository(self._database_path).load_all(p)} for p in ('conservative','balanced','aggressive')};views=[]
  for pos in repo.load_open_positions():
   lots=repo.load_lots_for_position(pos.id);points=chart.load_by_symbol(pos.symbol);price=points[-1].close_price if points else None;invested=pos.purchase_price*pos.quantity+pos.purchase_fees;value=price*pos.quantity if price is not None else None;pl=value-invested if value is not None else None;ret=pl/invested if pl is not None and invested else None;target=pos.purchase_price*1.08;distance=target/price-1 if price else None;current=latest.get(pos.entry_profile,{}).get(pos.symbol.upper())
   views.append(PortfolioPositionView(pos,lots,price,value,invested,pl,ret,target,distance,(date.today()-date.fromisoformat(pos.purchase_date)).days,current.signal if current else None,current.opportunity_score if current else None,current.confidence if current else None,current.risk_level if current else None))
  trades=repo.load_trades();return PortfolioDashboardResult(views,trades,sum(x.invested_amount for x in views),sum(x.market_value or 0 for x in views),sum(x.unrealized_profit or 0 for x in views),sum(x.net_profit for x in trades))
