(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> streamlit run ui/streamlit_app.py                            
2026-09-25 09:42:40.098 Uvicorn server started on :::8501

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.178.32:8501

  Help agents write better Streamlit apps?
  Install the official Streamlit skills by running streamlit skills in your terminal.

2026-09-25 09:42:56.937 Please replace `use_container_width` with `width`.

`use_container_width` will be removed after 2025-12-31.

For `use_container_width=True`, use `width='stretch'`. For `use_container_width=False`, use `width='content'`.
FUNDAMENTAL DB: D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\config\stockmind\stockmind.db
INITIALIZE FUNDAMENTAL REPOSITORY
2026-09-25 09:47:24.611 Uncaught app execution
Traceback (most recent call last):
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\.venv\Lib\site-packages\streamlit\runtime\scriptrunner\exec_code.py", line 136, in exec_func_with_error_handling
    result = func()
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\.venv\Lib\site-packages\streamlit\runtime\scriptrunner\script_runner.py", line 816, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\ui\streamlit_app.py", line 146, in <module>
    render_watchlist(profile)
    ~~~~~~~~~~~~~~~~^^^^^^^^^
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\ui\components\watchlist_view.py", line 54, in render
    alerts = AlertsDashboardUseCase().load(profile_name)
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\src\stockmind\application\dashboard\use_cases\alerts_dashboard_use_case.py", line 59, in load
    AlertResult(
    ~~~~~~~~~~~^
        title="Hohe Confidence",
        ^^^^^^^^^^^^^^^^^^^^^^^^
    ...<4 lines>...
        severity="success"
        ^^^^^^^^^^^^^^^^^^
    )
    ^
TypeError: AlertResult.__init__() missing 3 required positional arguments: 'symbol', 'profile_name', and 'reason'
