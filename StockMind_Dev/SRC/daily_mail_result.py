from dataclasses import dataclass
@dataclass(frozen=True)
class ProfileSignalMailItem:profile_name:str;signal:str;target_hit_rate:float;complete_period_count:int;sample_quality:str
@dataclass(frozen=True)
class StockMailItem:symbol:str;company_name:str;profiles:list[ProfileSignalMailItem];has_buy_signal:bool;fitted_active:bool=False;fitted_strategy_name:str|None=None;fitted_signal:str|None=None;fitted_base_profile:str|None=None
@dataclass(frozen=True)
class PortfolioMailItem:symbol:str;company_name:str;unrealized_profit:float|None;unrealized_return_pct:float|None;holding_days:int;remaining_strategy_days:int;target_reached:bool;current_signal:str|None;current_score:float|None;score_change:float|None;attention_level:str;attention_reasons:list[str];exit_status:str='HOLD';exit_strategy:str='BASELINE_8PCT_60D';exit_reasons:list[str]|None=None;exit_validation_status:str='INSUFFICIENT_VALIDATION'
@dataclass(frozen=True)
class DailyMailResult:trading_date:str|None;previous_trading_date:str|None;subject:str;buy_signal_stocks:list[StockMailItem];changes:list[dict];watchlist:list[StockMailItem];portfolio_items:list[PortfolioMailItem];portfolio_invested:float;portfolio_market_value:float;portfolio_unrealized:float;portfolio_realized_ytd:float
