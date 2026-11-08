from stockmind.application.use_cases.analyze_stock_use_case import AnalyzeStockUseCase
from stockmind.infrastructure.strategy.fitted_profile_repository import FittedProfileRepository
from stockmind.infrastructure.strategy.individual_analysis_repository import IndividualAnalysisRepository

class RunIndividualAnalysisUseCase:
    def __init__(self,database_path=None):self._database_path=database_path
    def execute(self,symbol):
        profile=FittedProfileRepository(self._database_path).load_active(symbol)
        if profile is None:raise ValueError(f"Kein aktives Individual-Profil für {symbol.upper()} vorhanden.")
        result=AnalyzeStockUseCase().execute(symbol=symbol,profile_name="individual")
        IndividualAnalysisRepository(self._database_path).save(symbol,profile)
        return result
