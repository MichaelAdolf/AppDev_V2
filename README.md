(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> python scripts/test_daily_buy_signals.py
conservative: BUY=False, quality=LOW, missing=['rsi_oversold', 'lower_bollinger', 'adx_strength']
balanced: BUY=False, quality=LOW, missing=['rsi_oversold', 'lower_bollinger', 'adx_strength']
aggressive: BUY=True, quality=MEDIUM, missing=[]
Profile-dependent BUY signal test: OK
(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> python -m unittest tests.test_daily_signal_repository.py
E
======================================================================
ERROR: test_daily_signal_repository (unittest.loader._FailedTest.test_daily_signal_repository)
----------------------------------------------------------------------
ImportError: Failed to import test module: test_daily_signal_repository
Traceback (most recent call last):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.3824.0_x64__qbz5n2kfra8p0\Lib\unittest\loader.py", line 137, in loadTestsFromName
    module = __import__(module_name)
ModuleNotFoundError: No module named 'tests.test_daily_signal_repository'


----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
