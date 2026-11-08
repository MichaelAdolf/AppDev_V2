(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> python scripts/apply_rc1_consensus_patch.py
>> 
Patched src\stockmind\application\dashboard\use_cases\stock_detail_dashboard_use_case.py
(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> python -m unittest tests.test_individual_activation_hardening tests.test_fitted_profile_activation tests.test_individual_daily_refresh_policy
..E..
======================================================================
ERROR: test_only_validated_candidate_can_be_activated (tests.test_fitted_profile_activation.FittedProfileActivationTest.test_only_validated_candidate_can_be_activated)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.3824.0_x64__qbz5n2kfra8p0\Lib\unittest\mock.py", line 1432, in patched
    return func(*newargs, **newkeywargs)
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\tests\test_fitted_profile_activation.py", line 9, in test_only_validated_candidate_can_be_activated
    result=ActivateFittedProfileUseCase().execute('p1');repo_type.return_value.activate.assert_called_once_with('p1','NVDA');self.assertEqual(result.status,'ACTIVE')
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\src\stockmind\application\strategy\activate_fitted_profile_use_case.py", line 5, in execute
    def execute(self,profile_id):return IndividualProfileActivationOrchestrator(self._database_path).execute(profile_id).profile
                                        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\src\stockmind\application\strategy\individual_profile_activation_orchestrator.py", line 15, in execute
    if candidate is None:raise ValueError('Fitted Profile wurde nicht gefunden.')
                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: Fitted Profile wurde nicht gefunden.

----------------------------------------------------------------------
Ran 5 tests in 0.017s

FAILED (errors=1)
