import sqlite3
from stockmind.domain.history.historical_opportunity_entry import HistoricalOpportunityEntry
from stockmind.shared.config.settings import Settings


class HistoricalOpportunityRepository:
    def __init__(self, database_path: str | None = None):
        settings = Settings.load()
        self._database_path = database_path or settings.database_path
        self._initialize()

    def _connect(self):
        return sqlite3.connect(self._database_path)

    def _initialize(self):
        connection = self._connect()
        connection.execute("""
            CREATE TABLE IF NOT EXISTS historical_opportunities (
                symbol TEXT NOT NULL,
                profile_name TEXT NOT NULL,
                trading_date TEXT NOT NULL,
                opportunity_score REAL NOT NULL,
                confidence REAL NOT NULL,
                historical_success_rate REAL NOT NULL,
                historical_sample_count INTEGER NOT NULL,
                historical_source TEXT NOT NULL,
                risk_level TEXT NOT NULL,
                signal TEXT NOT NULL,
                quality TEXT NOT NULL,
                PRIMARY KEY (symbol, profile_name, trading_date)
            )
        """)
        connection.commit(); connection.close()

    def replace_for(self, symbol: str, profile_name: str, entries: list[HistoricalOpportunityEntry]):
        connection = self._connect(); cursor = connection.cursor()
        cursor.execute(
            "DELETE FROM historical_opportunities WHERE symbol = ? AND profile_name = ?",
            (symbol.upper(), profile_name),
        )
        cursor.executemany("""
            INSERT INTO historical_opportunities (
                symbol, profile_name, trading_date, opportunity_score,
                confidence, historical_success_rate, historical_sample_count,
                historical_source, risk_level, signal, quality
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, [(
            e.symbol, e.profile_name, e.trading_date, e.opportunity_score,
            e.confidence, e.historical_success_rate, e.historical_sample_count,
            e.historical_source, e.risk_level, e.signal, e.quality,
        ) for e in entries])
        connection.commit(); connection.close()

    def load_by_symbol(self, symbol: str, profile_name: str) -> list[HistoricalOpportunityEntry]:
        connection = self._connect()
        rows = connection.execute("""
            SELECT symbol, profile_name, trading_date, opportunity_score,
                   confidence, historical_success_rate, historical_sample_count,
                   historical_source, risk_level, signal, quality
            FROM historical_opportunities
            WHERE symbol = ? AND profile_name = ?
            ORDER BY trading_date
        """, (symbol.upper(), profile_name)).fetchall()
        connection.close()
        return [HistoricalOpportunityEntry(*row) for row in rows]
