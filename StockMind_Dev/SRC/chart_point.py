from dataclasses import dataclass
@dataclass(frozen=True)
class ChartPoint:
 symbol:str;trading_date:str;close_price:float;bollinger_upper:float|None;bollinger_middle:float|None;bollinger_lower:float|None
 open_price:float|None=None;high_price:float|None=None;low_price:float|None=None
 source_currency:str='EUR';fx_rate_to_eur:float=1.0
 source_open_price:float|None=None;source_high_price:float|None=None;source_low_price:float|None=None;source_close_price:float|None=None
