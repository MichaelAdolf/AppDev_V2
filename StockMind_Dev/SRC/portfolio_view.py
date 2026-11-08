from datetime import date

import pandas as pd
import streamlit as st

from components.portfolio_exit_view import render as render_portfolio_exit
from stockmind.application.portfolio.add_position_use_case import AddPositionUseCase
from stockmind.application.portfolio.delete_portfolio_use_cases import (
    DeletePositionUseCase,
    DeletePurchaseLotUseCase,
    DeleteTradeUseCase,
)
from stockmind.application.portfolio.portfolio_dashboard_use_case import (
    PortfolioDashboardUseCase,
)
from stockmind.application.portfolio.portfolio_intelligence_use_case import (
    PortfolioIntelligenceUseCase,
)
from stockmind.application.portfolio.portfolio_performance_use_case import (
    PortfolioPerformanceUseCase,
)
from stockmind.application.portfolio.sell_position_use_case import SellPositionUseCase
from stockmind.application.portfolio.update_purchase_lot_use_case import (
    UpdatePurchaseLotUseCase,
)
from stockmind.infrastructure.watchlists.watchlist_repository import WatchlistRepository


def _money(value):
    return "–" if value is None else f"{value:,.2f} €"


def _pct(value):
    return "–" if value is None else f"{value:.1%}"


