from stockmind.domain.core_setup.core_setup_engine import CoreSetupEngine
from stockmind.domain.features.feature_engine import FeatureEngine
from stockmind.domain.history.daily_buy_signal import DailyBuySignal
from stockmind.domain.indicators.indicator_result import IndicatorResult
from stockmind.domain.profiles.trading_profile import TradingProfile
from stockmind.domain.quality.quality_engine import QualityEngine
from stockmind.domain.rules.rule_engine import RuleEngine
from stockmind.infrastructure.rules.rule_set_repository import RuleSetRepository


class DailyBuySignalEvaluator:
    QUALITY_ORDER = {
        "LOW": 1,
        "MEDIUM": 2,
        "HIGH": 3,
        "VERY_HIGH": 4,
    }

    def evaluate(
        self,
        symbol: str,
        profile: TradingProfile,
        analysis_period: str,
        trading_date: str,
        entry_price: float,
        indicator_result: IndicatorResult,
        rule_set_name: str = "entry_setup",
        min_quality: str = "MEDIUM",
    ) -> DailyBuySignal:
        features = FeatureEngine().build(
            result=indicator_result,
            profile=profile,
        )
        rule_set = RuleSetRepository().get_by_name(rule_set_name)
        rule_results = RuleEngine(rule_set=rule_set).evaluate(features)
        core_setup_result = CoreSetupEngine().evaluate(rule_results)
        quality_result = QualityEngine().calculate(
            rule_results=rule_results,
            core_setup_result=core_setup_result,
        )
        meets_quality = self.QUALITY_ORDER.get(
            quality_result.quality,
            0,
        ) >= self.QUALITY_ORDER.get(min_quality, 0)
        is_buy = core_setup_result.setup_detected and meets_quality

        return DailyBuySignal(
            symbol=symbol.upper().strip(),
            profile_name=profile.name,
            analysis_period=analysis_period,
            trading_date=trading_date,
            is_buy=is_buy,
            quality=quality_result.quality,
            quality_score=quality_result.score,
            core_setup_detected=core_setup_result.setup_detected,
            satisfied_rules=core_setup_result.satisfied_rules,
            required_rules=core_setup_result.required_rules,
            reasons=quality_result.reasons,
            missing_rules=core_setup_result.missing_rules,
            entry_price=entry_price,
        )
