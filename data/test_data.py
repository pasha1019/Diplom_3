from faker import Faker

fake = Faker()

BASE_URL = "https://qa-stellarburgers.education-services.ru"
LOGIN_URL = f"{BASE_URL}/login"
REGISTER_URL = f"{BASE_URL}/register"
FORGOT_PASSWORD_URL = f"{BASE_URL}/forgot-password"
RESET_PASSWORD_URL = f"{BASE_URL}/reset-password"
FEED_URL = f"{BASE_URL}/feed"
MAIN_PAGE_URL = BASE_URL + "/"

def generate_email():
    return fake.email()


def generate_password():
    return fake.password(length=12)


def generate_name():
    return fake.first_name()
