import sqlite3
from stockmind.domain.history.historical_opportunity_entry import HistoricalOpportunityEntry
from stockmind.shared.config.settings import Settings


class HistoricalOpportunityRepository:
    COLUMNS={
        "quality_component":"REAL DEFAULT 0","confidence_component":"REAL DEFAULT 0",
        "historical_component":"REAL DEFAULT 0","risk_component":"REAL DEFAULT 0",
        "outcome":"TEXT DEFAULT 'INCOMPLETE_WINDOW'","is_complete":"INTEGER DEFAULT 0",
        "days_to_target":"INTEGER","max_gain_pct":"REAL","max_drawdown_pct":"REAL",
    }
    def __init__(self,database_path=None):
        self._database_path=database_path or Settings.load().database_path;self._initialize()
    def _connect(self):return sqlite3.connect(self._database_path)
    def _initialize(self):
        c=self._connect();c.execute("""CREATE TABLE IF NOT EXISTS historical_opportunities (
        symbol TEXT NOT NULL,profile_name TEXT NOT NULL,trading_date TEXT NOT NULL,
        opportunity_score REAL NOT NULL,confidence REAL NOT NULL,historical_success_rate REAL NOT NULL,
        historical_sample_count INTEGER NOT NULL,historical_source TEXT NOT NULL,risk_level TEXT NOT NULL,
        signal TEXT NOT NULL,quality TEXT NOT NULL,quality_component REAL DEFAULT 0,
        confidence_component REAL DEFAULT 0,historical_component REAL DEFAULT 0,risk_component REAL DEFAULT 0,
        outcome TEXT DEFAULT 'INCOMPLETE_WINDOW',is_complete INTEGER DEFAULT 0,days_to_target INTEGER,
        max_gain_pct REAL,max_drawdown_pct REAL,PRIMARY KEY(symbol,profile_name,trading_date))""")
        existing={r[1] for r in c.execute("PRAGMA table_info(historical_opportunities)").fetchall()}
        for n,t in self.COLUMNS.items():
            if n not in existing:c.execute(f"ALTER TABLE historical_opportunities ADD COLUMN {n} {t}")
        c.commit();c.close()
    def replace_for(self,symbol,profile_name,entries):
        c=self._connect();c.execute("DELETE FROM historical_opportunities WHERE symbol=? AND profile_name=?",(symbol.upper(),profile_name))
        c.executemany("""INSERT INTO historical_opportunities VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",[
        (e.symbol,e.profile_name,e.trading_date,e.opportunity_score,e.confidence,e.historical_success_rate,
        e.historical_sample_count,e.historical_source,e.risk_level,e.signal,e.quality,e.quality_component,
        e.confidence_component,e.historical_component,e.risk_component,e.outcome,int(e.is_complete),
        e.days_to_target,e.max_gain_pct,e.max_drawdown_pct) for e in entries])
        c.commit();c.close()
    def load_by_symbol(self,symbol,profile_name):
        c=self._connect();rows=c.execute("SELECT * FROM historical_opportunities WHERE symbol=? AND profile_name=? ORDER BY trading_date",(symbol.upper(),profile_name)).fetchall();c.close()
        return [HistoricalOpportunityEntry(*tuple(list(r[:16])+[bool(r[16])]+list(r[17:]))) for r in rows]
