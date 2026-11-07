from html import escape
class DailyMailRenderer:
 PROFILE_LABELS={'conservative':'Conservative','balanced':'Balanced','aggressive':'Aggressive'}
 def render(self,r):return f"""<!doctype html><html><body style='font-family:Arial,sans-serif;color:#222;max-width:1000px;margin:auto'><h1 style='color:#17365d'>StockMind Daily Trading Briefing</h1><p><b>Datenstand:</b> {escape(r.trading_date or '-')} | <b>Vergleich:</b> {escape(r.previous_trading_date or '-')}</p>{self._summary(r)}<h2>Aktuelle Kaufsignale</h2>{self._stocks(r.buy_signal_stocks,'Aktuell meldet kein Profil ein BUY-Signal.')}<h2>Portfolio: Positionen mit Aufmerksamkeit</h2>{self._portfolio_alerts(r.portfolio_items)}<h2>Portfolioübersicht</h2>{self._portfolio_summary(r)}<h2>Änderungen zum vorherigen Handelstag</h2>{self._changes(r.changes)}<h2>Gesamte Watchlist</h2>{self._stocks(r.watchlist,'Keine Watchlist-Daten verfügbar.')}<p style='font-size:12px;color:#777'>Portfolio-Hinweise markieren Prüfbedarf und sind noch keine automatische Verkaufsentscheidung.</p></body></html>"""
 def _summary(self,r):return f"<div style='background:#f4f7fb;padding:12px;border-radius:8px'><b>{len(r.watchlist)}</b> Watchlist-Aktien | <b>{len(r.buy_signal_stocks)}</b> Aktien mit BUY | <b>{sum(x.attention_level!='NORMAL' for x in r.portfolio_items)}</b> Portfolio-Hinweise</div>"
 def _portfolio_summary(self,r):return f"<div style='background:#eef6ff;padding:12px;border-radius:8px'><b>Investiert:</b> {r.portfolio_invested:,.2f} € | <b>Marktwert:</b> {r.portfolio_market_value:,.2f} € | <b>Unrealisiert:</b> {r.portfolio_unrealized:+,.2f} € | <b>Realisiert YTD:</b> {r.portfolio_realized_ytd:+,.2f} €</div>"
 def _portfolio_alerts(self,items):
  attention=[x for x in items if x.attention_level!='NORMAL']
  if not attention:return '<p>Keine offenen Positionen mit besonderem Prüfbedarf.</p>'
  return "".join(f"<div style='border-left:5px solid {'#b71c1c' if x.attention_level=='CRITICAL' else '#d9a300'};padding:8px 12px;margin:8px 0;background:#fafafa'><b>{escape(x.company_name)} ({escape(x.symbol)})</b><br>P/L: {x.unrealized_return_pct:.1%} ({x.unrealized_profit:+.2f} €) · Tag {x.holding_days}/60 · Rest {x.remaining_strategy_days} Tage<br>Signal: {escape(x.current_signal or '-')} · Score: {x.current_score if x.current_score is not None else '-'}<br><b>Prüfhintergrund:</b> {escape(', '.join(x.attention_reasons))}</div>" for x in attention)
 def _stocks(self,rows,empty):
  if not rows:return f'<p>{escape(empty)}</p>'
  head=''.join(f"<th style='{self._th()}'>{self.PROFILE_LABELS[p]}</th>" for p in ('conservative','balanced','aggressive'));body=[]
  for row in rows:
   by={p.profile_name:p for p in row.profiles};cells=''.join(self._signal(by.get(p)) for p in ('conservative','balanced','aggressive'));body.append(f"<tr><td style='{self._td()}'><b>{escape(row.company_name)}</b><br>{escape(row.symbol)}</td>{cells}</tr>")
  return f"<table style='border-collapse:collapse;width:100%;font-size:14px'><thead><tr><th style='{self._th()}'>Aktie</th>{head}</tr></thead><tbody>{''.join(body)}</tbody></table>"
 def _signal(self,p):
  if p is None:return f"<td style='{self._td()}'>–</td>"
  if p.signal=='BUY':
   hist='noch keine vollständige historische Periode' if p.complete_period_count==0 else f'{p.target_hit_rate:.0%}<br><span style="font-size:12px">{p.complete_period_count} Perioden · {escape(p.sample_quality)}</span>';return f"<td style='{self._td()}background:#e9f7ee;text-align:center'><b style='color:#087f23'>● BUY</b><br>{hist}</td>"
  color='#b71c1c' if p.signal=='SELL' else '#8a6d00';bg='#fdeeee' if p.signal=='SELL' else '#fff9e6';return f"<td style='{self._td()}background:{bg};text-align:center'><span style='color:{color}'>● {escape(p.signal)}</span></td>"
 def _changes(self,changes):
  if not changes:return '<p>Keine wesentlichen Veränderungen zum vorherigen Handelstag.</p>'
  rows=''.join(f"<tr><td style='{self._td()}'><b>{escape(x['company_name'])}</b> ({escape(x['symbol'])})</td><td style='{self._td()}'>{escape(x['type'])}</td><td style='{self._td()}'>{escape(x['detail'])}</td></tr>" for x in changes);return f"<table style='border-collapse:collapse;width:100%;font-size:14px'><tbody>{rows}</tbody></table>"
 def _th(self):return 'padding:8px;border:1px solid #ddd;background:#eef2f6;text-align:left'
 def _td(self):return 'padding:8px;border:1px solid #ddd;'
