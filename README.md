AttributeError: 'NoneType' object has no attribute 'fundamental_score'

File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\ui\streamlit_app.py", line 90, in <module>
    render_stock_detail(
    ~~~~~~~~~~~~~~~~~~~^
        profile_name=profile,
        ^^^^^^^^^^^^^^^^^^^^^
        symbol=selected_symbol
        ^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\ui\components\stock_detail_view.py", line 438, in render
    f"{fundamentals.fundamental_score:.0f}/100"
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
