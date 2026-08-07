from stockmind.infrastructure.profiles.profile_repository import (
    ProfileRepository
)


def main():

    repository = ProfileRepository()

    for profile in repository.get_all():

        print("\n=== PROFILE ===")
        print(profile)


if __name__ == "__main__":
    main()
