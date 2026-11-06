(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> python -m unittest tests.test_exit_research_validation tests.test_exit_strategy_research tests.test_portfolio_intelligence
>> 
..EE.
======================================================================
ERROR: test_baseline_exits_when_target_is_reached (tests.test_exit_strategy_research.ExitSimulationTest.test_baseline_exits_when_target_is_reached)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\tests\test_exit_strategy_research.py", line 9, in test_baseline_exits_when_target_is_reached
    result=ExitSimulationUseCase().simulate(period,prices,[],ExitStrategy('BASELINE'))
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\src\stockmind\application\exit\exit_simulation_use_case.py", line 49, in simulate
    if point.high_price is not None else close
       ^^^^^^^^^^^^^^^^
AttributeError: 'types.SimpleNamespace' object has no attribute 'high_price'

======================================================================
ERROR: test_stop_loss_can_exit_before_time_limit (tests.test_exit_strategy_research.ExitSimulationTest.test_stop_loss_can_exit_before_time_limit)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\tests\test_exit_strategy_research.py", line 14, in test_stop_loss_can_exit_before_time_limit
    result=ExitSimulationUseCase().simulate(period,prices,[],ExitStrategy('STOP',stop_loss_pct=.05))
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\src\stockmind\application\exit\exit_simulation_use_case.py", line 49, in simulate
    if point.high_price is not None else close
       ^^^^^^^^^^^^^^^^
AttributeError: 'types.SimpleNamespace' object has no attribute 'high_price'

----------------------------------------------------------------------
Ran 5 tests in 0.005s

FAILED (errors=2)(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> python -m unittest tests.test_portfolio_lots tests.test_portfolio_foundation
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
