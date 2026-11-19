import sqlite3
from stockmind.domain.portfolio.portfolio_position import PortfolioPosition
from stockmind.domain.portfolio.portfolio_purchase_lot import PortfolioPurchaseLot
from stockmind.domain.portfolio.portfolio_trade import PortfolioTrade
from stockmind.shared.config.settings import Settings

class PortfolioRepository:
    def __init__(self,database_path=None):
        self._database_path=database_path or Settings.load().database_path
        self._initialize();self._migrate_existing_positions_to_lots();self._merge_duplicate_open_positions();self._ensure_open_symbol_index()
    def _connect(self):
        c=sqlite3.connect(self._database_path);c.row_factory=sqlite3.Row;c.execute('PRAGMA foreign_keys=ON');return c
    def _initialize(self):
        c=self._connect();c.executescript("""
        CREATE TABLE IF NOT EXISTS portfolio_positions(
          id TEXT PRIMARY KEY,symbol TEXT NOT NULL,company_name TEXT NOT NULL,
          purchase_date TEXT NOT NULL,purchase_price REAL NOT NULL,quantity REAL NOT NULL,
          purchase_fees REAL NOT NULL DEFAULT 0,entry_profile TEXT NOT NULL,entry_signal TEXT,
          entry_opportunity_score REAL,entry_confidence REAL,entry_risk TEXT,
          entry_target_hit_rate REAL,entry_sample_count INTEGER NOT NULL DEFAULT 0,
          entry_profile_buy_count INTEGER NOT NULL DEFAULT 0,entry_buy_period_start TEXT,
          note TEXT NOT NULL DEFAULT '',status TEXT NOT NULL DEFAULT 'OPEN',created_at TEXT NOT NULL,updated_at TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS portfolio_purchase_lots(
          id TEXT PRIMARY KEY,position_id TEXT NOT NULL,symbol TEXT NOT NULL,purchase_date TEXT NOT NULL,
          purchase_price REAL NOT NULL,quantity REAL NOT NULL,purchase_fees REAL NOT NULL DEFAULT 0,
          entry_profile TEXT NOT NULL,entry_signal TEXT,entry_opportunity_score REAL,entry_confidence REAL,
          entry_risk TEXT,entry_target_hit_rate REAL,entry_sample_count INTEGER NOT NULL DEFAULT 0,
          entry_profile_buy_count INTEGER NOT NULL DEFAULT 0,entry_buy_period_start TEXT,note TEXT NOT NULL DEFAULT '',
          created_at TEXT NOT NULL,updated_at TEXT NOT NULL,
          FOREIGN KEY(position_id) REFERENCES portfolio_positions(id) ON DELETE CASCADE);
        CREATE INDEX IF NOT EXISTS idx_portfolio_lots_position ON portfolio_purchase_lots(position_id,purchase_date);
        CREATE TABLE IF NOT EXISTS portfolio_trades(
          id TEXT PRIMARY KEY,position_id TEXT NOT NULL,symbol TEXT NOT NULL,company_name TEXT NOT NULL,
          purchase_date TEXT NOT NULL,purchase_price REAL NOT NULL,sale_date TEXT NOT NULL,sale_price REAL NOT NULL,
          quantity REAL NOT NULL,purchase_fees REAL NOT NULL,sale_fees REAL NOT NULL,tax_paid REAL NOT NULL,
          gross_profit REAL NOT NULL,profit_after_fees REAL NOT NULL,net_profit REAL NOT NULL,
          gross_return_pct REAL NOT NULL,net_return_pct REAL NOT NULL,holding_days INTEGER NOT NULL,
          entry_profile TEXT NOT NULL,entry_signal TEXT,entry_opportunity_score REAL,exit_reason TEXT NOT NULL,
          note TEXT NOT NULL DEFAULT '',created_at TEXT NOT NULL);
        CREATE INDEX IF NOT EXISTS idx_portfolio_trades_sale_date ON portfolio_trades(sale_date,symbol);
        """);c.commit();c.close()
    def _migrate_existing_positions_to_lots(self):
        c=self._connect()
        try:
            rows=c.execute("""SELECT p.* FROM portfolio_positions p WHERE NOT EXISTS(
              SELECT 1 FROM portfolio_purchase_lots l WHERE l.position_id=p.id)""").fetchall()
            for r in rows:
                c.execute("""INSERT INTO portfolio_purchase_lots VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",(
                  'legacy-'+r['id'],r['id'],r['symbol'],r['purchase_date'],r['purchase_price'],r['quantity'],r['purchase_fees'],
                  r['entry_profile'],r['entry_signal'],r['entry_opportunity_score'],r['entry_confidence'],r['entry_risk'],
                  r['entry_target_hit_rate'],r['entry_sample_count'],r['entry_profile_buy_count'],r['entry_buy_period_start'],
                  r['note'],r['created_at'],r['updated_at']))
            c.commit()
        finally:c.close()
    def _merge_duplicate_open_positions(self):
        c=self._connect()
        try:
            symbols=c.execute("""SELECT symbol FROM portfolio_positions WHERE status='OPEN' GROUP BY symbol HAVING COUNT(*)>1""").fetchall()
            for symbol_row in symbols:
                rows=c.execute("""SELECT id FROM portfolio_positions WHERE symbol=? AND status='OPEN' ORDER BY created_at,id""",(symbol_row[0],)).fetchall()
                keeper=rows[0][0]
                for duplicate in rows[1:]:
                    c.execute("UPDATE portfolio_purchase_lots SET position_id=? WHERE position_id=?",(keeper,duplicate[0]))
                    c.execute("DELETE FROM portfolio_positions WHERE id=?",(duplicate[0],))
            c.commit()
        finally:c.close()
    def _ensure_open_symbol_index(self):
        c=self._connect();c.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_one_open_position_per_symbol ON portfolio_positions(symbol) WHERE status='OPEN'");c.commit();c.close()
    def find_open_position_by_symbol(self,symbol):
        c=self._connect();r=c.execute("SELECT * FROM portfolio_positions WHERE symbol=? AND status='OPEN'",(symbol.upper(),)).fetchone();c.close();return self._position_from_row(r) if r else None
    def add_position(self,p):
        c=self._connect();c.execute("""INSERT INTO portfolio_positions VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",self._position_row(p));c.commit();c.close()
    def add_purchase_lot(self,l):
        c=self._connect();c.execute("INSERT INTO portfolio_purchase_lots VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",self._lot_row(l));c.commit();c.close()
    def update_purchase_lot(self,l):
        c=self._connect();c.execute("""UPDATE portfolio_purchase_lots SET purchase_date=?,purchase_price=?,quantity=?,purchase_fees=?,entry_profile=?,note=?,updated_at=? WHERE id=?""",(l.purchase_date,l.purchase_price,l.quantity,l.purchase_fees,l.entry_profile,l.note,l.updated_at,l.id));c.commit();c.close()
    def load_lot(self,lot_id):
        c=self._connect();r=c.execute("SELECT * FROM portfolio_purchase_lots WHERE id=?",(lot_id,)).fetchone();c.close();return self._lot_from_row(r) if r else None
    def load_lots_for_position(self,position_id):
        c=self._connect();rows=c.execute("SELECT * FROM portfolio_purchase_lots WHERE position_id=? ORDER BY purchase_date,created_at",(position_id,)).fetchall();c.close();return [self._lot_from_row(r) for r in rows]
    def delete_purchase_lot(self,lot_id):
        c=self._connect();r=c.execute("SELECT position_id FROM portfolio_purchase_lots WHERE id=?",(lot_id,)).fetchone()
        if not r:c.close();raise ValueError('Kauftranche wurde nicht gefunden.')
        pid=r[0];c.execute("DELETE FROM portfolio_purchase_lots WHERE id=?",(lot_id,))
        remaining=c.execute("SELECT COUNT(*) FROM portfolio_purchase_lots WHERE position_id=?",(pid,)).fetchone()[0]
        if remaining==0:c.execute("DELETE FROM portfolio_positions WHERE id=? AND status='OPEN'",(pid,))
        c.commit();c.close()
    def delete_open_position(self,position_id):
        c=self._connect();cur=c.execute("DELETE FROM portfolio_positions WHERE id=? AND status='OPEN'",(position_id,));c.commit();c.close()
        if cur.rowcount!=1:raise ValueError('Offene Position wurde nicht gefunden.')
    def delete_trade(self,trade_id):
        c=self._connect();cur=c.execute("DELETE FROM portfolio_trades WHERE id=?",(trade_id,));c.commit();c.close()
        if cur.rowcount!=1:raise ValueError('Trade wurde nicht gefunden.')
    def load_position(self,pid):
        c=self._connect();r=c.execute("SELECT * FROM portfolio_positions WHERE id=?",(pid,)).fetchone();c.close();return self._position_from_row(r) if r else None
    def load_open_positions(self):
        c=self._connect();rows=c.execute("SELECT * FROM portfolio_positions WHERE status='OPEN' ORDER BY symbol").fetchall();c.close();return [self._aggregate_position(self._position_from_row(r)) for r in rows]
    def _aggregate_position(self,p):
        lots=self.load_lots_for_position(p.id)
        if not lots:return p
        qty=sum(x.quantity for x in lots);value=sum(x.purchase_price*x.quantity for x in lots);fees=sum(x.purchase_fees for x in lots);first=min(lots,key=lambda x:x.purchase_date)
        return PortfolioPosition(p.id,p.symbol,p.company_name,first.purchase_date,value/qty,qty,fees,first.entry_profile,first.entry_signal,first.entry_opportunity_score,first.entry_confidence,first.entry_risk,first.entry_target_hit_rate,first.entry_sample_count,first.entry_profile_buy_count,first.entry_buy_period_start,p.note,p.status,p.created_at,p.updated_at)
    def close_position(self,pid,updated_at,trade):
        c=self._connect();c.execute('BEGIN')
        try:
            cur=c.execute("UPDATE portfolio_positions SET status='CLOSED',updated_at=? WHERE id=? AND status='OPEN'",(updated_at,pid))
            if cur.rowcount!=1:raise ValueError('Position wurde nicht gefunden oder ist bereits geschlossen.')
            c.execute("INSERT INTO portfolio_trades VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",self._trade_row(trade));c.commit()
        except Exception:c.rollback();raise
        finally:c.close()
    def load_trades(self):
        c=self._connect();rows=c.execute("SELECT * FROM portfolio_trades ORDER BY sale_date DESC,symbol").fetchall();c.close();return [PortfolioTrade(**dict(r)) for r in rows]
    def _position_row(self,p):return (p.id,p.symbol,p.company_name,p.purchase_date,p.purchase_price,p.quantity,p.purchase_fees,p.entry_profile,p.entry_signal,p.entry_opportunity_score,p.entry_confidence,p.entry_risk,p.entry_target_hit_rate,p.entry_sample_count,p.entry_profile_buy_count,p.entry_buy_period_start,p.note,p.status,p.created_at,p.updated_at)
    def _lot_row(self,l):return (l.id,l.position_id,l.symbol,l.purchase_date,l.purchase_price,l.quantity,l.purchase_fees,l.entry_profile,l.entry_signal,l.entry_opportunity_score,l.entry_confidence,l.entry_risk,l.entry_target_hit_rate,l.entry_sample_count,l.entry_profile_buy_count,l.entry_buy_period_start,l.note,l.created_at,l.updated_at)
    def _trade_row(self,t):return (t.id,t.position_id,t.symbol,t.company_name,t.purchase_date,t.purchase_price,t.sale_date,t.sale_price,t.quantity,t.purchase_fees,t.sale_fees,t.tax_paid,t.gross_profit,t.profit_after_fees,t.net_profit,t.gross_return_pct,t.net_return_pct,t.holding_days,t.entry_profile,t.entry_signal,t.entry_opportunity_score,t.exit_reason,t.note,t.created_at)
    def _position_from_row(self,r):return PortfolioPosition(**dict(r))
    def _lot_from_row(self,r):return PortfolioPurchaseLot(**dict(r))
