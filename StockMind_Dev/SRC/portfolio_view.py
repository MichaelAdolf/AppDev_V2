from datetime import date
import pandas as pd
import streamlit as st
from stockmind.application.portfolio.add_position_use_case import AddPositionUseCase
from stockmind.application.portfolio.delete_portfolio_use_cases import DeletePositionUseCase,DeletePurchaseLotUseCase,DeleteTradeUseCase
from stockmind.application.portfolio.portfolio_dashboard_use_case import PortfolioDashboardUseCase
from stockmind.application.portfolio.portfolio_intelligence_use_case import PortfolioIntelligenceUseCase
from stockmind.application.portfolio.portfolio_performance_use_case import PortfolioPerformanceUseCase
from stockmind.application.portfolio.sell_position_use_case import SellPositionUseCase
from stockmind.application.portfolio.update_purchase_lot_use_case import UpdatePurchaseLotUseCase
from stockmind.infrastructure.watchlists.watchlist_repository import WatchlistRepository

def _money(v):return '–' if v is None else f'{v:,.2f} €'
def _pct(v):return '–' if v is None else f'{v:.1%}'
def render():
 r=PortfolioDashboardUseCase().load();intel=PortfolioIntelligenceUseCase().load();st.subheader('Portfolio');st.caption('Positionsüberwachung für das +8-%-Ziel innerhalb von 60 Kalendertagen. Hinweise markieren Prüfbedarf, noch keine automatische Verkaufsentscheidung.')
 c1,c2,c3,c4=st.columns(4);c1.metric('Investiert',_money(r.invested_amount));c2.metric('Marktwert',_money(r.market_value));c3.metric('Unrealisiert',_money(r.unrealized_profit));c4.metric('Realisiert netto',_money(r.realized_net_profit))
 tabs=st.tabs(['Position Intelligence','Offene Positionen','Kauf hinzufügen','Kauftranchen verwalten','Position verkaufen','Trade History','Performance'])
 with tabs[0]:
  if not intel:st.info('Noch keine offenen Positionen vorhanden.')
  for x in intel:
   icon='🔴' if x.attention_level=='CRITICAL' else '🟡' if x.attention_level=='ATTENTION' else '🔵'
   with st.expander(f'{icon} {x.company_name} ({x.symbol}) · {_pct(x.unrealized_return_pct)} · Tag {x.holding_days}/60',expanded=x.attention_level!='NORMAL'):
    a,b,c,d=st.columns(4);a.metric('P/L',_money(x.unrealized_profit),_pct(x.unrealized_return_pct));b.metric('+8-%-Ziel',_money(x.target_price));c.metric('Restlaufzeit',f'{x.remaining_strategy_days} Tage');d.metric('Status',x.attention_level)
    st.write('**Entry → Heute**');st.dataframe(pd.DataFrame([{'Kennzahl':'Opportunity Score','Entry':x.entry_score,'Heute':x.current_score,'Δ':x.score_change},{'Kennzahl':'Confidence','Entry':x.entry_confidence,'Heute':x.current_confidence,'Δ':x.confidence_change},{'Kennzahl':'Risk','Entry':x.entry_risk,'Heute':x.current_risk,'Δ':''},{'Kennzahl':'Signal','Entry':x.entry_signal,'Heute':x.current_signal,'Δ':''}]),hide_index=True,width='stretch')
    if x.attention_reasons:st.warning('Prüfhintergrund: '+', '.join(x.attention_reasons))
    st.caption(f'{len(x.lots)} Kauftranchen · {x.quantity:g} Stück · gewichteter Kaufkurs {x.weighted_purchase_price:.2f} €')
 with tabs[1]:
  st.dataframe(pd.DataFrame([{'Aktie':f'{x.position.company_name} ({x.position.symbol})','Tranchen':len(x.lots),'Stück':x.position.quantity,'Ø Kaufkurs':round(x.position.purchase_price,2),'Aktuell':x.current_price,'P/L €':round(x.unrealized_profit,2) if x.unrealized_profit is not None else None,'P/L %':round(x.unrealized_return_pct*100,2) if x.unrealized_return_pct is not None else None,'Signal':x.current_signal,'Score':x.current_score} for x in r.positions]),width='stretch',hide_index=True) if r.positions else st.info('Noch keine offenen Positionen vorhanden.')
 with tabs[2]:
  watch=[x for x in WatchlistRepository().load_all() if x.active];labels={f'{x.company_name} ({x.symbol})':x.symbol for x in watch}
  if labels:
   with st.form('add_lot'):
    label=st.selectbox('Aktie',list(labels));d=st.date_input('Kaufdatum',date.today());a,b,c=st.columns(3);price=a.number_input('Kaufpreis',min_value=.01);qty=b.number_input('Stückzahl',min_value=.0001,format='%.4f');fees=c.number_input('Kaufgebühren',min_value=0.);profile=st.selectbox('Entry-Profil',['conservative','balanced','aggressive'],index=1);note=st.text_area('Notiz');submit=st.form_submit_button('Kauf hinzufügen',type='primary')
   if submit:AddPositionUseCase().execute(labels[label],d,price,qty,fees,profile,note);st.success('Kauf hinzugefügt.');st.rerun()
 with tabs[3]:
  lots=[(x,lot) for x in r.positions for lot in x.lots]
  if lots:
   names={f'{x.position.symbol} · {lot.purchase_date} · {lot.quantity:g} Stück zu {lot.purchase_price:.2f} €':lot.id for x,lot in lots};sel=st.selectbox('Kauftranche',list(names));lot=next(l for _,l in lots if l.id==names[sel])
   with st.form('edit_lot'):
    d=st.date_input('Kaufdatum',date.fromisoformat(lot.purchase_date));a,b,c=st.columns(3);price=a.number_input('Kaufpreis',min_value=.01,value=float(lot.purchase_price));qty=b.number_input('Stückzahl',min_value=.0001,value=float(lot.quantity),format='%.4f');fees=c.number_input('Gebühren',min_value=0.,value=float(lot.purchase_fees));profile=st.selectbox('Profil',['conservative','balanced','aggressive'],index=['conservative','balanced','aggressive'].index(lot.entry_profile));note=st.text_area('Notiz',lot.note);save=st.form_submit_button('Änderungen speichern')
   if save:UpdatePurchaseLotUseCase().execute(lot.id,d,price,qty,fees,profile,note);st.rerun()
   confirm=st.checkbox('Kauftranche dauerhaft löschen.');
   if st.button('Kauftranche löschen',disabled=not confirm):DeletePurchaseLotUseCase().execute(lot.id);st.rerun()
  else:st.info('Keine Kauftranchen vorhanden.')
 with tabs[4]:
  if r.positions:
   choices={f'{x.position.company_name} ({x.position.symbol}) · {x.position.quantity:g} Stück':x.position.id for x in r.positions}
   with st.form('sell_position'):
    label=st.selectbox('Position',list(choices));d=st.date_input('Verkaufsdatum',date.today());a,b,c=st.columns(3);price=a.number_input('Verkaufspreis',min_value=.01);fees=b.number_input('Verkaufsgebühren',min_value=0.);tax=c.number_input('Steuer',min_value=0.);reason=st.selectbox('Exit-Grund',['MANUAL','TARGET_REACHED','TIME_LIMIT','STOP_LOSS','SIGNAL_DETERIORATION']);note=st.text_area('Verkaufsnotiz');submit=st.form_submit_button('Position vollständig verkaufen',type='primary')
   if submit:trade=SellPositionUseCase().execute(choices[label],d,price,fees,tax,reason,note);st.success(f'Trade abgeschlossen: {_money(trade.net_profit)}');st.rerun()
  else:st.info('Keine offene Position vorhanden.')
 with tabs[5]:
  if r.trades:
   st.dataframe(pd.DataFrame([{'Aktie':f'{t.company_name} ({t.symbol})','Kauf':t.purchase_date,'Verkauf':t.sale_date,'Netto €':round(t.net_profit,2),'Netto %':round(t.net_return_pct*100,2),'Profil':t.entry_profile,'Exit':t.exit_reason} for t in r.trades]),width='stretch',hide_index=True)
   tc={f'{t.symbol} · {t.sale_date} · {t.net_profit:.2f} €':t.id for t in r.trades};chosen=st.selectbox('Fehlerhaften Trade löschen',list(tc));confirm=st.checkbox('Trade dauerhaft löschen.')
   if st.button('Trade löschen',disabled=not confirm):DeleteTradeUseCase().execute(tc[chosen]);st.rerun()
  else:st.info('Noch keine abgeschlossenen Trades.')
 with tabs[6]:
  perf=PortfolioPerformanceUseCase().load();periods={'month':'Dieser Monat','six_months':'Letzte 6 Monate','ytd':'Seit 01.01.','twelve_months':'Letzte 12 Monate','all':'Gesamt'};st.dataframe(pd.DataFrame([{'Zeitraum':label,'Trades':perf[k]['trade_count'],'Win Rate %':round(perf[k]['win_rate']*100,1),'Netto €':round(perf[k]['net_profit'],2),'Ø Gewinner €':round(perf[k]['average_winner'],2),'Ø Verlierer €':round(perf[k]['average_loser'],2),'Ø Tage':round(perf[k]['average_holding_days'],1)} for k,label in periods.items()]),width='stretch',hide_index=True);st.subheader('Performance nach Entry-Profil');st.dataframe(pd.DataFrame([{'Profil':p,'Trades':v['trade_count'],'Win Rate %':round(v['win_rate']*100,1),'Netto €':round(v['net_profit'],2),'Ø Tage':round(v['average_holding_days'],1)} for p,v in perf['by_profile'].items()]),width='stretch',hide_index=True)
