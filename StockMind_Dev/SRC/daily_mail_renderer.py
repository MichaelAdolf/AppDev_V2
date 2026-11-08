from html import escape
class DailyMailRenderer:
 PROFILE_LABELS={'conservative':'Conservative','balanced':'Balanced','aggressive':'Aggressive'}
 def render(self,r):return f"""<!doctype html><html><body style='font-family:Arial,sans-serif;color:#222;max-width:1100px;margin:auto'><h1>StockMind Daily Trading Briefing</h1><p><b>Datenstand:</b> {escape(r.trading_date or '-')}</p><h2>Aktuelle Kaufsignale</h2>{self._stocks(r.buy_signal_stocks,'Keine BUY-Signale.')}<h2>Exit Intelligence</h2>{self._exit(r.portfolio_items)}<h2>Portfolio</h2><p>Investiert {r.portfolio_invested:,.2f} € | Marktwert {r.portfolio_market_value:,.2f} € | Unrealisiert {r.portfolio_unrealized:+,.2f} € | Realisiert YTD {r.portfolio_realized_ytd:+,.2f} €</p><h2>Gesamte Watchlist</h2>{self._stocks(r.watchlist,'Keine Watchlist-Daten.')}</body></html>"""
 def _stocks(self,rows,empty):
  if not rows:return f'<p>{escape(empty)}</p>'
  head=''.join(f'<th>{self.PROFILE_LABELS[p]}</th>' for p in ('conservative','balanced','aggressive'))+'<th>Fitted</th>';body=[]
  for row in rows:
   by={p.profile_name:p for p in row.profiles};cells=''.join(self._signal(by.get(p)) for p in ('conservative','balanced','aggressive'));fitted=(f'<b>{escape(row.fitted_strategy_name or "Fitted")}</b><br>{escape(row.fitted_signal or "-")}<br><small>Basis {escape(row.fitted_base_profile or "-")}</small>' if row.fitted_active else '–');body.append(f'<tr><td><b>{escape(row.company_name)}</b><br>{escape(row.symbol)}</td>{cells}<td>{fitted}</td></tr>')
  return f"<table border='1' cellpadding='7' cellspacing='0' style='border-collapse:collapse;width:100%'><tr><th>Aktie</th>{head}</tr>{''.join(body)}</table>"
 def _signal(self,p):
  if not p:return '<td>–</td>'
  evidence='kein vollständiges Sample' if p.complete_period_count==0 else f'{p.target_hit_rate:.0%} · {p.complete_period_count} Perioden';return f'<td><b>{escape(p.signal)}</b><br><small>{evidence}</small></td>'
 def _exit(self,items):
  rows=[x for x in items if x.exit_status=='EXIT_REVIEW']
  return '<p>Keine Exit-Prüfung.</p>' if not rows else ''.join(f'<p><b>{escape(x.company_name)} ({escape(x.symbol)})</b>: EXIT_REVIEW · {escape(", ".join(x.exit_reasons or []))}</p>' for x in rows)
