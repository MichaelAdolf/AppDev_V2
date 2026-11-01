from dataclasses import dataclass

@dataclass(frozen=True)
class WatchlistEntry:
    symbol: str

    company_name: str

    active: bool

    created_at: str