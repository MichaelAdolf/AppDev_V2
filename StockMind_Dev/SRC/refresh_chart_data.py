import math
from stockmind.application.currency.eur_market_data_service import EurMarketDataService
from stockmind.domain.history.chart_point import ChartPoint
from stockmind.infrastructure.history.chart_data_repository import ChartDataRepository
from stockmind.infrastructure.watchlists.watchlist_repository import WatchlistRepository

def get_symbols():return WatchlistRepository().load_active_symbols()
def _number(value):
 try:n=float(value);return n if math.isfinite(n) else None
 except (TypeError,ValueError):return None
def build_chart_points(symbol):
 result=EurMarketDataService().history(symbol,'5y');eur=result.data_eur;source=result.data_source;rates=result.fx_rates
 if eur.empty:return []
 middle=eur['Close'].rolling(20).mean();std=eur['Close'].rolling(20).std();upper=middle+2*std;lower=middle-2*std;points=[]
 for i,row in eur.iterrows():
  close=_number(row.get('Close'))
  if close is None:continue
  raw=source.loc[i];points.append(ChartPoint(symbol.upper(),i.date().isoformat(),close,_number(upper.loc[i]),_number(middle.loc[i]),_number(lower.loc[i]),_number(row.get('Open')),_number(row.get('High')),_number(row.get('Low')),result.source_currency,float(rates.loc[i]),_number(raw.get('Open')),_number(raw.get('High')),_number(raw.get('Low')),_number(raw.get('Close'))))
 return points
def main():
 repo=ChartDataRepository()
 for symbol in get_symbols():
  print(f'Refreshing EUR-normalized OHLC chart data for {symbol}');points=build_chart_points(symbol)
  if points:repo.replace_for_symbol(symbol,points)
  else:print(f'Skipping {symbol}: no valid chart data')
 print('EUR-normalized chart data refresh complete.')
if __name__=='__main__':main()
