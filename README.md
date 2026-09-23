(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> python tests/test_historical_outcomes.py                                            
F...F.
======================================================================
FAIL: test_below_target (__main__.HistoricalOutcomeTest.test_below_target)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\tests\test_historical_outcomes.py", line 55, in test_below_target
    self.assertEqual(result.outcome, HistoricalOutcome.BELOW_TARGET)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: <HistoricalOutcome.FLAT: 'FLAT'> != <HistoricalOutcome.BELOW_TARGET: 'BELOW_TARGET'>

======================================================================
FAIL: test_negative (__main__.HistoricalOutcomeTest.test_negative)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\tests\test_historical_outcomes.py", line 71, in test_negative
    self.assertEqual(result.outcome, HistoricalOutcome.NEGATIVE)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: <HistoricalOutcome.FLAT: 'FLAT'> != <HistoricalOutcome.NEGATIVE: 'NEGATIVE'>

----------------------------------------------------------------------
Ran 6 tests in 0.020s

FAILED (failures=2)

(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> python scripts/test_historical_success_engine.py

==============================
PROFILE: CONSERVATIVE
==============================
Setups:            24
Complete:          24
Target hit:        17
Below target:      2
Flat:              1
Negative:          4
Incomplete:        0
Target-hit rate:   70.83%
Below-target rate: 8.33%
Flat rate:         4.17%
Negative rate:     16.67%
Sample quality:    MEDIUM

==============================
PROFILE: BALANCED
==============================
Setups:            57
Complete:          57
Target hit:        43
Below target:      4
Flat:              1
Negative:          9
Incomplete:        0
Target-hit rate:   75.44%
Below-target rate: 7.02%
Flat rate:         1.75%
Negative rate:     15.79%
Sample quality:    HIGH

==============================
PROFILE: AGGRESSIVE
==============================
Setups:            125
Complete:          125
Target hit:        98
Below target:      7
Flat:              3
Negative:          17
Incomplete:        0
Target-hit rate:   78.40%
Below-target rate: 5.60%
Flat rate:         2.40%
Negative rate:     13.60%
Sample quality:    HIGH




