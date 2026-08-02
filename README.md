from stockmind.infrastructure.rules.rule_set_repository import (
    RuleSetRepository
)


def main():

    repository = RuleSetRepository()

    mean_reversion = repository.get_by_name(
        "mean_reversion"
    )

    trend_following = repository.get_by_name(
        "trend_following"
    )

    print("\n=== MEAN REVERSION RULE SET ===")
    print(mean_reversion)

    print("\nRules:")

    for rule in mean_reversion.rules:
        print(rule.name)

    print("\n=== TREND FOLLOWING RULE SET ===")
    print(trend_following)

    print("\nRules:")

    for rule in trend_following.rules:
        print(rule.name)

    print("\n=== ALL RULE SETS ===")

    for rule_set in repository.get_all():
        print(rule_set.name)


if __name__ == "__main__":
    main()
