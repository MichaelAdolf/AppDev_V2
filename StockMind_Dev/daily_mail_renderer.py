from html import escape

class DailyMailRenderer:
    LABELS={'conservative':'Conservative','balanced':'Balanced','aggressive':'Aggressive','individual':'Individual'}
    def render(self,result):
        exits=[x for x in result.portfolio_items if x.exit_status=='EXIT_REVIEW'];watches=[x for x in result.portfolio_items if x.exit_status=='WATCH'];holds=[x for x in result.portfolio_items if x.exit_status=='HOLD']
        return f"""<!doctype html><html><body style='font-family:Arial,sans-serif;color:#222;max-width:980px;margin:auto;background:#fff'><h1 style='color:#17365d'>StockMind Daily Action Briefing</h1><p><b>Datenstand:</b> {escape(result.trading_date or '-')} &nbsp; | &nbsp; <b>Vergleich:</b> {escape(result.previous_trading_date or '-')}</p>{self._action_summary(result,exits,watches)}<h2 style='color:#087f23'>🟢 Entry Opportunities</h2>{self._entries(result.buy_signal_stocks)}<h2 style='color:#b71c1c'>🔴 Exit Review</h2>{self._portfolio_actions(exits,'Keine Position benötigt aktuell eine Exit-Prüfung.')}<h2 style='color:#8a6d00'>🟡 Watch</h2>{self._portfolio_actions(watches,'Keine Position benötigt aktuell erhöhte Aufmerksamkeit.')}<h2 style='color:#2f75b5'>🔵 Portfolio Summary</h2>{self._portfolio_summary(result,holds)}<h2>📈 Daily Changes</h2>{self._changes(result.changes)}<h2>📋 Watchlist</h2>{self._watchlist(result.watchlist)}<p style='font-size:12px;color:#777;margin-top:24px'>BUY bedeutet Einstieg prüfen. EXIT REVIEW bedeutet Verkauf manuell prüfen. StockMind führt keine Transaktionen aus.</p></body></html>"""
    def _action_summary(self,r,exits,watches):
        return f"<div style='display:flex;gap:8px;flex-wrap:wrap;margin:16px 0'><span style='{self._pill('#e9f7ee','#087f23')}'>{len(r.buy_signal_stocks)} Entry</span><span style='{self._pill('#fdeeee','#b71c1c')}'>{len(exits)} Exit Review</span><span style='{self._pill('#fff9e6','#8a6d00')}'>{len(watches)} Watch</span></div>"
    def _entries(self,rows):
        if not rows:return '<p>Keine aktuellen BUY-Signale.</p>'
        blocks=[]
        for row in rows:
            buys=[x for x in row.profiles if x.signal=='BUY'];primary=next((x for x in buys if x.profile_name==row.primary_profile),buys[0])
            profiles=', '.join(self.LABELS.get(x.profile_name,x.profile_name) for x in buys)
            blocks.append(f"<div style='{self._card('#087f23')}'><b>{escape(row.company_name)} ({escape(row.symbol)})</b><br><b style='color:#087f23'>🟢 BUY · Einstieg prüfen</b><br><small>BUY-Profile: {escape(profiles)}</small><table style='margin-top:8px'><tr><td>Primärprofil</td><td><b>{escape(self.LABELS.get(primary.profile_name,primary.profile_name))}</b></td></tr><tr><td>Opportunity Score</td><td>{self._num(primary.opportunity_score,1)}</td></tr><tr><td>Confidence</td><td>{self._pct(primary.confidence)}</td></tr><tr><td>Historical Hit</td><td>{primary.target_hit_rate:.0%}</td></tr><tr><td>Sample</td><td>{primary.complete_period_count} Perioden · {escape(primary.sample_quality)}</td></tr><tr><td>Risk</td><td>{escape(primary.risk_level or '-')}</td></tr></table></div>")
        return ''.join(blocks)
    def _portfolio_actions(self,rows,empty):
        if not rows:return f'<p>{escape(empty)}</p>'
        color='#b71c1c' if rows[0].exit_status=='EXIT_REVIEW' else '#8a6d00';icon='🔴' if rows[0].exit_status=='EXIT_REVIEW' else '🟡';action='Verkauf prüfen' if rows[0].exit_status=='EXIT_REVIEW' else 'Position beobachten'
        return ''.join(f"<div style='{self._card(color)}'><b>{escape(x.company_name)} ({escape(x.symbol)})</b><br><b style='color:{color}'>{icon} {escape(x.exit_status.replace('_',' '))} · {action}</b><br>P/L: {self._pct(x.unrealized_return_pct)} ({self._money(x.unrealized_profit)}) · Tag {x.holding_days}/60 · Rest {x.remaining_strategy_days} Tage<br>Strategie: {escape(x.exit_strategy)} · Validation: {escape(x.exit_validation_status)}<br>Gründe: {escape(', '.join(x.exit_reasons or []) or 'keine')}</div>" for x in rows)
    def _portfolio_summary(self,r,holds):
        summary=f"<div style='background:#eef6ff;padding:12px;border-radius:8px'><b>Investiert:</b> {self._money(r.portfolio_invested)} &nbsp; <b>Marktwert:</b> {self._money(r.portfolio_market_value)} &nbsp; <b>Unrealisiert:</b> {self._money(r.portfolio_unrealized,True)} &nbsp; <b>Realisiert YTD:</b> {self._money(r.portfolio_realized_ytd,True)}</div>"
        return summary+(f"<p>🔵 HOLD: {len(holds)} Position(en) ohne aktuellen Handlungsbedarf.</p>" if holds else '<p>Keine HOLD-Positionen.</p>')
    def _changes(self,changes):
        if not changes:return '<p>Keine wesentlichen Veränderungen zum vorherigen Handelstag.</p>'
        return ''.join(f"<div style='padding:7px 0;border-bottom:1px solid #eee'><b>{escape(x['company_name'])} ({escape(x['symbol'])})</b>: {escape(x['type'])} · {escape(x['detail'])}</div>" for x in changes[:12])
    def _watchlist(self,rows):
        if not rows:return '<p>Keine Watchlist-Daten.</p>'
        body=[]
        for row in rows:
            decisions=' | '.join(f"{escape(self.LABELS.get(x.profile_name,x.profile_name))}: {escape(x.signal)}" for x in row.profiles)
            body.append(f"<tr><td><b>{escape(row.company_name)}</b><br>{escape(row.symbol)}</td><td>{decisions}</td></tr>")
        return f"<table style='border-collapse:collapse;width:100%;font-size:13px'><tr><th style='{self._th()}'>Aktie</th><th style='{self._th()}'>Profilentscheidungen</th></tr>{''.join(body)}</table>"
    def _card(self,color):return f'border-left:5px solid {color};padding:12px;margin:9px 0;background:#fafafa;border-radius:4px'
    def _pill(self,bg,color):return f'background:{bg};color:{color};padding:8px 12px;border-radius:18px;font-weight:bold'
    def _th(self):return 'text-align:left;padding:7px;border-bottom:2px solid #ddd'
    def _num(self,v,d=1):return '-' if v is None else f'{v:.{d}f}'
    def _pct(self,v):return '-' if v is None else f'{v:.1%}'
    def _money(self,v,signed=False):return '-' if v is None else (f'{v:+,.2f} €' if signed else f'{v:,.2f} €')
