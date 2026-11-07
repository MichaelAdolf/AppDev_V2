import unittest
from types import SimpleNamespace
from unittest.mock import patch
from stockmind.application.strategy.fitted_profile_search_use_case import FittedProfileSearchUseCase
class FittedProfileSearchTest(unittest.TestCase):
 @patch('stockmind.application.strategy.fitted_profile_search_use_case.ProfileRepository')
 @patch('stockmind.application.strategy.fitted_profile_search_use_case.IndicatorChartDataRepository')
 @patch('stockmind.application.strategy.fitted_profile_search_use_case.ChartDataRepository')
 def test_search_produces_ranked_candidates_without_changing_standard_profile(self,chart,indicators,profiles):
  base=SimpleNamespace(rsi_oversold_threshold=30,rsi_overbought_threshold=70,bollinger_lower_threshold=.25,adx_trend_strength_threshold=20,stochastic_oversold_threshold=20);profiles.return_value.get_by_name.return_value=base
  dates=['2025-01-01','2025-04-01','2025-07-01'];chart.return_value.load_by_symbol.return_value=[SimpleNamespace(trading_date=d,close_price=100,bollinger_lower=90,bollinger_upper=110,high_price=109,low_price=95) for d in dates]+[SimpleNamespace(trading_date='2026-10-01',close_price=100,bollinger_lower=90,bollinger_upper=110,high_price=100,low_price=100)]
  indicators.return_value.load_by_symbol.return_value=[SimpleNamespace(trading_date=d,rsi_14=25,adx=25,stoch_k=15) for d in dates]
  rows=FittedProfileSearchUseCase().search('NVDA','balanced',5);self.assertTrue(rows);self.assertEqual(base.rsi_oversold_threshold,30);self.assertTrue(all(x.status=='CANDIDATE' for x in rows))
if __name__=='__main__':unittest.main()
