OK
(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> streamlit run ui/streamlit_app.py                                                   
2026-09-27 11:51:32.904 Uvicorn server started on :::8501

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.178.32:8501

  Help agents write better Streamlit apps?
  Install the official Streamlit skills by running streamlit skills in your terminal.

FUNDAMENTAL DB: D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\config\stockmind\stockmind.db
INITIALIZE FUNDAMENTAL REPOSITORY
FUNDAMENTAL DB: D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\config\stockmind\stockmind.db
INITIALIZE FUNDAMENTAL REPOSITORY
FUNDAMENTAL DB: D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\config\stockmind\stockmind.db
INITIALIZE FUNDAMENTAL REPOSITORY
FUNDAMENTAL DB: D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\config\stockmind\stockmind.db
INITIALIZE FUNDAMENTAL REPOSITORY
2026-09-27 11:54:09.441 Uncaught app execution
Traceback (most recent call last):
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\.venv\Lib\site-packages\streamlit\runtime\scriptrunner\exec_code.py", line 136, in exec_func_with_error_handling
    result = func()
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\.venv\Lib\site-packages\streamlit\runtime\scriptrunner\script_runner.py", line 816, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\ui\streamlit_app.py", line 164, in <module>
    render_stock_detail(
    ~~~~~~~~~~~~~~~~~~~^
        profile_name=profile,
        ^^^^^^^^^^^^^^^^^^^^^
        symbol=selected_symbol
        ^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\ui\components\stock_detail_view.py", line 53, in render
    .load(
     ~~~~^
        profile_name=profile_name,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^
        symbol=symbol
        ^^^^^^^^^^^^^
    )
    ^
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\src\stockmind\application\dashboard\use_cases\stock_detail_dashboard_use_case.py", line 19, in load
    setups=HistoricalSetupDashboardUseCase().load(symbol,profile_name=profile_name,analysis_period="5y")
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\src\stockmind\application\dashboard\use_cases\historical_setup_dashboard_use_case.py", line 74, in load
    sum(
    ~~~^
        setup.max_gain_pct
        ^^^^^^^^^^^^^^^^^^
        for setup in setups
        ^^^^^^^^^^^^^^^^^^^
    )
    ^
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
2026-09-27 11:54:22.953 Uncaught app execution
Traceback (most recent call last):
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\.venv\Lib\site-packages\streamlit\runtime\scriptrunner\exec_code.py", line 136, in exec_func_with_error_handling
    result = func()
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\.venv\Lib\site-packages\streamlit\runtime\scriptrunner\script_runner.py", line 816, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\ui\streamlit_app.py", line 164, in <module>
    render_stock_detail(
    ~~~~~~~~~~~~~~~~~~~^
        profile_name=profile,
        ^^^^^^^^^^^^^^^^^^^^^
        symbol=selected_symbol
        ^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\ui\components\stock_detail_view.py", line 53, in render
    .load(
     ~~~~^
        profile_name=profile_name,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^
        symbol=symbol
        ^^^^^^^^^^^^^
    )
    ^
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\src\stockmind\application\dashboard\use_cases\stock_detail_dashboard_use_case.py", line 19, in load
    setups=HistoricalSetupDashboardUseCase().load(symbol,profile_name=profile_name,analysis_period="5y")
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\src\stockmind\application\dashboard\use_cases\historical_setup_dashboard_use_case.py", line 74, in load
    sum(
    ~~~^
        setup.max_gain_pct
        ^^^^^^^^^^^^^^^^^^
        for setup in setups
        ^^^^^^^^^^^^^^^^^^^
    )
    ^
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
FUNDAMENTAL DB: D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\config\stockmind\stockmind.db
INITIALIZE FUNDAMENTAL REPOSITORY
FUNDAMENTAL DB: D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\config\stockmind\stockmind.db
INITIALIZE FUNDAMENTAL REPOSITORY
2026-09-27 11:54:28.782 Uncaught app execution
Traceback (most recent call last):
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\.venv\Lib\site-packages\streamlit\runtime\scriptrunner\exec_code.py", line 136, in exec_func_with_error_handling
    result = func()
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\.venv\Lib\site-packages\streamlit\runtime\scriptrunner\script_runner.py", line 816, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\ui\streamlit_app.py", line 164, in <module>
    render_stock_detail(
    ~~~~~~~~~~~~~~~~~~~^
        profile_name=profile,
        ^^^^^^^^^^^^^^^^^^^^^
        symbol=selected_symbol
        ^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\ui\components\stock_detail_view.py", line 53, in render
    .load(
     ~~~~^
        profile_name=profile_name,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^
        symbol=symbol
        ^^^^^^^^^^^^^
    )
    ^
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\src\stockmind\application\dashboard\use_cases\stock_detail_dashboard_use_case.py", line 19, in load
    setups=HistoricalSetupDashboardUseCase().load(symbol,profile_name=profile_name,analysis_period="5y")
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\src\stockmind\application\dashboard\use_cases\historical_setup_dashboard_use_case.py", line 74, in load
    sum(
    ~~~^
        setup.max_gain_pct
        ^^^^^^^^^^^^^^^^^^
        for setup in setups
        ^^^^^^^^^^^^^^^^^^^
    )
    ^
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
FUNDAMENTAL DB: D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\config\stockmind\stockmind.db
INITIALIZE FUNDAMENTAL REPOSITORY
FUNDAMENTAL DB: D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\config\stockmind\stockmind.db
INITIALIZE FUNDAMENTAL REPOSITORY
