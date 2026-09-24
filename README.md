(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> streamlit run ui/streamlit_app.py
2026-09-24 17:50:26.623 Uvicorn server started on :::8501

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.178.32:8501

  Help agents write better Streamlit apps?
  Install the official Streamlit skills by running streamlit skills in your terminal.

2026-09-24 17:50:28.392 Please replace `use_container_width` with `width`.

`use_container_width` will be removed after 2025-12-31.

For `use_container_width=True`, use `width='stretch'`. For `use_container_width=False`, use `width='content'`.
2026-09-24 17:50:29.098 Please replace `use_container_width` with `width`.

`use_container_width` will be removed after 2025-12-31.

For `use_container_width=True`, use `width='stretch'`. For `use_container_width=False`, use `width='content'`.
2026-09-24 17:50:29.105 Please replace `use_container_width` with `width`.

`use_container_width` will be removed after 2025-12-31.

For `use_container_width=True`, use `width='stretch'`. For `use_container_width=False`, use `width='content'`.
2026-09-24 17:50:29.496 Please replace `use_container_width` with `width`.

`use_container_width` will be removed after 2025-12-31.

For `use_container_width=True`, use `width='stretch'`. For `use_container_width=False`, use `width='content'`.
2026-09-24 17:50:29.545 Please replace `use_container_width` with `width`.

`use_container_width` will be removed after 2025-12-31.

For `use_container_width=True`, use `width='stretch'`. For `use_container_width=False`, use `width='content'`.
2026-09-24 17:50:29.620 Please replace `use_container_width` with `width`.

`use_container_width` will be removed after 2025-12-31.

For `use_container_width=True`, use `width='stretch'`. For `use_container_width=False`, use `width='content'`.
2026-09-24 17:50:29.662 Please replace `use_container_width` with `width`.

`use_container_width` will be removed after 2025-12-31.

For `use_container_width=True`, use `width='stretch'`. For `use_container_width=False`, use `width='content'`.
2026-09-24 17:50:29.684 Please replace `use_container_width` with `width`.

`use_container_width` will be removed after 2025-12-31.

For `use_container_width=True`, use `width='stretch'`. For `use_container_width=False`, use `width='content'`.
FUNDAMENTAL DB: D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\config\stockmind\stockmind.db
INITIALIZE FUNDAMENTAL REPOSITORY
2026-09-24 17:50:29.707 Uncaught app execution
Traceback (most recent call last):
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\.venv\Lib\site-packages\streamlit\runtime\scriptrunner\exec_code.py", line 136, in exec_func_with_error_handling
    result = func()
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\.venv\Lib\site-packages\streamlit\runtime\scriptrunner\script_runner.py", line 816, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\ui\streamlit_app.py", line 185, in <module>
    render_stock_detail(
    ~~~~~~~~~~~~~~~~~~~^
        profile_name=profile,
        ^^^^^^^^^^^^^^^^^^^^^
        symbol=selected_symbol
        ^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\ui\components\stock_detail_view.py", line 672, in render
    f"{buy_periods.overall_success_rate:.1f}%"
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'BuyPeriodDashboardResult' object has no attribute 'overall_success_rate'
