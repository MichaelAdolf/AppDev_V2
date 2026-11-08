from dataclasses import dataclass
from stockmind.infrastructure.strategy.fitted_profile_repository import FittedProfileRepository

@dataclass(frozen=True)
class ActiveStrategy:
    symbol:str
    strategy_type:str
    strategy_name:str
    base_profile:str
    fitted_profile:object|None

class ActiveStrategyResolver:
    def __init__(self,database_path=None):self._repo=FittedProfileRepository(database_path)
    def resolve(self,symbol,standard_profile='balanced'):
        fitted=self._repo.load_active(symbol)
        if fitted:return ActiveStrategy(symbol.upper(),'FITTED',f'{symbol.upper()} Fitted v{fitted.version}',fitted.base_profile,fitted)
        return ActiveStrategy(symbol.upper(),'STANDARD',standard_profile,standard_profile,None)
