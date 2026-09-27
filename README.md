(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> python -m unittest tests.test_true_incremental_repositories
.
----------------------------------------------------------------------
Ran 1 test in 0.026s

OK
(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> python -m unittest tests.test_refresh_coordinator          
.
----------------------------------------------------------------------
Ran 1 test in 0.003s

OK
(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> python scripts/run_daily_refresh.py                                                 
Traceback (most recent call last):
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\scripts\run_daily_refresh.py", line 2, in <module>
    from stockmind.application.refresh.refresh_coordinator import RefreshCoordinator
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\src\stockmind\application\refresh\refresh_coordinator.py", line 2, in <module>
    from stockmind.application.refresh.bootstrap_stock_use_case import BootstrapStockUseCase
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\src\stockmind\application\refresh\bootstrap_stock_use_case.py", line 4, in <module>
    from stockmind.application.refresh.incremental_market_refresh import refresh_symbol
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\src\stockmind\application\refresh\incremental_market_refresh.py", line 2, in <module>
    from scripts.refresh_chart_data import build_chart_points
ModuleNotFoundError: No module named 'scripts'
