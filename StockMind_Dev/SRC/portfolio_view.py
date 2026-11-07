from datetime import date

import pandas as pd
import streamlit as st

from components.exit_strategy_research_view import render as render_exit_research
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
from components.portfolio_exit_view import render as render_portfolio_exit



def _money(value):
    return "–" if value is None else f"{value:,.2f} €"


def _pct(value):
    return "–" if value is None else f"{value:.1%}"


def render():
    result = PortfolioDashboardUseCase().load()
    intelligence = PortfolioIntelligenceUseCase().load()

    st.subheader("Portfolio")
    st.caption(
        "Positionsüberwachung für das +8-%-Ziel innerhalb von 60 Kalendertagen. "
        "Hinweise markieren Prüfbedarf, noch keine automatische Verkaufsentscheidung."
    )

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Investiert", _money(result.invested_amount))
    col2.metric("Marktwert", _money(result.market_value))
    col3.metric("Unrealisiert", _money(result.unrealized_profit))
    col4.metric("Realisiert netto", _money(result.realized_net_profit))

    tabs = st.tabs([
        "Position Intelligence",
        "Exit Intelligence",
        "Offene Positionen",
        "Kauf hinzufügen",
        "Kauftranchen verwalten",
        "Position verkaufen",
        "Trade History",
        "Performance",
        "Exit Strategy Research",
    ])

    # ------------------------------------------------------------
    # 1. Position Intelligence
    # ------------------------------------------------------------
    with tabs[0]:
        if not intelligence:
            st.info("Noch keine offenen Positionen vorhanden.")
        else:
            for item in intelligence:
                if item.attention_level == "CRITICAL":
                    icon = "🔴"
                elif item.attention_level == "ATTENTION":
                    icon = "🟡"
                else:
                    icon = "🔵"

                title = (
                    f"{icon} {item.company_name} ({item.symbol}) · "
                    f"{_pct(item.unrealized_return_pct)} · "
                    f"Tag {item.holding_days}/60"
                )

                with st.expander(
                    title,
                    expanded=item.attention_level != "NORMAL",
                ):
                    c1, c2, c3, c4 = st.columns(4)
                    c1.metric(
                        "P/L",
                        _money(item.unrealized_profit),
                        _pct(item.unrealized_return_pct),
                    )
                    c2.metric("+8-%-Ziel", _money(item.target_price))
                    c3.metric(
                        "Restlaufzeit",
                        f"{item.remaining_strategy_days} Tage",
                    )
                    c4.metric("Status", item.attention_level)

                    st.write("**Entry → Heute**")
                    st.dataframe(
                        pd.DataFrame([
                            {
                                "Kennzahl": "Opportunity Score",
                                "Entry": item.entry_score,
                                "Heute": item.current_score,
                                "Δ": item.score_change,
                            },
                            {
                                "Kennzahl": "Confidence",
                                "Entry": item.entry_confidence,
                                "Heute": item.current_confidence,
                                "Δ": item.confidence_change,
                            },
                            {
                                "Kennzahl": "Risk",
                                "Entry": item.entry_risk,
                                "Heute": item.current_risk,
                                "Δ": "",
                            },
                            {
                                "Kennzahl": "Signal",
                                "Entry": item.entry_signal,
                                "Heute": item.current_signal,
                                "Δ": "",
                            },
                        ]),
                        hide_index=True,
                        width="stretch",
                    )

                    if item.attention_reasons:
                        st.warning(
                            "Prüfhintergrund: "
                            + ", ".join(item.attention_reasons)
                        )

                    st.caption(
                        f"{len(item.lots)} Kauftranchen · "
                        f"{item.quantity:g} Stück · "
                        f"gewichteter Kaufkurs "
                        f"{item.weighted_purchase_price:.2f} €"
                    )
    # ------------------------------------------------------------
    # 2. Exit Intelligence
    # ------------------------------------------------------------
    with tabs[1]:
        render_portfolio_exit()
    # ------------------------------------------------------------
    # 3. Offene Positionen
    # ------------------------------------------------------------
    with tabs[2]:
        if not result.positions:
            st.info("Noch keine offenen Positionen vorhanden.")
        else:
            rows = []
            for item in result.positions:
                position = item.position
                rows.append({
                    "Aktie": (
                        f"{position.company_name} "
                        f"({position.symbol})"
                    ),
                    "Tranchen": len(item.lots),
                    "Stück": position.quantity,
                    "Ø Kaufkurs": round(position.purchase_price, 2),
                    "Aktuell": item.current_price,
                    "P/L €": (
                        round(item.unrealized_profit, 2)
                        if item.unrealized_profit is not None
                        else None
                    ),
                    "P/L %": (
                        round(item.unrealized_return_pct * 100, 2)
                        if item.unrealized_return_pct is not None
                        else None
                    ),
                    "Signal": item.current_signal,
                    "Score": item.current_score,
                })

            st.dataframe(
                pd.DataFrame(rows),
                width="stretch",
                hide_index=True,
            )

    # ------------------------------------------------------------
    # 4. Kauf hinzufügen
    # ------------------------------------------------------------
    with tabs[3]:
        watchlist = [
            entry
            for entry in WatchlistRepository().load_all()
            if entry.active
        ]
        labels = {
            f"{entry.company_name} ({entry.symbol})": entry.symbol
            for entry in watchlist
        }

        if not labels:
            st.warning("Keine aktiven Watchlist-Aktien.")
        else:
            with st.form("add_lot"):
                label = st.selectbox("Aktie", list(labels))
                purchase_date = st.date_input(
                    "Kaufdatum",
                    date.today(),
                )

                c1, c2, c3 = st.columns(3)
                purchase_price = c1.number_input(
                    "Kaufpreis",
                    min_value=0.01,
                )
                quantity = c2.number_input(
                    "Stückzahl",
                    min_value=0.0001,
                    format="%.4f",
                )
                purchase_fees = c3.number_input(
                    "Kaufgebühren",
                    min_value=0.0,
                )

                entry_profile = st.selectbox(
                    "Entry-Profil",
                    ["conservative", "balanced", "aggressive"],
                    index=1,
                )
                note = st.text_area("Notiz")

                submitted = st.form_submit_button(
                    "Kauf hinzufügen",
                    type="primary",
                )

            if submitted:
                AddPositionUseCase().execute(
                    labels[label],
                    purchase_date,
                    purchase_price,
                    quantity,
                    purchase_fees,
                    entry_profile,
                    note,
                )
                st.success("Kauf hinzugefügt.")
                st.rerun()

    # ------------------------------------------------------------
    # 5. Kauftranchen verwalten
    # ------------------------------------------------------------
    with tabs[4]:
        lots = [
            (position_view, lot)
            for position_view in result.positions
            for lot in position_view.lots
        ]

        if not lots:
            st.info("Keine Kauftranchen vorhanden.")
        else:
            names = {
                (
                    f"{position_view.position.symbol} · "
                    f"{lot.purchase_date} · "
                    f"{lot.quantity:g} Stück zu "
                    f"{lot.purchase_price:.2f} €"
                ): lot.id
                for position_view, lot in lots
            }

            selected_label = st.selectbox(
                "Kauftranche",
                list(names),
            )
            selected_lot = next(
                lot
                for _, lot in lots
                if lot.id == names[selected_label]
            )

            with st.form("edit_lot"):
                purchase_date = st.date_input(
                    "Kaufdatum",
                    date.fromisoformat(selected_lot.purchase_date),
                )

                c1, c2, c3 = st.columns(3)
                purchase_price = c1.number_input(
                    "Kaufpreis",
                    min_value=0.01,
                    value=float(selected_lot.purchase_price),
                )
                quantity = c2.number_input(
                    "Stückzahl",
                    min_value=0.0001,
                    value=float(selected_lot.quantity),
                    format="%.4f",
                )
                purchase_fees = c3.number_input(
                    "Gebühren",
                    min_value=0.0,
                    value=float(selected_lot.purchase_fees),
                )

                profiles = [
                    "conservative",
                    "balanced",
                    "aggressive",
                ]
                entry_profile = st.selectbox(
                    "Profil",
                    profiles,
                    index=profiles.index(selected_lot.entry_profile),
                )
                note = st.text_area(
                    "Notiz",
                    selected_lot.note,
                )

                save = st.form_submit_button(
                    "Änderungen speichern"
                )

            if save:
                UpdatePurchaseLotUseCase().execute(
                    selected_lot.id,
                    purchase_date,
                    purchase_price,
                    quantity,
                    purchase_fees,
                    entry_profile,
                    note,
                )
                st.success("Kauftranche aktualisiert.")
                st.rerun()

            confirm_delete = st.checkbox(
                "Kauftranche dauerhaft löschen."
            )
            if st.button(
                "Kauftranche löschen",
                disabled=not confirm_delete,
            ):
                DeletePurchaseLotUseCase().execute(
                    selected_lot.id
                )
                st.success("Kauftranche gelöscht.")
                st.rerun()

    # ------------------------------------------------------------
    # 6. Position verkaufen
    # ------------------------------------------------------------
    with tabs[5]:
        if not result.positions:
            st.info("Keine offene Position vorhanden.")
        else:
            choices = {
                (
                    f"{item.position.company_name} "
                    f"({item.position.symbol}) · "
                    f"{item.position.quantity:g} Stück"
                ): item.position.id
                for item in result.positions
            }

            with st.form("sell_position"):
                label = st.selectbox(
                    "Position",
                    list(choices),
                )
                sale_date = st.date_input(
                    "Verkaufsdatum",
                    date.today(),
                )

                c1, c2, c3 = st.columns(3)
                sale_price = c1.number_input(
                    "Verkaufspreis",
                    min_value=0.01,
                )
                sale_fees = c2.number_input(
                    "Verkaufsgebühren",
                    min_value=0.0,
                )
                tax_paid = c3.number_input(
                    "Steuer",
                    min_value=0.0,
                )

                exit_reason = st.selectbox(
                    "Exit-Grund",
                    [
                        "MANUAL",
                        "TARGET_REACHED",
                        "TIME_LIMIT",
                        "STOP_LOSS",
                        "SIGNAL_DETERIORATION",
                    ],
                )
                note = st.text_area("Verkaufsnotiz")

                submitted = st.form_submit_button(
                    "Position vollständig verkaufen",
                    type="primary",
                )

            if submitted:
                trade = SellPositionUseCase().execute(
                    choices[label],
                    sale_date,
                    sale_price,
                    sale_fees,
                    tax_paid,
                    exit_reason,
                    note,
                )
                st.success(
                    "Trade abgeschlossen: "
                    + _money(trade.net_profit)
                )
                st.rerun()

    # ------------------------------------------------------------
    # 7. Trade History
    # ------------------------------------------------------------
    with tabs[6]:
        if not result.trades:
            st.info("Noch keine abgeschlossenen Trades.")
        else:
            st.dataframe(
                pd.DataFrame([
                    {
                        "Aktie": f"{trade.company_name} ({trade.symbol})",
                        "Kauf": trade.purchase_date,
                        "Verkauf": trade.sale_date,
                        "Netto €": round(trade.net_profit, 2),
                        "Netto %": round(
                            trade.net_return_pct * 100,
                            2,
                        ),
                        "Profil": trade.entry_profile,
                        "Exit": trade.exit_reason,
                    }
                    for trade in result.trades
                ]),
                width="stretch",
                hide_index=True,
            )

            trade_choices = {
                (
                    f"{trade.symbol} · {trade.sale_date} · "
                    f"{trade.net_profit:.2f} €"
                ): trade.id
                for trade in result.trades
            }
            chosen_trade = st.selectbox(
                "Fehlerhaften Trade löschen",
                list(trade_choices),
            )
            confirm_trade_delete = st.checkbox(
                "Trade dauerhaft löschen."
            )

            if st.button(
                "Trade löschen",
                disabled=not confirm_trade_delete,
            ):
                DeleteTradeUseCase().execute(
                    trade_choices[chosen_trade]
                )
                st.success("Trade gelöscht.")
                st.rerun()

    # ------------------------------------------------------------
    # 8. Performance
    # ------------------------------------------------------------
    with tabs[7]:
        performance = PortfolioPerformanceUseCase().load()

        periods = {
            "month": "Dieser Monat",
            "six_months": "Letzte 6 Monate",
            "ytd": "Seit 01.01.",
            "twelve_months": "Letzte 12 Monate",
            "all": "Gesamt",
        }

        st.dataframe(
            pd.DataFrame([
                {
                    "Zeitraum": label,
                    "Trades": performance[key]["trade_count"],
                    "Win Rate %": round(
                        performance[key]["win_rate"] * 100,
                        1,
                    ),
                    "Netto €": round(
                        performance[key]["net_profit"],
                        2,
                    ),
                    "Ø Gewinner €": round(
                        performance[key]["average_winner"],
                        2,
                    ),
                    "Ø Verlierer €": round(
                        performance[key]["average_loser"],
                        2,
                    ),
                    "Ø Tage": round(
                        performance[key]["average_holding_days"],
                        1,
                    ),
                }
                for key, label in periods.items()
            ]),
            width="stretch",
            hide_index=True,
        )

        st.subheader("Performance nach Entry-Profil")
        st.dataframe(
            pd.DataFrame([
                {
                    "Profil": profile,
                    "Trades": values["trade_count"],
                    "Win Rate %": round(
                        values["win_rate"] * 100,
                        1,
                    ),
                    "Netto €": round(
                        values["net_profit"],
                        2,
                    ),
                    "Ø Tage": round(
                        values["average_holding_days"],
                        1,
                    ),
                }
                for profile, values
                in performance["by_profile"].items()
            ]),
            width="stretch",
            hide_index=True,
        )

    # ------------------------------------------------------------
    # 9. Exit Strategy Research
    # ------------------------------------------------------------
    with tabs[8]:
        render_exit_research()
