from types import SimpleNamespace
import sqlite3

import pandas as pd
import yfinance as yf

from stockmind.domain.confidence.confidence_engine import ConfidenceEngine
from stockmind.domain.core_setup.core_setup_engine import CoreSetupEngine
from stockmind.domain.features.feature_engine import FeatureEngine
from stockmind.domain.history.historical_opportunity_entry import HistoricalOpportunityEntry
from stockmind.domain.history.historical_outcome import evaluate_price_window
from stockmind.domain.indicators.adx_indicator import ADXIndicator
from stockmind.domain.indicators.bollinger_indicator import BollingerIndicator
from stockmind.domain.indicators.ema_indicator import EMAIndicator
from stockmind.domain.indicators.indicator_engine import IndicatorEngine
from stockmind.domain.indicators.macd_indicator import MACDIndicator
from stockmind.domain.indicators.rsi_indicator import RSIIndicator
from stockmind.domain.indicators.sma_indicator import SMAIndicator
from stockmind.domain.indicators.stochastic_indicator import StochasticIndicator
from stockmind.domain.quality.quality_engine import QualityEngine
from stockmind.domain.risk.risk_engine import RiskEngine
from stockmind.domain.rules.rule_engine import RuleEngine
from stockmind.domain.scoring.opportunity_score_engine import OpportunityScoreEngine
from stockmind.domain.signals.signal_engine import SignalEngine
from stockmind.infrastructure.history.historical_opportunity_repository import HistoricalOpportunityRepository
from stockmind.infrastructure.profiles.profile_repository import ProfileRepository
from stockmind.infrastructure.rules.rule_set_repository import RuleSetRepository
from stockmind.shared.config.settings import Settings


