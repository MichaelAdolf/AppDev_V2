from stockmind.application.dashboard.models.profile_comparison_result import ProfileComparisonEntry,ProfileComparisonResult
from stockmind.application.dashboard.use_cases.buy_period_dashboard_use_case import BuyPeriodDashboardUseCase
from stockmind.application.strategy.fitted_profile_signal_use_case import FittedProfileSignalUseCase
from stockmind.infrastructure.history.daily_buy_signal_repository import DailyBuySignalRepository
from stockmind.infrastructure.history.latest_analysis_repository import LatestAnalysisRepository
from stockmind.infrastructure.strategy.fitted_profile_repository import FittedProfileRepository

class ProfileComparisonDashboardUseCase:
    STANDARD_PROFILES=["conservative","balanced","aggressive"]
    def load(self,symbol,analysis_period="5y",max_gap_days=3):
        symbol=symbol.upper();entries=[];analysis_repo=LatestAnalysisRepository();signal_repo=DailyBuySignalRepository();period_uc=BuyPeriodDashboardUseCase()
        for profile_name in self.STANDARD_PROFILES:
            stock=next((x for x in analysis_repo.load_all(profile_name) if x.symbol.upper()==symbol),None)
            if stock is None:continue
            latest_signal=signal_repo.load_latest(symbol=symbol,profile_name=profile_name,analysis_period=analysis_period);period=period_uc.load(symbol,profile_name,analysis_period,max_gap_days);active=period.active_period;stats=period.statistics
            entries.append(ProfileComparisonEntry(profile_name,stock.opportunity_score,stock.confidence,stock.signal,stock.risk_level,latest_signal.is_buy if latest_signal else None,active.start_date if active else None,active.calendar_duration_days if active else None,period.period_count,stats.complete_period_count,stats.incomplete_period_count,stats.target_hit_rate,stats.below_target_rate,stats.flat_rate,stats.negative_rate))
        active_profile=FittedProfileRepository().load_active(symbol)
        if active_profile:
            stock=next((x for x in analysis_repo.load_all("individual") if x.symbol.upper()==symbol),None);signal=FittedProfileSignalUseCase().evaluate(symbol);validation=FittedProfileRepository().load_validation(active_profile.id) or {};count=int(validation.get('validation_sample_count',0));rate=float(validation.get('validation_target_hit_rate',0.0))
            if stock:
                entries.append(ProfileComparisonEntry("individual",stock.opportunity_score,stock.confidence,stock.signal,stock.risk_level,signal.signal=='BUY',None,None,count,count,0,rate,0.0,0.0,max(0.0,1-rate)))
        return ProfileComparisonResult(symbol,analysis_period,entries)
