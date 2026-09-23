from dataclasses import dataclass

from stockmind.domain.rules.base_rule import ( BaseRule )

@dataclass(frozen=True)
class RuleSet:
    name: str
    
    rules: list[BaseRule]
