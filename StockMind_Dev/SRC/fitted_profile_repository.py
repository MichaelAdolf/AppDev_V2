import sqlite3
from stockmind.domain.strategy.fitted_profile import FittedProfile
from stockmind.shared.config.settings import Settings
class FittedProfileRepository:
 def __init__(self,database_path=None):self._database_path=database_path or Settings.load().database_path;self._initialize()
 def _connect(self):c=sqlite3.connect(self._database_path);c.row_factory=sqlite3.Row;return c
 def _initialize(self):
  c=self._connect();c.execute("""CREATE TABLE IF NOT EXISTS fitted_profiles(id TEXT PRIMARY KEY,symbol TEXT NOT NULL,version INTEGER NOT NULL,status TEXT NOT NULL,base_profile TEXT NOT NULL,rsi_oversold_threshold REAL NOT NULL,rsi_overbought_threshold REAL NOT NULL,bollinger_lower_threshold REAL NOT NULL,adx_trend_strength_threshold REAL NOT NULL,stochastic_oversold_threshold REAL NOT NULL,created_at TEXT NOT NULL,UNIQUE(symbol,version))""");c.execute("""CREATE TABLE IF NOT EXISTS fitted_profile_validations(profile_id TEXT PRIMARY KEY,status TEXT NOT NULL,train_sample_count INTEGER NOT NULL,validation_sample_count INTEGER NOT NULL,train_target_hit_rate REAL NOT NULL,validation_target_hit_rate REAL NOT NULL,benchmark_target_hit_rate REAL NOT NULL,stable_fold_rate REAL NOT NULL,reasons TEXT NOT NULL,validated_at TEXT NOT NULL)""");c.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_one_active_fitted_per_symbol ON fitted_profiles(symbol) WHERE status='ACTIVE'");c.commit();c.close()
 def next_version(self,symbol):
  c=self._connect();r=c.execute('SELECT COALESCE(MAX(version),0)+1 FROM fitted_profiles WHERE symbol=?',(symbol.upper(),)).fetchone();c.close();return r[0]
 def save(self,p):
  c=self._connect();c.execute('INSERT OR REPLACE INTO fitted_profiles VALUES(?,?,?,?,?,?,?,?,?,?,?)',(p.id,p.symbol,p.version,p.status,p.base_profile,p.rsi_oversold_threshold,p.rsi_overbought_threshold,p.bollinger_lower_threshold,p.adx_trend_strength_threshold,p.stochastic_oversold_threshold,p.created_at));c.commit();c.close()
 def load_by_symbol(self,symbol):
  c=self._connect();rows=c.execute('SELECT * FROM fitted_profiles WHERE symbol=? ORDER BY version DESC',(symbol.upper(),)).fetchall();c.close();return [FittedProfile(**dict(r)) for r in rows]
 def load(self,profile_id):
  c=self._connect();r=c.execute('SELECT * FROM fitted_profiles WHERE id=?',(profile_id,)).fetchone();c.close();return FittedProfile(**dict(r)) if r else None
 def update_status(self,profile_id,status):
  c=self._connect();c.execute('UPDATE fitted_profiles SET status=? WHERE id=?',(status,profile_id));c.commit();c.close()
 def save_validation(self,profile_id,status,train_n,val_n,train_rate,val_rate,benchmark_rate,fold_rate,reasons,validated_at):
  c=self._connect();c.execute('INSERT OR REPLACE INTO fitted_profile_validations VALUES(?,?,?,?,?,?,?,?,?,?)',(profile_id,status,train_n,val_n,train_rate,val_rate,benchmark_rate,fold_rate,'|'.join(reasons),validated_at));c.commit();c.close()
 def load_validation(self,profile_id):
  c=self._connect();r=c.execute('SELECT * FROM fitted_profile_validations WHERE profile_id=?',(profile_id,)).fetchone();c.close();return dict(r) if r else None
 def activate(self,profile_id,symbol):
  c=self._connect()
  try:
   c.execute('BEGIN');row=c.execute('SELECT status FROM fitted_profiles WHERE id=? AND symbol=?',(profile_id,symbol.upper())).fetchone()
   if not row or row[0]!='VALIDATED':raise ValueError('Nur ein VALIDATED Fitted Profile darf aktiviert werden.')
   c.execute("UPDATE fitted_profiles SET status='VALIDATED' WHERE symbol=? AND status='ACTIVE'",(symbol.upper(),));c.execute("UPDATE fitted_profiles SET status='ACTIVE' WHERE id=?",(profile_id,));c.commit()
  except Exception:c.rollback();raise
  finally:c.close()
 def deactivate_symbol(self,symbol):
  c=self._connect();c.execute("UPDATE fitted_profiles SET status='VALIDATED' WHERE symbol=? AND status='ACTIVE'",(symbol.upper(),));c.commit();c.close()
 def load_active(self,symbol):
  c=self._connect();r=c.execute("SELECT * FROM fitted_profiles WHERE symbol=? AND status='ACTIVE' ORDER BY version DESC LIMIT 1",(symbol.upper(),)).fetchone();c.close();return FittedProfile(**dict(r)) if r else None
