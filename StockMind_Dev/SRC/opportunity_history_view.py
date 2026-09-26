import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots
from stockmind.infrastructure.history.chart_data_repository import ChartDataRepository
def render(history,profile_name,symbol=None):
 if not history:st.warning("Kein historischer Opportunity-Replay vorhanden.");return
 df=pd.DataFrame([{"Datum":x.trading_date,"Opportunity Score":x.opportunity_score,"Confidence %":x.confidence*100,"Signal":x.signal,"Risiko":x.risk_level} for x in history])
 points=ChartDataRepository().load_by_symbol(symbol) if symbol else []
 fig=make_subplots(rows=2,cols=1,shared_xaxes=True,vertical_spacing=.06,row_heights=[.55,.45]);fig.add_trace(go.Scatter(x=[p.trading_date for p in points],y=[p.close_price for p in points],name="Kurs"),row=1,col=1);fig.add_trace(go.Scatter(x=df["Datum"],y=df["Opportunity Score"],name="Opportunity Score"),row=2,col=1)
 buy=df[df["Signal"]=="BUY"];fig.add_trace(go.Scatter(x=buy["Datum"],y=buy["Opportunity Score"],mode="markers",name="BUY",marker=dict(color="#00a046",size=5)),row=2,col=1);fig.update_layout(title=f"Kurs und Opportunity Score ({profile_name})",hovermode="x unified");fig.update_yaxes(title_text="Kurs",row=1,col=1);fig.update_yaxes(title_text="Score",range=[0,100],row=2,col=1);st.plotly_chart(fig,width="stretch")
