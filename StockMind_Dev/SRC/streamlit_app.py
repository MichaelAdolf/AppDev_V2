import streamlit as st

from components.portfolio_view import render as render_portfolio
from components.stock_decision_summary import render as render_stock_decision_summary
from components.stock_detail_view import render as render_stock_detail
from components.strategy_center_view import render as render_strategy_center
from components.top_movers_view import render as render_top_movers
from components.watchlist_view import render as render_watchlist
from stockmind.application.strategy.fitted_profile_signal_use_case import FittedProfileSignalUseCase
from stockmind.application.watchlists.add_stock_use_case import AddStockUseCase
from stockmind.application.watchlists.remove_stock_use_case import RemoveStockUseCase
from stockmind.infrastructure.strategy.fitted_profile_repository import FittedProfileRepository
from stockmind.infrastructure.watchlists.watchlist_repository import WatchlistRepository

st.set_page_config(page_title="StockMind", layout="wide")
st.title("📈 StockMind")

# Sidebar: daily operating context
st.sidebar.header("StockMind")
entries = [item for item in WatchlistRepository().load_all() if item.active]
labels = {f"{item.company_name} ({item.symbol})": item.symbol for item in entries}

if labels:
    selected_label = st.sidebar.selectbox(
        "Aktie auswählen",
        list(labels),
        key="sidebar_stock_selection",
    )
    selected_symbol = labels[selected_label]
else:
    selected_symbol = None
    st.sidebar.info("Noch keine aktive Watchlist-Aktie vorhanden.")

profile_options = ["conservative", "balanced", "aggressive"]
if selected_symbol and FittedProfileRepository().load_active(selected_symbol):
    profile_options.append("individual")

profile = st.sidebar.selectbox(
    "Profil",
    profile_options,
    index=min(1, len(profile_options) - 1),
    key="sidebar_profile_selection",
)

if profile == "individual" and selected_symbol:
    fitted = FittedProfileSignalUseCase().evaluate(selected_symbol)
    st.sidebar.caption(
        f"{fitted.strategy_name} · Signal {fitted.signal} · "
        f"{fitted.matched_conditions}/{fitted.required_conditions} Bedingungen"
    )

st.sidebar.divider()
st.sidebar.subheader("📋 Watchlist verwalten")
new_symbol = st.sidebar.text_input("Aktie hinzufügen", value="")
if st.sidebar.button("➕ Hinzufügen"):
    if new_symbol.strip():
        added = AddStockUseCase().execute(new_symbol)
        if added:
            st.sidebar.success(f"{new_symbol.upper()} hinzugefügt.")
        else:
            st.sidebar.warning("Aktie bereits vorhanden.")
        st.rerun()

all_entries = WatchlistRepository().load_all()
if all_entries:
    selected_remove = st.sidebar.selectbox(
        "Aktie entfernen",
        [item.symbol for item in all_entries],
    )
    if st.sidebar.button("➖ Entfernen"):
        RemoveStockUseCase().execute(selected_remove)
        st.sidebar.success(f"{selected_remove} entfernt.")
        st.rerun()

# Main navigation
watchlist_tab, movers_tab, portfolio_tab, stock_tab, strategies_tab = st.tabs([
    "🏆 Watchlist",
    "📈 Top Movers",
    "💼 Portfolio",
    "🔎 Aktienanalyse",
    "🧪 Strategien",
])

# Existing dashboards still require one of the three standard profiles.
standard_profile = profile
if profile == "individual":
    active = FittedProfileRepository().load_active(selected_symbol)
    standard_profile = active.base_profile if active else "balanced"

with watchlist_tab:
    render_watchlist(standard_profile)

with movers_tab:
    render_top_movers(standard_profile)

with portfolio_tab:
    render_portfolio()

with stock_tab:
    if not selected_symbol:
        st.info("Bitte zuerst eine Aktie in die Watchlist aufnehmen.")
    else:
        render_stock_decision_summary(selected_symbol)
        st.divider()
        render_stock_detail(
            profile_name=standard_profile,
            symbol=selected_symbol,
        )

with strategies_tab:
    render_strategy_center()
