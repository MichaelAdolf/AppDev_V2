(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> streamlit run ui/streamlit_app.py
2026-09-26 18:30:46.865 Uvicorn server started on :::8501

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.178.32:8501

  Help agents write better Streamlit apps?
  Install the official Streamlit skills by running streamlit skills in your terminal.

2026-09-26 18:30:48.892 Uncaught app execution
Traceback (most recent call last):
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\.venv\Lib\site-packages\streamlit\runtime\scriptrunner\exec_code.py", line 136, in exec_func_with_error_handling
    result = func()
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\.venv\Lib\site-packages\streamlit\runtime\scriptrunner\script_runner.py", line 816, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\ui\streamlit_app.py", line 157, in <module>
    selected_symbol = render_stock_selector(profile, show_heading=False)
TypeError: render() got an unexpected keyword argument 'show_heading'
