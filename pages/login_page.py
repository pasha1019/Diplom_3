import allure

from data.test_data import LOGIN_URL
from locators.login_page_locators import (
    EMAIL_INPUT,
    HEADING,
    PASSWORD_INPUT,
    RECOVERY_LINK,
    REGISTER_LINK,
    SUBMIT_BUTTON,
)
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page Object страницы входа в аккаунт."""

    def __init__(self, driver):
        super().__init__(driver, LOGIN_URL)

    @allure.step("Ввести email '{email}'")
    def enter_email(self, email):
        """Вводит email в поле ввода."""
        self.send_keys(EMAIL_INPUT, email)

    @allure.step("Ввести пароль")
    def enter_password(self, password):
        """Вводит пароль в поле ввода."""
        self.send_keys(PASSWORD_INPUT, password)

    @allure.step("Клик по кнопке 'Войти'")
    def click_submit(self):
        """Кликает по кнопке 'Войти' для отправки формы."""
        self.click(SUBMIT_BUTTON)

    @allure.step("Клик по 'Зарегистрироваться'")
    def click_register(self):
        """Кликает по ссылке 'Зарегистрироваться' для перехода на страницу регистрации."""
        self.click(REGISTER_LINK)

    @allure.step("Клик по 'Восстановить пароль'")
    def click_recovery(self):
        """Кликает по ссылке 'Забыли пароль?' для перехода на страницу восстановления."""
        self.click(RECOVERY_LINK)

    @allure.step("Проверить заголовок страницы")
    def get_heading_text(self):
        """Возвращает текст заголовка страницы."""
        return self.get_text(HEADING)

    @allure.step("Проверить, что открыта страница логина")
    def is_login_page(self):
        """Возвращает True, если текущий URL совпадает со страницей входа."""
        return self.get_current_url() == LOGIN_URL
