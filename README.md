import yfinance as yf

from stockmind.application.models.stock_analysis_result import (
    StockAnalysisResult
)

from stockmind.domain.indicators.indicator_engine import (
    IndicatorEngine
)

from stockmind.domain.indicators.sma_indicator import (
    SMAIndicator
)

from stockmind.domain.indicators.ema_indicator import (
    EMAIndicator
)

from stockmind.domain.indicators.rsi_indicator import (
    RSIIndicator
)

from stockmind.domain.indicators.macd_indicator import (
    MACDIndicator
)

from stockmind.domain.indicators.bollinger_indicator import (
    BollingerIndicator
)

from stockmind.domain.indicators.adx_indicator import (
    ADXIndicator
)

from stockmind.domain.indicators.stochastic_indicator import (
    StochasticIndicator
)

from stockmind.domain.features.feature_engine import (
    FeatureEngine
)

from stockmind.domain.rules.rule_engine import (
    RuleEngine
)

from stockmind.domain.core_setup.core_setup_engine import (
    CoreSetupEngine
)

from stockmind.domain.quality.quality_engine import (
    QualityEngine
)

from stockmind.domain.confidence.confidence_engine import (
    ConfidenceEngine
)

from stockmind.domain.risk.risk_engine import (
    RiskEngine
)

from stockmind.domain.signals.signal_engine import (
    SignalEngine
)

from stockmind.domain.historical_success.historical_success_engine import (
    HistoricalSuccessEngine
)

from stockmind.infrastructure.profiles.profile_repository import (
    ProfileRepository
)

from stockmind.infrastructure.rules.rule_set_repository import (
    RuleSetRepository
)


class AnalyzeStockUseCase:

    def execute(
        self,
        symbol: str,
        profile_name: str,
        rule_set_name: str = "entry_setup"
    ) -> StockAnalysisResult:

        profile = (
            ProfileRepository()
            .get_by_name(
                profile_name
            )
        )

        rule_set = (
            RuleSetRepository()
            .get_by_name(
                rule_set_name
            )
        )

        ticker = yf.Ticker(
            symbol
        )

        data = ticker.history(
            period="5y"
        )

        indicator_engine = IndicatorEngine(
            indicators=[
                SMAIndicator(),
                EMAIndicator(),
                RSIIndicator(),
                MACDIndicator(),
                BollingerIndicator(),
                ADXIndicator(),
                StochasticIndicator(),
            ]
        )

        indicator_result = (
            indicator_engine.calculate(
                symbol=symbol,
                data=data
            )
        )

        features = (
            FeatureEngine()
            .build(
                result=indicator_result,
                profile=profile
            )
        )

        rule_results = (
            RuleEngine(
                rule_set=rule_set
            )
            .evaluate(
                features
            )
        )

        core_setup_result = (
            CoreSetupEngine()
            .evaluate(
                rule_results
            )
        )

        quality_result = (
            QualityEngine()
            .calculate(
                rule_results=rule_results,
                core_setup_result=core_setup_result
            )
        )

        historical_result = (
            HistoricalSuccessEngine()
            .analyze(
                symbol=symbol,
                data=data,
                profile=profile,
                rule_set_name=rule_set_name,
                target_pct=0.08,
                lookahead_days=60,
                min_quality="MEDIUM",
                top_n_similar=50
            )
        )

        confidence_result = (
            ConfidenceEngine()
            .calculate(
                rule_results=rule_results,
                historical_success_result=historical_result
            )
        )

        risk_result = (
            RiskEngine()
            .calculate(
                features
            )
        )

        signal = (
            SignalEngine()
            .create_signal(
                symbol=symbol,
                quality_result=quality_result,
                confidence_result=confidence_result,
                risk_result=risk_result
            )
        )

        return StockAnalysisResult(
            symbol=symbol,
            profile_name=profile_name,

            signal=signal,

            quality=quality_result.quality,

            confidence=confidence_result.confidence,

            risk_level=risk_result.level,

            historical_success_rate=(
                historical_result.success_rate
            ),

            setup_count=(
                historical_result.setup_count
            ),

            sample_quality=(
                historical_result.sample_quality
            ),

            average_similarity=(
                historical_result.average_similarity
            ),

            reasons=(
                signal.reasons
            )
        )