def render():
    result = PortfolioDashboardUseCase().load()
    intelligence = PortfolioIntelligenceUseCase().load()

    st.header("Portfolio")
    st.caption(
        "Offene Positionen, Käufe, Verkäufe, Performance und produktive "
        "Exit Intelligence. Strategie-Research befindet sich im Tab Strategien."
    )

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Investiert", _money(result.invested_amount))
    c2.metric("Marktwert", _money(result.market_value))
    c3.metric("Unrealisiert", _money(result.unrealized_profit))
    c4.metric("Realisiert netto", _money(result.realized_net_profit))

    tabs = st.tabs([
        "Position Intelligence",
        "Exit Intelligence",
        "Offene Positionen",
        "Kauf hinzufügen",
        "Kauftranchen verwalten",
        "Position verkaufen",
        "Trade History",
        "Performance",
    ])

    with tabs[0]:
        if not intelligence:
            st.info("Noch keine offenen Positionen vorhanden.")
        for item in intelligence:
            icon = "🔴" if item.attention_level == "CRITICAL" else "🟡" if item.attention_level == "ATTENTION" else "🔵"
            with st.expander(
                f"{icon} {item.company_name} ({item.symbol}) · "
                f"{_pct(item.unrealized_return_pct)} · Tag {item.holding_days}/60",
                expanded=item.attention_level != "NORMAL",
            ):
                a, b, c, d = st.columns(4)
                a.metric("P/L", _money(item.unrealized_profit), _pct(item.unrealized_return_pct))
                b.metric("+8-%-Ziel", _money(item.target_price))
                c.metric("Restlaufzeit", f"{item.remaining_strategy_days} Tage")
                d.metric("Status", item.attention_level)
                st.dataframe(pd.DataFrame([
                    {"Kennzahl": "Opportunity Score", "Entry": item.entry_score, "Heute": item.current_score, "Δ": item.score_change},
                    {"Kennzahl": "Confidence", "Entry": item.entry_confidence, "Heute": item.current_confidence, "Δ": item.confidence_change},
                    {"Kennzahl": "Risk", "Entry": item.entry_risk, "Heute": item.current_risk, "Δ": ""},
                    {"Kennzahl": "Signal", "Entry": item.entry_signal, "Heute": item.current_signal, "Δ": ""},
                ]), width="stretch", hide_index=True)
                if item.attention_reasons:
                    st.warning("Prüfhintergrund: " + ", ".join(item.attention_reasons))

    with tabs[1]:
        render_portfolio_exit()

    with tabs[2]:
        if not result.positions:
            st.info("Noch keine offenen Positionen vorhanden.")
        else:
            st.dataframe(pd.DataFrame([{
                "Aktie": f"{item.position.company_name} ({item.position.symbol})",
                "Tranchen": len(item.lots),
                "Stück": item.position.quantity,
                "Ø Kaufkurs": round(item.position.purchase_price, 2),
                "Aktuell": item.current_price,
                "P/L €": None if item.unrealized_profit is None else round(item.unrealized_profit, 2),
                "P/L %": None if item.unrealized_return_pct is None else round(item.unrealized_return_pct * 100, 2),
                "Signal": item.current_signal,
                "Score": item.current_score,
            } for item in result.positions]), width="stretch", hide_index=True)

    with tabs[3]:
        watchlist = [item for item in WatchlistRepository().load_all() if item.active]
        labels = {f"{item.company_name} ({item.symbol})": item.symbol for item in watchlist}
        if not labels:
            st.warning("Keine aktiven Watchlist-Aktien.")
        else:
            with st.form("add_portfolio_lot"):
                label = st.selectbox("Aktie", list(labels))
                purchase_date = st.date_input("Kaufdatum", date.today())
                a, b, c = st.columns(3)
                price = a.number_input("Kaufpreis", min_value=0.01)
                quantity = b.number_input("Stückzahl", min_value=0.0001, format="%.4f")
                fees = c.number_input("Kaufgebühren", min_value=0.0)
                profile = st.selectbox("Entry-Profil", ["conservative", "balanced", "aggressive"], index=1)
                note = st.text_area("Notiz")
                submitted = st.form_submit_button("Kauf hinzufügen", type="primary")
            if submitted:
                AddPositionUseCase().execute(labels[label], purchase_date, price, quantity, fees, profile, note)
                st.success("Kauf hinzugefügt.")
                st.rerun()

    with tabs[4]:
        lots = [(view, lot) for view in result.positions for lot in view.lots]
        if not lots:
            st.info("Keine Kauftranchen vorhanden.")
        else:
            choices = {
                f"{view.position.symbol} · {lot.purchase_date} · {lot.quantity:g} Stück zu {lot.purchase_price:.2f} €": lot.id
                for view, lot in lots
            }
            selected = st.selectbox("Kauftranche", list(choices))
            lot = next(item for _, item in lots if item.id == choices[selected])
            with st.form("edit_portfolio_lot"):
                purchase_date = st.date_input("Kaufdatum", date.fromisoformat(lot.purchase_date))
                a, b, c = st.columns(3)
                price = a.number_input("Kaufpreis", min_value=0.01, value=float(lot.purchase_price))
                quantity = b.number_input("Stückzahl", min_value=0.0001, value=float(lot.quantity), format="%.4f")
                fees = c.number_input("Gebühren", min_value=0.0, value=float(lot.purchase_fees))
                profiles = ["conservative", "balanced", "aggressive"]
                profile = st.selectbox("Profil", profiles, index=profiles.index(lot.entry_profile))
                note = st.text_area("Notiz", lot.note)
                save = st.form_submit_button("Änderungen speichern")
            if save:
                UpdatePurchaseLotUseCase().execute(lot.id, purchase_date, price, quantity, fees, profile, note)
                st.success("Kauftranche aktualisiert.")
                st.rerun()
            confirm = st.checkbox("Kauftranche dauerhaft löschen.")
            if st.button("Kauftranche löschen", disabled=not confirm):
                DeletePurchaseLotUseCase().execute(lot.id)
                st.rerun()

    with tabs[5]:
        if not result.positions:
            st.info("Keine offene Position vorhanden.")
        else:
            choices = {
                f"{item.position.company_name} ({item.position.symbol}) · {item.position.quantity:g} Stück": item.position.id
                for item in result.positions
            }
            with st.form("sell_portfolio_position"):
                label = st.selectbox("Position", list(choices))
                sale_date = st.date_input("Verkaufsdatum", date.today())
                a, b, c = st.columns(3)
                price = a.number_input("Verkaufspreis", min_value=0.01)
                fees = b.number_input("Verkaufsgebühren", min_value=0.0)
                tax = c.number_input("Steuer", min_value=0.0)
                reason = st.selectbox("Exit-Grund", ["MANUAL", "TARGET_REACHED", "TIME_LIMIT", "STOP_LOSS", "SIGNAL_DETERIORATION"])
                note = st.text_area("Verkaufsnotiz")
                submitted = st.form_submit_button("Position vollständig verkaufen", type="primary")
            if submitted:
                trade = SellPositionUseCase().execute(choices[label], sale_date, price, fees, tax, reason, note)
                st.success(f"Trade abgeschlossen: {_money(trade.net_profit)}")
                st.rerun()

    with tabs[6]:
        if not result.trades:
            st.info("Noch keine abgeschlossenen Trades.")
        else:
            st.dataframe(pd.DataFrame([{
                "Aktie": f"{trade.company_name} ({trade.symbol})",
                "Kauf": trade.purchase_date,
                "Verkauf": trade.sale_date,
                "Netto €": round(trade.net_profit, 2),
                "Netto %": round(trade.net_return_pct * 100, 2),
                "Profil": trade.entry_profile,
                "Exit": trade.exit_reason,
            } for trade in result.trades]), width="stretch", hide_index=True)
            choices = {f"{trade.symbol} · {trade.sale_date} · {trade.net_profit:.2f} €": trade.id for trade in result.trades}
            selected = st.selectbox("Fehlerhaften Trade löschen", list(choices))
            confirm = st.checkbox("Trade dauerhaft löschen.")
            if st.button("Trade löschen", disabled=not confirm):
                DeleteTradeUseCase().execute(choices[selected])
                st.rerun()

    with tabs[7]:
        performance = PortfolioPerformanceUseCase().load()
        periods = {
            "month": "Dieser Monat",
            "six_months": "Letzte 6 Monate",
            "ytd": "Seit 01.01.",
            "twelve_months": "Letzte 12 Monate",
            "all": "Gesamt",
        }
        st.dataframe(pd.DataFrame([{
            "Zeitraum": label,
            "Trades": performance[key]["trade_count"],
            "Win Rate %": round(performance[key]["win_rate"] * 100, 1),
            "Netto €": round(performance[key]["net_profit"], 2),
            "Ø Gewinner €": round(performance[key]["average_winner"], 2),
            "Ø Verlierer €": round(performance[key]["average_loser"], 2),
            "Ø Tage": round(performance[key]["average_holding_days"], 1),
        } for key, label in periods.items()]), width="stretch", hide_index=True)
        st.subheader("Performance nach Entry-Profil")
        st.dataframe(pd.DataFrame([{
            "Profil": profile,
            "Trades": values["trade_count"],
            "Win Rate %": round(values["win_rate"] * 100, 1),
            "Netto €": round(values["net_profit"], 2),
            "Ø Tage": round(values["average_holding_days"], 1),
        } for profile, values in performance["by_profile"].items()]), width="stretch", hide_index=True)
