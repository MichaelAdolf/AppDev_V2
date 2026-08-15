(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> python scripts/refresh_fundamental_data.py
Refreshing fundamentals for NVDA
Traceback (most recent call last):
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\scripts\refresh_fundamental_data.py", line 172, in <module>
    main()
    ~~~~^^
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\scripts\refresh_fundamental_data.py", line 160, in main
    repository.save(
    ~~~~~~~~~~~~~~~^
        entry
        ^^^^^
    )
    ^
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\src\stockmind\infrastructure\history\fundamental_data_repository.py", line 75, in save
    cursor.execute(
    ~~~~~~~~~~~~~~^
        """
        ^^^
    ...<33 lines>...
        )
        ^
    )
    ^
sqlite3.OperationalError: table fundamental_data has no column named current_price
