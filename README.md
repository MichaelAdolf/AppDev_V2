(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> python -m unittest tests.test_refresh_coordinator
E
======================================================================
ERROR: test_refresh_coordinator (unittest.loader._FailedTest.test_refresh_coordinator)
----------------------------------------------------------------------
ImportError: Failed to import test module: test_refresh_coordinator
Traceback (most recent call last):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.3824.0_x64__qbz5n2kfra8p0\Lib\unittest\loader.py", line 137, in loadTestsFromName
    module = __import__(module_name)
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\tests\test_refresh_coordinator.py", line 3, in <module>
    from stockmind.application.refresh.refresh_coordinator import RefreshCoordinator
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\src\stockmind\application\refresh\refresh_coordinator.py", line 2, in <module>
    from stockmind.application.refresh.bootstrap_stock_use_case import BootstrapStockUseCase
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\src\stockmind\application\refresh\bootstrap_stock_use_case.py", line 4, in <module>
    from stockmind.application.refresh.incremental_market_refresh import refresh_symbol
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\src\stockmind\application\refresh\incremental_market_refresh.py", line 2, in <module>
    from refresh_chart_data import build_chart_points
ModuleNotFoundError: No module named 'refresh_chart_data'


----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
