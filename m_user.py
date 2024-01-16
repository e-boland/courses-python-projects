"""Module to generate random users"""

import faker
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
logging.basicConfig(filename=BASE_DIR / 'm_user.log', level=logging.INFO)

fake = faker.Faker()


def get_user():
    """ Generate a single user

    Returns:
        str: user
    """
    logging.info("Generating a user.")
    return f"{fake.first_name()} {fake.last_name()}"


def get_users(n: int):
    """ Generate a list of users

    Args:
        n (): int: number of users to generate

    Returns: list[str]: users

    """
    logging.info(f"Generating a liste of {n} users.")
    return [get_user() for _ in range(n)]


if __name__ == "__main__":
    user = get_users(5)
    print(user)
