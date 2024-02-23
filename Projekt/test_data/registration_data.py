from faker import Faker


class AccountData:
    def __init__(self):
        fake = Faker("pl_PL")
        self.registration_email = fake.email()
        self.registration_password = fake.password(13)
