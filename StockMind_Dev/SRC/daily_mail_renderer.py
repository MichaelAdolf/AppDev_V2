from html import escape


class DailyMailRenderer:
    PROFILE_LABELS={"conservative":"Conservative","balanced":"Balanced","aggressive":"Aggressive"}

    def render(self,result):
        return f"""<!doctype html><html><body style='font-family:Arial,sans-serif;color:#222;max-width:1000px;margin:auto'>
        <h1 style='color:#17365d'>StockMind Daily Trading Briefing</h1>
        <p><b>Datenstand:</b> {escape(result.trading_date or '-')} &nbsp; | &nbsp; <b>Vergleich:</b> {escape(result.previous_trading_date or '-')}</p>
        {self._summary(result)}
        <h2>Aktuelle Kaufsignale</h2>
        {self._stock_table(result.buy_signal_stocks,empty='Aktuell meldet kein Profil ein BUY-Signal.')}
        <h2>Änderungen zum vorherigen Handelstag</h2>
        {self._changes(result.changes)}
        <h2>Gesamte Watchlist</h2>
        {self._stock_table(result.watchlist,empty='Keine Watchlist-Daten verfügbar.')}
        <p style='font-size:12px;color:#777;margin-top:24px'>BUY-Trefferquoten beziehen sich auf vollständige historische BUY-Perioden mit dem StockMind-Ziel von +8 % innerhalb von 60 Kalendertagen.</p>
        </body></html>"""

    def _summary(self,r):
        return f"<div style='background:#f4f7fb;padding:12px;border-radius:8px'><b>{len(r.watchlist)}</b> Watchlist-Aktien &nbsp; | &nbsp; <b>{len(r.buy_signal_stocks)}</b> Aktien mit mindestens einem BUY &nbsp; | &nbsp; <b>{len(r.changes)}</b> relevante Änderungen</div>"

    def _stock_table(self,rows,empty):
        if not rows:return f"<p>{escape(empty)}</p>"
        head="".join(f"<th style='{self._th()}'>{self.PROFILE_LABELS[p]}</th>" for p in ("conservative","balanced","aggressive"))
        body=[]
        for row in rows:
            by={p.profile_name:p for p in row.profiles}
            cells="".join(self._signal_cell(by.get(p)) for p in ("conservative","balanced","aggressive"))
            body.append(f"<tr><td style='{self._td()}'><b>{escape(row.company_name)}</b><br><span style='color:#666'>{escape(row.symbol)}</span></td>{cells}</tr>")
        return f"<table style='border-collapse:collapse;width:100%;font-size:14px'><thead><tr><th style='{self._th()}'>Aktie</th>{head}</tr></thead><tbody>{''.join(body)}</tbody></table>"

    def _signal_cell(self,p):
        if p is None:return f"<td style='{self._td()}'>–</td>"
        if p.signal=="BUY":
            text=f"<b style='color:#087f23'>● BUY</b><br><b>{p.target_hit_rate:.0%}</b><br><span style='font-size:12px'>{p.complete_period_count} Perioden · {escape(p.sample_quality)}</span>"
            bg="#e9f7ee"
        elif p.signal=="SELL":text="<span style='color:#b71c1c'>● SELL</span>";bg="#fdeeee"
        else:text="<span style='color:#8a6d00'>● HOLD</span>";bg="#fff9e6"
        return f"<td style='{self._td()}background:{bg};text-align:center'>{text}</td>"

    def _changes(self, changes):

        if not changes:
            return (
                "<p>"
                "Keine wesentlichen Veränderungen "
                "zum vorherigen Handelstag."
                "</p>"
            )

        rows = "".join(
            (
                f"<tr>"
                f"<td style='{self._td()}'>"
                f"<b>{escape(item['company_name'])}</b> "
                f"({escape(item['symbol'])})"
                f"</td>"
                f"<td style='{self._td()}'>"
                f"{escape(item['type'])}"
                f"</td>"
                f"<td style='{self._td()}'>"
                f"{escape(item['detail'])}"
                f"</td>"
                f"</tr>"
            )
            for item in changes
        )

        return (
            "<table "
            "style='border-collapse:collapse;"
            "width:100%;"
            "font-size:14px'>"

            "<thead>"
            "<tr>"

            f"<th style='{self._th()}'>"
            "Aktie"
            "</th>"

            f"<th style='{self._th()}'>"
            "Änderung"
            "</th>"

            f"<th style='{self._th()}'>"
            "Details"
            "</th>"

            "</tr>"
            "</thead>"

            f"<tbody>{rows}</tbody>"

            "</table>"
        )
    def _th(self):return "padding:8px;border:1px solid #ddd;background:#eef2f6;text-align:left"
    def _td(self):return "padding:8px;border:1px solid #ddd;"
