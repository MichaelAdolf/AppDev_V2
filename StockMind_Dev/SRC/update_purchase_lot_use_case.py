from dataclasses import replace
from datetime import datetime
from stockmind.infrastructure.portfolio.portfolio_repository import PortfolioRepository
class UpdatePurchaseLotUseCase:
 def __init__(self,database_path=None):self._repository=PortfolioRepository(database_path)
 def execute(self,lot_id,purchase_date,purchase_price,quantity,purchase_fees,entry_profile,note=''):
  lot=self._repository.load_lot(lot_id)
  if not lot:raise ValueError('Kauftranche wurde nicht gefunden.')
  if purchase_price<=0 or quantity<=0 or purchase_fees<0:raise ValueError('Kaufdaten sind ungültig.')
  updated=replace(lot,purchase_date=str(purchase_date),purchase_price=float(purchase_price),quantity=float(quantity),purchase_fees=float(purchase_fees),entry_profile=entry_profile,note=note.strip(),updated_at=datetime.now().isoformat(timespec='seconds'))
  self._repository.update_purchase_lot(updated);return updated
