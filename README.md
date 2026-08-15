UnboundLocalError: cannot access local variable 'period' where it is not associated with a value

File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\ui\streamlit_app.py", line 90, in <module>
    render_stock_detail(
    ~~~~~~~~~~~~~~~~~~~^
        profile_name=profile,
        ^^^^^^^^^^^^^^^^^^^^^
        symbol=selected_symbol
        ^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\ui\components\stock_detail_view.py", line 349, in render
    render_price_chart(
    ~~~~~~~~~~~~~~~~~~^
        dashboard.symbol
        ^^^^^^^^^^^^^^^^
    )
    ^
File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\ui\components\price_chart.py", line 79, in render
    period.end_date
    ^^^^^^
