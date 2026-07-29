import requests

from data.test_data import BASE_URL

API_REGISTER_URL = f"{BASE_URL}/api/auth/register"
API_LOGIN_URL = f"{BASE_URL}/api/auth/login"
API_USER_URL = f"{BASE_URL}/api/auth/user"


def register_user(email: str, password: str, name: str) -> dict:
    """Регистрирует пользователя через API. Возвращает ответ сервера."""
    payload = {"email": email, "password": password, "name": name}
    response = requests.post(API_REGISTER_URL, json=payload)
    return response.json()


def login_user(email: str, password: str) -> dict:
    """Логинит пользователя через API. Возвращает ответ с токенами."""
    payload = {"email": email, "password": password}
    response = requests.post(API_LOGIN_URL, json=payload)
    return response.json()


def delete_user(access_token: str) -> dict:
    """Удаляет пользователя через API по токену авторизации."""
    headers = {"Authorization": access_token}
    response = requests.delete(API_USER_URL, headers=headers)
    return response.json()
