from dataclasses import dataclass
import math
import pandas as pd
import yfinance as yf
from stockmind.infrastructure.currency.currency_repository import CurrencyRepository

@dataclass(frozen=True)
class EurMarketDataResult:
    symbol: str
    source_currency: str
    data_source: pd.DataFrame
    data_eur: pd.DataFrame
    fx_rates: pd.Series

class EurMarketDataService:
    PRICE_COLUMNS=('Open','High','Low','Close')
    def __init__(self,database_path=None):self._repo=CurrencyRepository(database_path)
    def history(self,symbol,period='5y'):
        ticker=yf.Ticker(symbol);data=ticker.history(period=period).copy()
        if data.empty:return EurMarketDataResult(symbol.upper(),'EUR',data,data,pd.Series(dtype=float))
        if data.index.tz is not None:data.index=data.index.tz_localize(None)
        currency=self._resolve_currency(ticker,symbol)
        rates=self._rates_to_eur(currency,data.index,period)
        eur=self.convert_frame(data,rates)
        self._repo.save_instrument_currency(symbol,currency)
        self._repo.replace_rates(currency,'EUR',rates)
        return EurMarketDataResult(symbol.upper(),currency,data,eur,rates)
    def _resolve_currency(self,ticker,symbol):
        cached=self._repo.load_instrument_currency(symbol)
        values=[]
        try:values.append(ticker.fast_info.get('currency'))
        except Exception:pass
        try:values.append(ticker.history_metadata.get('currency'))
        except Exception:pass
        try:values.append(ticker.info.get('currency'))
        except Exception:pass
        currency=next((str(x).upper() for x in values if x),cached)
        if not currency:raise ValueError(f'Keine Instrumentwährung für {symbol} ermittelbar.')
        return currency
    def _rates_to_eur(self,currency,index,period):
        if currency=='EUR':return pd.Series(1.0,index=index,name='fx_rate_to_eur')
        direct=f'{currency}EUR=X';inverse=f'EUR{currency}=X'
        rates=self._download_fx(direct,period,index,invert=False)
        if rates is None:rates=self._download_fx(inverse,period,index,invert=True)
        if rates is None:raise ValueError(f'Kein historischer FX-Kurs {currency}→EUR verfügbar.')
        return rates
    def _download_fx(self,pair,period,target_index,invert):
        try:data=yf.Ticker(pair).history(period=period).copy()
        except Exception:return None
        if data.empty or 'Close' not in data:return None
        if data.index.tz is not None:data.index=data.index.tz_localize(None)
        series=pd.to_numeric(data['Close'],errors='coerce').replace([math.inf,-math.inf],pd.NA).dropna()
        if series.empty:return None
        if invert:series=1.0/series
        # Use the last known currency rate for exchange holidays; never look ahead
        normalized=series.groupby(series.index.normalize()).last()
        target=pd.DatetimeIndex(target_index).normalize()
        aligned=normalized.reindex(target,method='ffill')
        if aligned.isna().any():
            # Only initial history gaps use the first available quote
            aligned=aligned.bfill()
        aligned.index=target_index
        return aligned.astype(float).rename('fx_rate_to_eur')
    @classmethod
    def convert_frame(cls,data,rates):
        result=data.copy();aligned=rates.reindex(result.index)
        if aligned.isna().any():raise ValueError('FX-Historie enthält Lücken für Marktdaten.')
        for column in cls.PRICE_COLUMNS:
            if column in result:result[column]=pd.to_numeric(result[column],errors='coerce')*aligned
        if 'Dividends' in result:result['Dividends']=pd.to_numeric(result['Dividends'],errors='coerce')*aligned
        result.attrs['currency']='EUR';return result
