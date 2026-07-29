import allure

from data.test_data import FORGOT_PASSWORD_URL
from locators.recovery_page_locators import (
    ACTIVE_PASSWORD_CONTAINER,
    EMAIL_INPUT,
    HEADING,
    LOGIN_LINK,
    PASSWORD_CONTAINER,
    PASSWORD_ICON,
    PASSWORD_INPUT,
    SUBMIT_BUTTON,
)
from pages.base_page import BasePage


class RecoveryPage(BasePage):
    """Page Object страницы восстановления пароля."""

    def __init__(self, driver):
        super().__init__(driver, FORGOT_PASSWORD_URL)

    @allure.step("Ввести email '{email}'")
    def enter_email(self, email):
        """Вводит email в поле ввода на странице восстановления."""
        self.send_keys(EMAIL_INPUT, email)

    @allure.step("Клик по кнопке 'Восстановить'")
    def click_submit(self):
        """Кликает по кнопке 'Восстановить' для отправки формы."""
        self.click(SUBMIT_BUTTON)

    @allure.step("Клик по 'Войти'")
    def click_login(self):
        """Кликает по ссылке 'Войти' для перехода на страницу входа."""
        self.click(LOGIN_LINK)

    @allure.step("Проверить заголовок 'Восстановление пароля'")
    def get_heading_text(self):
        """Возвращает текст заголовка страницы."""
        return self.get_text(HEADING)

    @allure.step("Клик по иконке показа/скрытия пароля")
    def click_password_icon(self):
        """Кликает по иконке глаза для переключения видимости пароля."""
        self.click(PASSWORD_ICON)

    @allure.step("Проверить тип поля пароля")
    def get_password_input_type(self):
        """Возвращает текущий тип input (password/text) поля пароля."""
        return self.get_element_attribute(PASSWORD_INPUT, "type")

    @allure.step("Проверить класс контейнера пароля")
    def get_password_container_class(self):
        """Возвращает CSS-класс контейнера поля пароля."""
        return self.get_element_attribute(PASSWORD_CONTAINER, "class")

    @allure.step("Проверить, что поле пароля активно (подсвечено)")
    def is_password_field_active(self):
        """Возвращает True, если поле пароля подсвечено (имеет активный стиль)."""
        return self.is_element_visible(ACTIVE_PASSWORD_CONTAINER)

    @allure.step("Проверить, что открыта страница восстановления пароля")
    def is_forgot_password_page(self):
        """Возвращает True, если URL содержит '/forgot-password'."""
        return "/forgot-password" in self.get_current_url()

    @allure.step("Проверить, что открыта страница сброса пароля")
    def is_reset_password_page(self):
        """Ожидает и возвращает True, если URL содержит '/reset-password'."""
        self.wait_for_url_contains("/reset-password")
        return "/reset-password" in self.get_current_url()
