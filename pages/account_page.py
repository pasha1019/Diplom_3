import allure

from locators.account_page_locators import (
    LOGOUT_BUTTON,
    ORDER_HISTORY_LINK,
)
from pages.base_page import BasePage


class AccountPage(BasePage):
    """Page Object страницы личного кабинета."""

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Дождаться загрузки страницы личного кабинета")
    def wait_for_account_page(self):
        """Ожидает загрузки страницы профиля (/account/profile)."""
        self.wait_for_url_contains("/account/profile")

    @allure.step("Проверить, что открыта страница личного кабинета")
    def is_account_page(self):
        """Возвращает True, если URL содержит '/account/profile'."""
        return "/account/profile" in self.get_current_url()

    @allure.step("Проверить, что открыта страница истории заказов")
    def is_order_history_page(self):
        """Возвращает True, если URL содержит '/account/order-history'."""
        return "/account/order-history" in self.get_current_url()

    @allure.step("Клик по 'История заказов'")
    def click_order_history(self):
        """Кликает по ссылке 'История заказов' в личном кабинете."""
        self.click(ORDER_HISTORY_LINK)

    @allure.step("Клик по 'Выход'")
    def click_logout(self):
        """Кликает по кнопке 'Выход' для выхода из аккаунта."""
        self.click(LOGOUT_BUTTON)

    @allure.step("Проверить, что открыта страница входа (после выхода)")
    def is_redirected_to_login(self):
        """Ожидает и возвращает True, если произошёл редирект на страницу входа."""
        self.wait_for_url_contains("/login")
        return "/login" in self.get_current_url()
