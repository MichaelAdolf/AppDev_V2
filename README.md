AttributeError: 'IndicatorChartPoint' object has no attribute 'adx'

File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\ui\streamlit_app.py", line 90, in <module>
    render_stock_detail(
    ~~~~~~~~~~~~~~~~~~~^
        profile_name=profile,
        ^^^^^^^^^^^^^^^^^^^^^
        symbol=selected_symbol
        ^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\ui\components\stock_detail_view.py", line 362, in render
    render_adx_chart(
    ~~~~~~~~~~~~~~~~^
        dashboard.symbol
        ^^^^^^^^^^^^^^^^
    )
    ^
File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\ui\components\indicator_charts.py", line 183, in render_adx_chart
    point.adx
