(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> python -m unittest tests.test_portfolio_lots tests.test_portfolio_foundation
.E
======================================================================
ERROR: test_position_can_be_added_and_fully_closed (tests.test_portfolio_foundation.PortfolioFoundationTest.test_position_can_be_added_and_fully_closed)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\tests\test_portfolio_foundation.py", line 31, in test_position_can_be_added_and_fully_closed
    position_id=position.id, sale_date="2026-10-31",
                ^^^^^^^^^^^
AttributeError: 'tuple' object has no attribute 'id'

----------------------------------------------------------------------
Ran 2 tests in 0.159s

FAILED (errors=1)
(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> python -m unittest tests.test_portfolio_foundation                          
>> 
E
======================================================================
ERROR: test_position_can_be_added_and_fully_closed (tests.test_portfolio_foundation.PortfolioFoundationTest.test_position_can_be_added_and_fully_closed)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\tests\test_portfolio_foundation.py", line 31, in test_position_can_be_added_and_fully_closed
    position_id=position.id, sale_date="2026-10-31",
                ^^^^^^^^^^^
AttributeError: 'tuple' object has no attribute 'id'

----------------------------------------------------------------------
Ran 1 test in 0.075s

FAILED (errors=1)
