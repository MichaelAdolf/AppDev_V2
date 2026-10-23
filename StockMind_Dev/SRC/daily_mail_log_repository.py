import sqlite3
from datetime import datetime
from stockmind.shared.config.settings import Settings

class DailyMailLogRepository:
    def __init__(self,database_path=None):
        self._database_path=database_path or Settings.load().database_path
        c=sqlite3.connect(self._database_path);c.execute("""CREATE TABLE IF NOT EXISTS daily_mail_log(trading_date TEXT PRIMARY KEY,sent_at TEXT NOT NULL,subject TEXT NOT NULL,status TEXT NOT NULL)""");c.commit();c.close()
    def was_sent(self,trading_date):
        if not trading_date:return False
        c=sqlite3.connect(self._database_path);r=c.execute("SELECT 1 FROM daily_mail_log WHERE trading_date=? AND status='SENT'",(trading_date,)).fetchone();c.close();return r is not None
    def mark_sent(self,trading_date,subject):
        if not trading_date:return
        c=sqlite3.connect(self._database_path);c.execute("INSERT OR REPLACE INTO daily_mail_log VALUES(?,?,?,'SENT')",(trading_date,datetime.now().isoformat(timespec='seconds'),subject));c.commit();c.close()
