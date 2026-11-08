import unittest
from types import SimpleNamespace
from unittest.mock import patch
from stockmind.application.strategy.fitted_profile_validation_use_case import FittedProfileValidationUseCase
class FittedProfileValidationTest(unittest.TestCase):
 @patch('stockmind.application.strategy.fitted_profile_validation_use_case.ProfileRepository')
 @patch('stockmind.application.strategy.fitted_profile_validation_use_case.IndicatorChartDataRepository')
 @patch('stockmind.application.strategy.fitted_profile_validation_use_case.ChartDataRepository')
 @patch('stockmind.application.strategy.fitted_profile_validation_use_case.FittedProfileRepository')
 def test_insufficient_sample_is_persisted(self,repo,chart,indicators,profiles):
  p=SimpleNamespace(id='p1',symbol='NVDA',version=1,base_profile='balanced',rsi_oversold_threshold=30,rsi_overbought_threshold=70,bollinger_lower_threshold=.25,adx_trend_strength_threshold=20,stochastic_oversold_threshold=20);repo.return_value.load.return_value=p;profiles.return_value.get_by_name.return_value=p
  chart.return_value.load_by_symbol.return_value=[];indicators.return_value.load_by_symbol.return_value=[]
  r=FittedProfileValidationUseCase().validate('p1');self.assertEqual(r.status,'INSUFFICIENT_SAMPLE');repo.return_value.update_status.assert_called_with('p1','INSUFFICIENT_SAMPLE');repo.return_value.save_validation.assert_called_once()
if __name__=='__main__':unittest.main()