class HistoricalOpportunityReplayUseCase:
    """Replay and incremental creation of historical opportunity entries.

    A historical score is calculated only with price data available up to the
    respective trading date. Later outcome fields are validation data only.
    """

    MIN_ROWS = 60

    def __init__(self, database_path: str | None = None):
        settings = Settings.load()
        self._database_path = database_path or settings.database_path

    def execute(
        self,
        symbol: str,
        profile_name: str,
        rule_set_name: str = "entry_setup",
        period: str = "5y",
    ) -> list[HistoricalOpportunityEntry]:
        symbol = symbol.upper().strip()
        data = self._load_data(symbol, period)
        repository = HistoricalOpportunityRepository(self._database_path)

        if data.empty:
            repository.replace_for(symbol, profile_name, [])
            return []

        entries = []
        for index in range(self.MIN_ROWS, len(data)):
            prefix = data.iloc[: index + 1]
            entry = self._build_entry(
                symbol=symbol,
                profile_name=profile_name,
                data=data,
                prefix=prefix,
                rule_set_name=rule_set_name,
            )
            if entry is not None:
                entries.append(entry)

        repository.replace_for(symbol, profile_name, entries)
        return entries

    def append_latest(
        self,
        symbol: str,
        profile_name: str,
        data: pd.DataFrame | None = None,
        rule_set_name: str = "entry_setup",
        period: str = "5y",
    ) -> HistoricalOpportunityEntry | None:
        """Persist exactly the newest missing replay day for one profile.

        Existing historical scores are never recalculated by this method.
        """
        symbol = symbol.upper().strip()
        data = self._normalize_data(data.copy()) if data is not None else self._load_data(symbol, period)
        if data.empty or len(data) <= self.MIN_ROWS:
            return None

        trading_date = data.index[-1].date().isoformat()
        repository = HistoricalOpportunityRepository(self._database_path)
        if repository.get_latest_date(symbol, profile_name) == trading_date:
            return None

        entry = self._build_entry(
            symbol=symbol,
            profile_name=profile_name,
            data=data,
            prefix=data,
            rule_set_name=rule_set_name,
        )
        if entry is not None:
            repository.upsert_entries([entry])
        return entry

    def _build_entry(self, symbol, profile_name, data, prefix, rule_set_name):
        trading_date = prefix.index[-1].date().isoformat()
        profile = ProfileRepository().get_by_name(profile_name, symbol=symbol)
        rule_set = RuleSetRepository().get_by_name(rule_set_name)
        indicator_engine = IndicatorEngine(indicators=[
            SMAIndicator(), EMAIndicator(), RSIIndicator(), MACDIndicator(),
            BollingerIndicator(), ADXIndicator(), StochasticIndicator(),
        ])

        try:
            indicators = indicator_engine.calculate(symbol=symbol, data=prefix)
            features = FeatureEngine().build(result=indicators, profile=profile)
            rules = RuleEngine(rule_set=rule_set).evaluate(features)
            core = CoreSetupEngine().evaluate(rules)
            quality = QualityEngine().calculate(
                rule_results=rules,
                core_setup_result=core,
            )
            evidence = self._evidence_before(
                symbol=symbol,
                profile_name=profile_name,
                trading_date=trading_date,
            )
            confidence = ConfidenceEngine().calculate(
                rule_results=rules,
                historical_success_result=evidence,
            )
            risk = RiskEngine().calculate(features)
            signal = SignalEngine().create_signal(
                symbol=symbol,
                quality_result=quality,
                confidence_result=confidence,
                risk_result=risk,
            )
            score = OpportunityScoreEngine().calculate(
                quality_result=quality,
                confidence_result=confidence,
                historical_success_result=evidence,
                risk_result=risk,
                profile=profile,
            )
        except (ValueError, ZeroDivisionError, KeyError, TypeError, IndexError):
            return None

        entry_price = float(prefix["Close"].iloc[-1])
        outcome = evaluate_price_window(
            data=data[["High", "Low", "Close"]],
            setup_date=trading_date,
            entry_price=entry_price,
            target_pct=0.08,
            lookahead_calendar_days=60,
            flat_threshold_pct=1.0,
        )
        return HistoricalOpportunityEntry(
            symbol=symbol,
            profile_name=profile_name,
            trading_date=trading_date,
            opportunity_score=score.score,
            confidence=confidence.confidence,
            historical_success_rate=evidence.success_rate,
            historical_sample_count=evidence.sample_count,
            historical_source=evidence.source,
            risk_level=risk.level,
            signal=signal.signal.value,
            quality=quality.quality,
            quality_component=score.quality_component,
            confidence_component=score.confidence_component,
            historical_component=score.historical_component,
            risk_component=score.risk_component,
            outcome=outcome.outcome.value,
            is_complete=outcome.is_complete,
            days_to_target=outcome.days_to_target,
            max_gain_pct=outcome.max_gain_pct,
            max_drawdown_pct=outcome.max_drawdown_pct,
        )

    def _load_data(self, symbol, period):
        return self._normalize_data(yf.Ticker(symbol).history(period=period).copy())

    def _normalize_data(self, data):
        if data.empty:
            return data
        if data.index.tz is not None:
            data.index = data.index.tz_localize(None)
        return data.sort_index()

    def _evidence_before(self, symbol: str, profile_name: str, trading_date: str):
        connection = sqlite3.connect(self._database_path)
        rows = connection.execute("""
            SELECT outcome
            FROM buy_periods
            WHERE symbol = ?
              AND profile_name = ?
              AND analysis_period = '5y'
              AND is_complete = 1
              AND window_end_date IS NOT NULL
              AND window_end_date <= ?
        """, (symbol, profile_name, trading_date)).fetchall()
        connection.close()

        sample_count = len(rows)
        target_hits = sum(1 for row in rows if row[0] == "TARGET_HIT")
        success_rate = target_hits / sample_count if sample_count else 0.0
        if sample_count >= 50:
            sample_quality = "HIGH"
        elif sample_count >= 20:
            sample_quality = "MEDIUM"
        elif sample_count > 0:
            sample_quality = "LOW"
        else:
            sample_quality = "NO_SAMPLE"

        return SimpleNamespace(
            success_rate=success_rate,
            sample_quality=sample_quality,
            sample_count=sample_count,
            source="BUY_PERIODS_REPLAY" if sample_count else "NO_SAMPLE",
        )
