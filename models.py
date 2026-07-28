# scripts/test_marketdata.py

from stockmind.infrastructure.market_data.mock_provider import (
    MockProvider
)

provider = MockProvider()

data = provider.fetch_history(
    "NVDA"
)

for item in data:
    print(item)
