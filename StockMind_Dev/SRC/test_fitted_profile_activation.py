import unittest
from types import SimpleNamespace
from unittest.mock import patch
from stockmind.application.strategy.activate_fitted_profile_use_case import ActivateFittedProfileUseCase
class FittedProfileActivationTest(unittest.TestCase):
 @patch('stockmind.application.strategy.activate_fitted_profile_use_case.FittedProfileRepository')
 def test_only_validated_candidate_can_be_activated(self,repo_type):
  repo_type.return_value.load.return_value=SimpleNamespace(id='p1',symbol='NVDA',status='VALIDATED');repo_type.return_value.load.side_effect=[SimpleNamespace(id='p1',symbol='NVDA',status='VALIDATED'),SimpleNamespace(id='p1',symbol='NVDA',status='ACTIVE')]
  result=ActivateFittedProfileUseCase().execute('p1');repo_type.return_value.activate.assert_called_once_with('p1','NVDA');self.assertEqual(result.status,'ACTIVE')
 @patch('stockmind.application.strategy.activate_fitted_profile_use_case.FittedProfileRepository')
 def test_non_validated_candidate_is_rejected(self,repo_type):
  repo_type.return_value.load.return_value=SimpleNamespace(id='p1',symbol='NVDA',status='DEGRADED')
  with self.assertRaises(ValueError):ActivateFittedProfileUseCase().execute('p1')
if __name__=='__main__':unittest.main()
