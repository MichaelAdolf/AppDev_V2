from dataclasses import dataclass
from stockmind.domain.portfolio.portfolio_position import PortfolioPosition
from stockmind.domain.portfolio.portfolio_purchase_lot import PortfolioPurchaseLot
from stockmind.domain.portfolio.portfolio_trade import PortfolioTrade
@dataclass(frozen=True)
class PortfolioPositionView:
 position: PortfolioPosition;lots:list[PortfolioPurchaseLot];current_price:float|None;market_value:float|None;invested_amount:float;unrealized_profit:float|None;unrealized_return_pct:float|None;target_price:float;target_distance_pct:float|None;holding_days:int;current_signal:str|None;current_score:float|None;current_confidence:float|None;current_risk:str|None
@dataclass(frozen=True)
class PortfolioDashboardResult:
 positions:list[PortfolioPositionView];trades:list[PortfolioTrade];invested_amount:float;market_value:float;unrealized_profit:float;realized_net_profit:float
