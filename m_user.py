import faker

fake = faker.Faker()


def get_user():
    return f"{fake.first_name()} {fake.last_name()}"


def get_users(n: int):
    return [get_user() for _ in range(n)]


if __name__ == "__main__":
    user = get_users(5)
    print(user)
