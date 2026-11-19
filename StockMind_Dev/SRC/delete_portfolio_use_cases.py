from stockmind.infrastructure.portfolio.portfolio_repository import PortfolioRepository
class DeletePurchaseLotUseCase:
 def __init__(self,database_path=None):self._repository=PortfolioRepository(database_path)
 def execute(self,lot_id):self._repository.delete_purchase_lot(lot_id)
class DeletePositionUseCase:
 def __init__(self,database_path=None):self._repository=PortfolioRepository(database_path)
 def execute(self,position_id):self._repository.delete_open_position(position_id)
class DeleteTradeUseCase:
 def __init__(self,database_path=None):self._repository=PortfolioRepository(database_path)
 def execute(self,trade_id):self._repository.delete_trade(trade_id)
