from stockmind.infrastructure.strategy.fitted_profile_repository import FittedProfileRepository

class ActivateFittedProfileUseCase:
    def __init__(self,database_path=None):self._repo=FittedProfileRepository(database_path)
    def execute(self,profile_id):
        profile=self._repo.load(profile_id)
        if profile is None:raise ValueError('Fitted Profile wurde nicht gefunden.')
        if profile.status!='VALIDATED':raise ValueError('Nur ein VALIDATED Fitted Profile darf aktiviert werden.')
        self._repo.activate(profile_id,profile.symbol)
        return self._repo.load(profile_id)

class DeactivateFittedProfileUseCase:
    def __init__(self,database_path=None):self._repo=FittedProfileRepository(database_path)
    def execute(self,symbol):
        self._repo.deactivate_symbol(symbol)
