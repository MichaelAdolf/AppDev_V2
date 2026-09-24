(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> python scripts/refresh_chart_data.py
Refreshing chart data for AAPL
Refreshing chart data for AMD
Refreshing chart data for AMZN
Refreshing chart data for ASML
Refreshing chart data for NFLX
Refreshing chart data for NVDA
Refreshing chart data for SAP
Chart data refresh complete.
(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> python -m unittest tests.test_analysis_history_profile_filter
.
----------------------------------------------------------------------
Ran 1 test in 0.037s

OK
(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> python -m unittest tests.test_stock_detail_company_name
E
======================================================================
ERROR: test_company_name_from_watchlist (tests.test_stock_detail_company_name.StockDetailCompanyNameTest.test_company_name_from_watchlist)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.3824.0_x64__qbz5n2kfra8p0\Lib\unittest\mock.py", line 1429, in patched
    with self.decoration_helper(patched,
         ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
                                args,
                                ^^^^^
                                keywargs) as (newargs, newkeywargs):
                                ^^^^^^^^^
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.3824.0_x64__qbz5n2kfra8p0\Lib\contextlib.py", line 141, in __enter__
    return next(self.gen)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.3824.0_x64__qbz5n2kfra8p0\Lib\unittest\mock.py", line 1411, in decoration_helper
    arg = exit_stack.enter_context(patching)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.3824.0_x64__qbz5n2kfra8p0\Lib\contextlib.py", line 530, in enter_context
    result = _enter(cm)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.3824.0_x64__qbz5n2kfra8p0\Lib\unittest\mock.py", line 1503, in __enter__
    original, local = self.get_original()
                      ~~~~~~~~~~~~~~~~~^^
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.3824.0_x64__qbz5n2kfra8p0\Lib\unittest\mock.py", line 1473, in get_original
    raise AttributeError(
        "%s does not have the attribute %r" % (target, name)
    )
AttributeError: <module 'stockmind.application.dashboard.use_cases.stock_detail_dashboard_use_case' from 'D:\\Users\\Michael\\Dokumente\\16_AppDev\\stockmind-platform\\src\\stockmind\\application\\dashboard\\use_cases\\stock_detail_dashboard_use_case.py'> does not have the attribute 'WatchlistRepository'

----------------------------------------------------------------------
Ran 1 test in 0.005s

FAILED (errors=1)
(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> streamlit run ui/streamlit_app.py                            
2026-09-24 20:17:33.949 Uvicorn server started on :::8501

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.178.32:8501

  Help agents write better Streamlit apps?
  Install the official Streamlit skills by running streamlit skills in your terminal.

2026-09-24 20:17:36.659 Uncaught app execution
Traceback (most recent call last):
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\.venv\Lib\site-packages\streamlit\runtime\scriptrunner\exec_code.py", line 136, in exec_func_with_error_handling
    result = func()
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\.venv\Lib\site-packages\streamlit\runtime\scriptrunner\script_runner.py", line 816, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\ui\streamlit_app.py", line 161, in <module>
    render_stock_detail(
    ~~~~~~~~~~~~~~~~~~~^
        profile_name=profile,
        ^^^^^^^^^^^^^^^^^^^^^
        symbol=selected_symbol
        ^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\ui\components\stock_detail_view.py", line 48, in render
    .load(
     ~~~~^
        profile_name=profile_name,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^
        symbol=symbol
        ^^^^^^^^^^^^^
    )
    ^
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\src\stockmind\application\dashboard\use_cases\stock_detail_dashboard_use_case.py", line 44, in load
    return StockDetailDashboardResult(
        symbol=stock.symbol,
    ...<32 lines>...
        period_negative_rate=stats.negative_rate,
    )
TypeError: StockDetailDashboardResult.__init__() missing 1 required positional argument: 'company_name'
