import json
import sqlite3

from stockmind.domain.history.daily_buy_signal import DailyBuySignal
from stockmind.shared.config.settings import Settings


class DailyBuySignalRepository:
    def __init__(self, database_path: str | None = None):
        settings = Settings.load()
        self._database_path = database_path or settings.database_path
        self._initialize()

    def _connect(self):
        return sqlite3.connect(self._database_path)

    def _initialize(self):
        connection = self._connect()
        try:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS daily_buy_signals (
                    symbol TEXT NOT NULL,
                    profile_name TEXT NOT NULL,
                    analysis_period TEXT NOT NULL,
                    trading_date TEXT NOT NULL,
                    is_buy INTEGER NOT NULL,
                    quality TEXT NOT NULL,
                    quality_score REAL NOT NULL,
                    core_setup_detected INTEGER NOT NULL,
                    satisfied_rules INTEGER NOT NULL,
                    required_rules INTEGER NOT NULL,
                    reasons_json TEXT NOT NULL,
                    missing_rules_json TEXT NOT NULL,
                    entry_price REAL NOT NULL,
                    PRIMARY KEY (
                        symbol,
                        profile_name,
                        analysis_period,
                        trading_date
                    )
                )
                """
            )
            connection.commit()
        finally:
            connection.close()

    def replace_for(
        self,
        symbol: str,
        profile_name: str,
        analysis_period: str,
        signals: list[DailyBuySignal],
    ):
        connection = self._connect()
        try:
            cursor = connection.cursor()
            cursor.execute(
                """
                DELETE FROM daily_buy_signals
                WHERE symbol = ?
                AND profile_name = ?
                AND analysis_period = ?
                """,
                (symbol.upper(), profile_name, analysis_period),
            )
            cursor.executemany(
                """
                INSERT INTO daily_buy_signals (
                    symbol,
                    profile_name,
                    analysis_period,
                    trading_date,
                    is_buy,
                    quality,
                    quality_score,
                    core_setup_detected,
                    satisfied_rules,
                    required_rules,
                    reasons_json,
                    missing_rules_json,
                    entry_price
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                [self._to_row(signal) for signal in signals],
            )
            connection.commit()
        finally:
            connection.close()

    def load_by_symbol(
        self,
        symbol: str,
        profile_name: str,
        analysis_period: str = "1y",
        buy_only: bool = False,
    ) -> list[DailyBuySignal]:
        query = """
            SELECT
                symbol,
                profile_name,
                analysis_period,
                trading_date,
                is_buy,
                quality,
                quality_score,
                core_setup_detected,
                satisfied_rules,
                required_rules,
                reasons_json,
                missing_rules_json,
                entry_price
            FROM daily_buy_signals
            WHERE symbol = ?
            AND profile_name = ?
            AND analysis_period = ?
        """
        parameters: list = [symbol.upper(), profile_name, analysis_period]
        if buy_only:
            query += " AND is_buy = 1"
        query += " ORDER BY trading_date ASC"

        connection = self._connect()
        try:
            rows = connection.execute(query, parameters).fetchall()
        finally:
            connection.close()
        return [self._from_row(row) for row in rows]

    def load_latest(
        self,
        symbol: str,
        profile_name: str,
        analysis_period: str = "5y",
    ) -> DailyBuySignal | None:
        connection = self._connect()
        try:
            row = connection.execute(
                """
                SELECT
                    symbol,
                    profile_name,
                    analysis_period,
                    trading_date,
                    is_buy,
                    quality,
                    quality_score,
                    core_setup_detected,
                    satisfied_rules,
                    required_rules,
                    reasons_json,
                    missing_rules_json,
                    entry_price
                FROM daily_buy_signals
                WHERE symbol = ?
                AND profile_name = ?
                AND analysis_period = ?
                ORDER BY trading_date DESC
                LIMIT 1
                """,
                (symbol.upper(), profile_name, analysis_period),
            ).fetchone()
        finally:
            connection.close()
        return self._from_row(row) if row else None

    def _to_row(self, signal: DailyBuySignal) -> tuple:
        return (
            signal.symbol,
            signal.profile_name,
            signal.analysis_period,
            signal.trading_date,
            int(signal.is_buy),
            signal.quality,
            signal.quality_score,
            int(signal.core_setup_detected),
            signal.satisfied_rules,
            signal.required_rules,
            json.dumps(signal.reasons, ensure_ascii=False),
            json.dumps(signal.missing_rules, ensure_ascii=False),
            signal.entry_price,
        )

    def _from_row(self, row) -> DailyBuySignal:
        return DailyBuySignal(
            symbol=row[0],
            profile_name=row[1],
            analysis_period=row[2],
            trading_date=row[3],
            is_buy=bool(row[4]),
            quality=row[5],
            quality_score=row[6],
            core_setup_detected=bool(row[7]),
            satisfied_rules=row[8],
            required_rules=row[9],
            reasons=json.loads(row[10]),
            missing_rules=json.loads(row[11]),
            entry_price=row[12],
        )
