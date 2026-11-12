import math,sqlite3
from stockmind.domain.history.chart_point import ChartPoint
from stockmind.shared.config.settings import Settings
class ChartDataRepository:
 EXTRA_COLUMNS={'open_price':'REAL','high_price':'REAL','low_price':'REAL','source_currency':"TEXT NOT NULL DEFAULT 'EUR'",'fx_rate_to_eur':'REAL NOT NULL DEFAULT 1.0','source_open_price':'REAL','source_high_price':'REAL','source_low_price':'REAL','source_close_price':'REAL'}
 def __init__(self,database_path=None):self._database_path=database_path or Settings.load().database_path;self._initialize()
 def _connect(self):return sqlite3.connect(self._database_path)
 def _initialize(self):
  c=self._connect();c.execute("""CREATE TABLE IF NOT EXISTS chart_data(symbol TEXT NOT NULL,trading_date TEXT NOT NULL,close_price REAL,bollinger_upper REAL,bollinger_middle REAL,bollinger_lower REAL,open_price REAL,high_price REAL,low_price REAL,source_currency TEXT NOT NULL DEFAULT 'EUR',fx_rate_to_eur REAL NOT NULL DEFAULT 1.0,source_open_price REAL,source_high_price REAL,source_low_price REAL,source_close_price REAL,PRIMARY KEY(symbol,trading_date))""");existing={r[1] for r in c.execute('PRAGMA table_info(chart_data)').fetchall()}
  for name,t in self.EXTRA_COLUMNS.items():
   if name not in existing:c.execute(f'ALTER TABLE chart_data ADD COLUMN {name} {t}')
  c.execute('DELETE FROM chart_data WHERE close_price IS NULL');c.commit();c.close()
 @staticmethod
 def _num(value):
  try:n=float(value);return n if math.isfinite(n) else None
  except (TypeError,ValueError):return None
 def replace_for_symbol(self,symbol,points):
  c=self._connect();c.execute('DELETE FROM chart_data WHERE symbol=?',(symbol.upper(),));self._write(c,points);c.commit();c.close()
 def upsert_points(self,points):
  if not points:return
  c=self._connect();self._write(c,points);c.commit();c.close()
 def _write(self,c,points):
  rows=[]
  for p in points:
   close=self._num(p.close_price)
   if close is None:continue
   rows.append((p.symbol.upper(),p.trading_date,close,self._num(p.bollinger_upper),self._num(p.bollinger_middle),self._num(p.bollinger_lower),self._num(p.open_price),self._num(p.high_price),self._num(p.low_price),p.source_currency.upper(),float(p.fx_rate_to_eur),self._num(p.source_open_price),self._num(p.source_high_price),self._num(p.source_low_price),self._num(p.source_close_price)))
  c.executemany('INSERT OR REPLACE INTO chart_data VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',rows)
 def get_latest_date(self,symbol):
  c=self._connect();r=c.execute('SELECT MAX(trading_date) FROM chart_data WHERE symbol=? AND close_price IS NOT NULL',(symbol.upper(),)).fetchone();c.close();return r[0] if r else None
 def load_by_symbol(self,symbol):
  c=self._connect();rows=c.execute('SELECT symbol,trading_date,close_price,bollinger_upper,bollinger_middle,bollinger_lower,open_price,high_price,low_price,source_currency,fx_rate_to_eur,source_open_price,source_high_price,source_low_price,source_close_price FROM chart_data WHERE symbol=? AND close_price IS NOT NULL ORDER BY trading_date',(symbol.upper(),)).fetchall();c.close();return [ChartPoint(*r) for r in rows if self._num(r[2]) is not None]
 def has_complete_ohlc(self,symbol):
  c=self._connect();r=c.execute("SELECT COUNT(*),SUM(CASE WHEN open_price IS NOT NULL AND high_price IS NOT NULL AND low_price IS NOT NULL THEN 1 ELSE 0 END) FROM chart_data WHERE symbol=? AND close_price IS NOT NULL",(symbol.upper(),)).fetchone();c.close();total,complete=r or (0,0);return total>0 and total==complete
