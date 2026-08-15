PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> & d:/Users/Michael/Dokumente/16_AppDev/stockmind-platform/.venv/Scripts/Activate.ps1                              python scripts/refresh_fundamental_data.py                                          v\stockmind-platform> 
Refreshing fundamentals for NVDA
Traceback (most recent call last):
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\scripts\refresh_fundamental_data.py", line 166, in <module>
    main()
    ~~~~^^
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\scripts\refresh_fundamental_data.py", line 150, in main
    entry = build_entry(
        symbol
    )
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\scripts\refresh_fundamental_data.py", line 73, in build_entry
    return FundamentalDataEntry(
        symbol=symbol,
    ...<59 lines>...
        )
    )
TypeError: FundamentalDataEntry.__init__() missing 1 required positional argument: 'current_price'
