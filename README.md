PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> & d:/Users/Michael/Dokumente/16_AppDev/stockmind-platform/.venv/Scripts/Activate.ps1                              python scripts/refresh_indicator_chart_data.py                                      v\stockmind-platform> 
Traceback (most recent call last):
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\scripts\refresh_indicator_chart_data.py",line 247, in <module>
    main()
    ~~~~^^
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\scripts\refresh_indicator_chart_data.py",line 224, in main
    repository = IndicatorChartDataRepository()
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\src\stockmind\infrastructure\history\indicator_chart_data_repository.py", line 17, in __init__
    self._initialize()
    ~~~~~~~~~~~~~~~~^^
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\src\stockmind\infrastructure\history\indicator_chart_data_repository.py", line 34, in _initialize
    cursor.execute(
    ~~~~~~~~~~~~~~^
        """
        ^^^
    ...<29 lines>...
        """
        ^^^
    )
    ^
sqlite3.OperationalError: table indicator_chart_data already exists
