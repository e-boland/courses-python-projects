"""Module to generate random users"""

import faker

fake = faker.Faker()


def get_user():
    """ Generate a single user

    Returns:
        str: user
    """
    return f"{fake.first_name()} {fake.last_name()}"


def get_users(n: int):
    """ Generate a list of users

    Args:
        n (): int: number of users to generate

    Returns: list[str]: users

    """
    return [get_user() for _ in range(n)]


if __name__ == "__main__":
    user = get_users(5)
    print(user)
