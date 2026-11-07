import sqlite3

from stockmind.domain.strategy.fitted_profile import FittedProfile
from stockmind.shared.config.settings import Settings


class FittedProfileRepository:
    def __init__(self, database_path=None):
        self._database_path = database_path or Settings.load().database_path
        self._initialize()

    def _connect(self):
        connection = sqlite3.connect(self._database_path)
        connection.row_factory = sqlite3.Row
        return connection

    def _initialize(self):
        connection = self._connect()
        try:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS fitted_profiles (
                    id TEXT PRIMARY KEY,
                    symbol TEXT NOT NULL,
                    version INTEGER NOT NULL,
                    status TEXT NOT NULL,
                    base_profile TEXT NOT NULL,
                    rsi_oversold_threshold REAL NOT NULL,
                    rsi_overbought_threshold REAL NOT NULL,
                    bollinger_lower_threshold REAL NOT NULL,
                    adx_trend_strength_threshold REAL NOT NULL,
                    stochastic_oversold_threshold REAL NOT NULL,
                    created_at TEXT NOT NULL,
                    UNIQUE(symbol, version)
                )
                """
            )
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS fitted_profile_validations (
                    profile_id TEXT PRIMARY KEY,
                    status TEXT NOT NULL,
                    train_sample_count INTEGER NOT NULL,
                    validation_sample_count INTEGER NOT NULL,
                    train_target_hit_rate REAL NOT NULL,
                    validation_target_hit_rate REAL NOT NULL,
                    benchmark_target_hit_rate REAL NOT NULL,
                    stable_fold_rate REAL NOT NULL,
                    reasons TEXT NOT NULL,
                    validated_at TEXT NOT NULL
                )
                """
            )
            connection.commit()
        finally:
            connection.close()

    def next_version(self, symbol):
        connection = self._connect()
        try:
            row = connection.execute(
                "SELECT COALESCE(MAX(version), 0) + 1 FROM fitted_profiles WHERE symbol = ?",
                (symbol.upper(),),
            ).fetchone()
            return row[0]
        finally:
            connection.close()

    def save(self, profile):
        connection = self._connect()
        try:
            connection.execute(
                "INSERT OR REPLACE INTO fitted_profiles VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    profile.id,
                    profile.symbol,
                    profile.version,
                    profile.status,
                    profile.base_profile,
                    profile.rsi_oversold_threshold,
                    profile.rsi_overbought_threshold,
                    profile.bollinger_lower_threshold,
                    profile.adx_trend_strength_threshold,
                    profile.stochastic_oversold_threshold,
                    profile.created_at,
                ),
            )
            connection.commit()
        finally:
            connection.close()

    def load_by_symbol(self, symbol):
        connection = self._connect()
        try:
            rows = connection.execute(
                "SELECT * FROM fitted_profiles WHERE symbol = ? ORDER BY version DESC",
                (symbol.upper(),),
            ).fetchall()
            return [FittedProfile(**dict(row)) for row in rows]
        finally:
            connection.close()

    def load(self, profile_id: str) -> FittedProfile | None:
        connection = self._connect()
        try:
            row = connection.execute(
                "SELECT * FROM fitted_profiles WHERE id = ?",
                (profile_id,),
            ).fetchone()
        finally:
            connection.close()

        return FittedProfile(**dict(row)) if row else None

    def update_status(self, profile_id: str, status: str):
        connection = self._connect()
        try:
            connection.execute(
                "UPDATE fitted_profiles SET status = ? WHERE id = ?",
                (status, profile_id),
            )
            connection.commit()
        finally:
            connection.close()

    def save_validation(
        self,
        profile_id: str,
        status: str,
        train_n: int,
        val_n: int,
        train_rate: float,
        val_rate: float,
        benchmark_rate: float,
        fold_rate: float,
        reasons: list[str],
        validated_at: str,
    ):
        connection = self._connect()
        try:
            connection.execute(
                """
                INSERT OR REPLACE INTO fitted_profile_validations (
                    profile_id,
                    status,
                    train_sample_count,
                    validation_sample_count,
                    train_target_hit_rate,
                    validation_target_hit_rate,
                    benchmark_target_hit_rate,
                    stable_fold_rate,
                    reasons,
                    validated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    profile_id,
                    status,
                    train_n,
                    val_n,
                    train_rate,
                    val_rate,
                    benchmark_rate,
                    fold_rate,
                    "|".join(reasons),
                    validated_at,
                ),
            )
            connection.commit()
        finally:
            connection.close()

    def load_active(self, symbol):
        connection = self._connect()
        try:
            row = connection.execute(
                """
                SELECT *
                FROM fitted_profiles
                WHERE symbol = ? AND status = 'ACTIVE'
                ORDER BY version DESC
                LIMIT 1
                """,
                (symbol.upper(),),
            ).fetchone()
            return FittedProfile(**dict(row)) if row else None
        finally:
            connection.close()
