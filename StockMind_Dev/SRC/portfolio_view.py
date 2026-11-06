from datetime import date
import pandas as pd
import streamlit as st
from stockmind.application.portfolio.add_position_use_case import AddPositionUseCase
from stockmind.application.portfolio.delete_portfolio_use_cases import DeletePositionUseCase,DeletePurchaseLotUseCase,DeleteTradeUseCase
from stockmind.application.portfolio.portfolio_dashboard_use_case import PortfolioDashboardUseCase
from stockmind.application.portfolio.portfolio_performance_use_case import PortfolioPerformanceUseCase
from stockmind.application.portfolio.sell_position_use_case import SellPositionUseCase
from stockmind.application.portfolio.update_purchase_lot_use_case import UpdatePurchaseLotUseCase
from stockmind.infrastructure.watchlists.watchlist_repository import WatchlistRepository

def _money(v):return '–' if v is None else f'{v:,.2f} €'
def render():
 r=PortfolioDashboardUseCase().load();st.subheader('Portfolio');st.caption('Eine Position je Aktie, mehrere einzeln verwaltbare Kauftranchen.')
 c1,c2,c3,c4=st.columns(4);c1.metric('Investiert',_money(r.invested_amount));c2.metric('Marktwert',_money(r.market_value));c3.metric('Unrealisiert',_money(r.unrealized_profit));c4.metric('Realisiert netto',_money(r.realized_net_profit))
 tabs=st.tabs(['Offene Positionen','Kauf hinzufügen','Kauftranchen verwalten','Position verkaufen','Trade History','Performance'])
 with tabs[0]:
  if not r.positions:st.info('Noch keine offenen Positionen vorhanden.')
  else:
   st.dataframe(pd.DataFrame([{'Aktie':f'{x.position.company_name} ({x.position.symbol})','Tranchen':len(x.lots),'Erster Kauf':x.position.purchase_date,'Stück':x.position.quantity,'Ø Kaufkurs':round(x.position.purchase_price,2),'Gebühren €':round(x.position.purchase_fees,2),'Aktuell':x.current_price,'Investiert €':round(x.invested_amount,2),'Marktwert €':round(x.market_value,2) if x.market_value is not None else None,'P/L €':round(x.unrealized_profit,2) if x.unrealized_profit is not None else None,'P/L %':round(x.unrealized_return_pct*100,2) if x.unrealized_return_pct is not None else None,'+8 % Ziel':round(x.target_price,2),'Signal':x.current_signal,'Score':x.current_score} for x in r.positions]),width='stretch',hide_index=True)
 with tabs[1]:
  watch=[x for x in WatchlistRepository().load_all() if x.active];labels={f'{x.company_name} ({x.symbol})':x.symbol for x in watch}
  if not labels:st.warning('Keine aktiven Watchlist-Aktien.')
  else:
   with st.form('add_lot'):
    label=st.selectbox('Aktie',list(labels));d=st.date_input('Kaufdatum',date.today());a,b,c=st.columns(3);price=a.number_input('Kaufpreis',min_value=.01,step=.01);qty=b.number_input('Stückzahl',min_value=.0001,step=1.,format='%.4f');fees=c.number_input('Kaufgebühren',min_value=0.,step=.01);profile=st.selectbox('Entry-Profil',['conservative','balanced','aggressive'],index=1);note=st.text_area('Notiz');submit=st.form_submit_button('Kauf hinzufügen',type='primary')
   if submit:
    AddPositionUseCase().execute(labels[label],d,price,qty,fees,profile,note);st.success('Kauftranche hinzugefügt und Position neu kumuliert.');st.rerun()
 with tabs[2]:
  lots=[(x,lot) for x in r.positions for lot in x.lots]
  if not lots:st.info('Keine Kauftranchen vorhanden.')
  else:
   names={f'{x.position.symbol} · {lot.purchase_date} · {lot.quantity:g} Stück zu {lot.purchase_price:.2f} €':lot.id for x,lot in lots};sel=st.selectbox('Kauftranche',list(names));lot=next(l for _,l in lots if l.id==names[sel])
   with st.form('edit_lot'):
    d=st.date_input('Kaufdatum',date.fromisoformat(lot.purchase_date));a,b,c=st.columns(3);price=a.number_input('Kaufpreis',min_value=.01,value=float(lot.purchase_price));qty=b.number_input('Stückzahl',min_value=.0001,value=float(lot.quantity),format='%.4f');fees=c.number_input('Gebühren',min_value=0.,value=float(lot.purchase_fees));profile=st.selectbox('Profil',['conservative','balanced','aggressive'],index=['conservative','balanced','aggressive'].index(lot.entry_profile));note=st.text_area('Notiz',lot.note);save=st.form_submit_button('Änderungen speichern')
   if save:UpdatePurchaseLotUseCase().execute(lot.id,d,price,qty,fees,profile,note);st.success('Kauftranche aktualisiert.');st.rerun()
   confirm=st.checkbox('Ich bestätige das dauerhafte Löschen dieser Kauftranche.',key='confirm_lot_delete')
   if st.button('Kauftranche löschen',disabled=not confirm):DeletePurchaseLotUseCase().execute(lot.id);st.success('Kauftranche gelöscht.');st.rerun()
   st.divider();position_choices={f'{x.position.company_name} ({x.position.symbol})':x.position.id for x in r.positions};pname=st.selectbox('Komplette offene Position löschen',list(position_choices));confirmp=st.checkbox('Ich bestätige das dauerhafte Löschen der kompletten offenen Position.')
   if st.button('Position ohne Verkauf löschen',disabled=not confirmp):DeletePositionUseCase().execute(position_choices[pname]);st.success('Position und Kauftranchen gelöscht.');st.rerun()
 with tabs[3]:
  if not r.positions:st.info('Keine offene Position vorhanden.')
  else:
   choices={f'{x.position.company_name} ({x.position.symbol}) · {x.position.quantity:g} Stück':x.position.id for x in r.positions}
   with st.form('sell_position'):
    label=st.selectbox('Position',list(choices));d=st.date_input('Verkaufsdatum',date.today());a,b,c=st.columns(3);price=a.number_input('Verkaufspreis',min_value=.01);fees=b.number_input('Verkaufsgebühren',min_value=0.);tax=c.number_input('Steuer',min_value=0.);reason=st.selectbox('Exit-Grund',['MANUAL','TARGET_REACHED','TIME_LIMIT','STOP_LOSS','SIGNAL_DETERIORATION']);note=st.text_area('Verkaufsnotiz');submit=st.form_submit_button('Position vollständig verkaufen',type='primary')
   if submit:trade=SellPositionUseCase().execute(choices[label],d,price,fees,tax,reason,note);st.success(f'Trade abgeschlossen: {_money(trade.net_profit)}');st.rerun()
 with tabs[4]:
  if not r.trades:st.info('Noch keine abgeschlossenen Trades.')
  else:
   st.dataframe(pd.DataFrame([{'ID':t.id,'Aktie':f'{t.company_name} ({t.symbol})','Kauf':t.purchase_date,'Verkauf':t.sale_date,'Stück':t.quantity,'Ø Kaufkurs':t.purchase_price,'Verkaufskurs':t.sale_price,'Netto €':round(t.net_profit,2),'Netto %':round(t.net_return_pct*100,2),'Exit':t.exit_reason} for t in r.trades]),width='stretch',hide_index=True)
   tc={f'{t.symbol} · Verkauf {t.sale_date} · {t.net_profit:.2f} €':t.id for t in r.trades};chosen=st.selectbox('Fehlerhaften Trade löschen',list(tc));confirmt=st.checkbox('Ich bestätige das dauerhafte Löschen des Trades.')
   if st.button('Trade löschen',disabled=not confirmt):DeleteTradeUseCase().execute(tc[chosen]);st.success('Trade gelöscht.');st.rerun()
 with tabs[5]:
  perf=PortfolioPerformanceUseCase().load();labels={'month':'Dieser Monat','six_months':'Letzte 6 Monate','ytd':'Seit 01.01.','twelve_months':'Letzte 12 Monate','all':'Gesamt'};st.dataframe(pd.DataFrame([{'Zeitraum':label,'Trades':perf[k]['trade_count'],'Gewinner':perf[k]['winner_count'],'Win Rate %':round(perf[k]['win_rate']*100,2),'Netto €':round(perf[k]['net_profit'],2),'Ø Haltedauer':round(perf[k]['average_holding_days'],1)} for k,label in labels.items()]),width='stretch',hide_index=True)
