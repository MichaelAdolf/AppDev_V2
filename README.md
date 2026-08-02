(.venv) PS D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform> python scripts/test_feature_engine.py
Traceback (most recent call last):
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\scripts\test_feature_engine.py", line 35, in <module>
    features = feature_engine.build( indicator_result )
  File "D:\Users\Michael\Dokumente\16_AppDev\stockmind-platform\src\stockmind\domain\features\feature_engine.py", line 22, in build
    return MarketFeatureSnapshot(
        symbol=result.symbol,
    ...<19 lines>...
        near_lower_bollinger=bollinger_position < 0.25
    )
TypeError: MarketFeatureSnapshot.__init__() got an unexpected keyword argument 'near_lower_bollinger'. Did you mean 'near_low_bollinger'?
