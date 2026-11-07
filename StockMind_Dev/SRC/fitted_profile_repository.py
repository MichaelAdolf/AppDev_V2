import sqlite3
from stockmind.domain.strategy.fitted_profile import FittedProfile
from stockmind.shared.config.settings import Settings
class FittedProfileRepository:
 def __init__(self,database_path=None):self._database_path=database_path or Settings.load().database_path;self._initialize()
 def _connect(self):c=sqlite3.connect(self._database_path);c.row_factory=sqlite3.Row;return c
 def _initialize(self):
  c=self._connect();c.execute("""CREATE TABLE IF NOT EXISTS fitted_profiles(id TEXT PRIMARY KEY,symbol TEXT NOT NULL,version INTEGER NOT NULL,status TEXT NOT NULL,base_profile TEXT NOT NULL,rsi_oversold_threshold REAL NOT NULL,rsi_overbought_threshold REAL NOT NULL,bollinger_lower_threshold REAL NOT NULL,adx_trend_strength_threshold REAL NOT NULL,stochastic_oversold_threshold REAL NOT NULL,created_at TEXT NOT NULL,UNIQUE(symbol,version))""");c.commit();c.close()
 def next_version(self,symbol):
  c=self._connect();row=c.execute('SELECT COALESCE(MAX(version),0)+1 FROM fitted_profiles WHERE symbol=?',(symbol.upper(),)).fetchone();c.close();return row[0]
 def save(self,p):
  c=self._connect();c.execute('INSERT OR REPLACE INTO fitted_profiles VALUES(?,?,?,?,?,?,?,?,?,?,?)',(p.id,p.symbol,p.version,p.status,p.base_profile,p.rsi_oversold_threshold,p.rsi_overbought_threshold,p.bollinger_lower_threshold,p.adx_trend_strength_threshold,p.stochastic_oversold_threshold,p.created_at));c.commit();c.close()
 def load_by_symbol(self,symbol):
  c=self._connect();rows=c.execute('SELECT * FROM fitted_profiles WHERE symbol=? ORDER BY version DESC',(symbol.upper(),)).fetchall();c.close();return [FittedProfile(**dict(r)) for r in rows]
 def load_active(self,symbol):
  c=self._connect();r=c.execute("SELECT * FROM fitted_profiles WHERE symbol=? AND status='ACTIVE' ORDER BY version DESC LIMIT 1",(symbol.upper(),)).fetchone();c.close();return FittedProfile(**dict(r)) if r else None
