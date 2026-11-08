(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> python -m unittest tests.test_daily_mail_v3 tests.test_daily_mail_use_case tests.test_productive_exit_engine
>> 
.E...
======================================================================
ERROR: test_buy_section_contains_stock_if_any_profile_is_buy (tests.test_daily_mail_use_case.DailyMailUseCaseTest.test_buy_section_contains_stock_if_any_profile_is_buy)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.3824.0_x64__qbz5n2kfra8p0\Lib\unittest\mock.py", line 1432, in patched
    return func(*newargs, **newkeywargs)
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\tests\test_daily_mail_use_case.py", line 15, in test_buy_section_contains_stock_if_any_profile_is_buy
    result=DailyMailUseCase().build();self.assertEqual(len(result.buy_signal_stocks),1);self.assertEqual(result.buy_signal_stocks[0].profiles[1].signal,"BUY")
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\src\stockmind\application\notifications\daily_mail_use_case.py", line 23, in build
    profiles.append(ProfileSignalMailItem(profile_name=entry.profile_name,signal=signal,target_hit_rate=entry.target_hit_rate,complete_period_count=count,sample_quality=quality,opportunity_score=entry.score,confidence=entry.confidence,risk_level=entry.risk_level))
                                   ^^^^^^^^^^^
AttributeError: 'types.SimpleNamespace' object has no attribute 'score'

----------------------------------------------------------------------
Ran 5 tests in 0.004s

FAILED (errors=1)
