from datetime import datetime

from stockmind.domain.entities.stock import Stock

from stockmind.domain.enums.signal_type import (
    SignalType
)

from stockmind.domain.value_objects.signal_decision import (
    SignalDecision
)

stock = Stock(
    symbol="NVDA",
    name="NVIDIA"
)

signal = SignalDecision(
    symbol="NVDA",
    signal=SignalType.BUY,
    score=84.0,
    confidence=0.88,
    created_at=datetime.now()
)

print(stock)
print(signal)
