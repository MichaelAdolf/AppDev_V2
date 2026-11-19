from datetime import datetime
from uuid import uuid4
from stockmind.application.dashboard.use_cases.profile_comparison_dashboard_use_case import ProfileComparisonDashboardUseCase
from stockmind.domain.portfolio.portfolio_position import PortfolioPosition
from stockmind.domain.portfolio.portfolio_purchase_lot import PortfolioPurchaseLot
from stockmind.infrastructure.portfolio.portfolio_repository import PortfolioRepository
from stockmind.infrastructure.watchlists.watchlist_repository import WatchlistRepository

class AddPositionUseCase:
 def __init__(self,database_path=None):self._repository=PortfolioRepository(database_path)
 def execute(self,symbol,purchase_date,purchase_price,quantity,purchase_fees=0.0,entry_profile='balanced',note=''):
  symbol=symbol.upper().strip()
  if purchase_price<=0 or quantity<=0:raise ValueError('Kaufpreis und Stückzahl müssen größer als 0 sein.')
  if purchase_fees<0:raise ValueError('Kaufgebühren dürfen nicht negativ sein.')
  watch=next((x for x in WatchlistRepository().load_all() if x.symbol.upper()==symbol),None);company=watch.company_name if watch else symbol
  comp=ProfileComparisonDashboardUseCase().load(symbol,'5y',3);selected=next((x for x in comp.entries if x.profile_name==entry_profile),None);buy_count=len({x.profile_name for x in comp.entries if x.signal=='BUY' or x.current_buy_signal is True})
  now=datetime.now().isoformat(timespec='seconds');position=self._repository.find_open_position_by_symbol(symbol)
  if position is None:
   position=PortfolioPosition(str(uuid4()),symbol,company,str(purchase_date),float(purchase_price),float(quantity),float(purchase_fees),entry_profile,'BUY' if selected and selected.current_buy_signal is True else selected.signal if selected else None,selected.score if selected else None,selected.confidence if selected else None,selected.risk_level if selected else None,selected.target_hit_rate if selected else None,selected.complete_period_count if selected else 0,buy_count,selected.active_period_start if selected else None,note.strip(),'OPEN',now,now);self._repository.add_position(position)
  lot=PortfolioPurchaseLot(str(uuid4()),position.id,symbol,str(purchase_date),float(purchase_price),float(quantity),float(purchase_fees),entry_profile,'BUY' if selected and selected.current_buy_signal is True else selected.signal if selected else None,selected.score if selected else None,selected.confidence if selected else None,selected.risk_level if selected else None,selected.target_hit_rate if selected else None,selected.complete_period_count if selected else 0,buy_count,selected.active_period_start if selected else None,note.strip(),now,now)
  self._repository.add_purchase_lot(lot);return self._repository.find_open_position_by_symbol(symbol)
