import allure

from data.test_data import REGISTER_URL
from locators.register_page_locators import (
    EMAIL_INPUT,
    NAME_INPUT,
    PASSWORD_INPUT,
    REGISTER_BUTTON,
)
from pages.base_page import BasePage


class RegisterPage(BasePage):
    """Page Object страницы регистрации нового пользователя."""

    def __init__(self, driver):
        super().__init__(driver, REGISTER_URL)

    @allure.step("Ввести имя '{name}'")
    def enter_name(self, name):
        """Вводит имя в поле ввода."""
        self.send_keys(NAME_INPUT, name)

    @allure.step("Ввести email '{email}'")
    def enter_email(self, email):
        """Вводит email в поле ввода."""
        self.send_keys(EMAIL_INPUT, email)

    @allure.step("Ввести пароль")
    def enter_password(self, password):
        """Вводит пароль в поле ввода."""
        self.send_keys(PASSWORD_INPUT, password)

    @allure.step("Клик по кнопке 'Зарегистрироваться'")
    def click_register(self):
        """Кликает по кнопке 'Зарегистрироваться' для отправки формы."""
        self.click(REGISTER_BUTTON)

    @allure.step("Проверить, что открыта страница входа (после регистрации)")
    def is_redirected_to_login(self):
        """Ожидает и возвращает True, если произошёл редирект на страницу входа."""
        self.wait_for_url_contains("/login")
        return "/login" in self.get_current_url()
