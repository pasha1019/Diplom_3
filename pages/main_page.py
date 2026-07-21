import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from data.test_data import MAIN_PAGE_URL
from locators.main_page_locators import (
    CONSTRUCTOR_BASKET,
    CONSTRUCTOR_LINK,
    COUNTER_NUMBER,
    INGREDIENT_CARD,
    LOGIN_BUTTON,
    MODAL_CLOSE_BUTTON,
    MODAL_INGREDIENT_TITLE,
    ORDER_BUTTON,
    ORDER_FEED_LINK,
    PERSONAL_ACCOUNT_LINK,
)
from pages.base_page import BasePage


class MainPage(BasePage):
    """Page Object главной страницы — конструктор бургеров."""

    def __init__(self, driver):
        super().__init__(driver, MAIN_PAGE_URL)

    @allure.step("Клик по кнопке 'Войти в аккаунт'")
    def click_login_button(self):
        """Кликает по кнопке 'Войти в аккаунт' на главной странице."""
        self.click(LOGIN_BUTTON)

    @allure.step("Проверить, что открыта главная страница")
    def is_main_page(self):
        """Возвращает True, если текущий URL совпадает с главной страницей."""
        return self.get_current_url() == MAIN_PAGE_URL

    @allure.step("Клик по 'Конструктор'")
    def click_constructor(self):
        """Кликает по ссылке 'Конструктор' в навигации."""
        self.click(CONSTRUCTOR_LINK)

    @allure.step("Клик по 'Лента Заказов'")
    def click_order_feed(self):
        """Кликает по ссылке 'Лента Заказов' в навигации."""
        self.click(ORDER_FEED_LINK)

    @allure.step("Клик по 'Личный Кабинет'")
    def click_personal_account(self):
        """Кликает по ссылке 'Личный кабинет' в навигации."""
        self.click(PERSONAL_ACCOUNT_LINK)

    @allure.step("Клик по ингредиенту")
    def click_ingredient(self):
        """Кликает по карточке ингредиента для открытия модального окна."""
        self.click(INGREDIENT_CARD)

    @allure.step("Проверить, что открыто модальное окно с деталями ингредиента")
    def is_ingredient_modal_open(self):
        """Возвращает True, если модальное окно ингредиента отображается."""
        return self.is_element_visible(MODAL_INGREDIENT_TITLE)

    @allure.step("Закрыть модальное окно по крестику")
    def close_modal(self):
        """Кликает по крестику для закрытия модального окна."""
        self.click(MODAL_CLOSE_BUTTON)

    @allure.step("Проверить, что модальное окно закрыто")
    def is_modal_closed(self):
        """Ожидает закрытия модального окна и возвращает True, если оно не отображается."""
        self.wait_for_element_not_visible(MODAL_INGREDIENT_TITLE)
        return True

    @allure.step("Перетащить ингредиент в конструктор")
    def drag_ingredient_to_constructor(self):
        """Drag-and-drop ингредиента из каталога в конструктор (корзину)."""
        source = self.wait.until(EC.element_to_be_clickable(INGREDIENT_CARD))
        target = self.wait.until(EC.visibility_of_element_located(CONSTRUCTOR_BASKET))
        ActionChains(self.driver).drag_and_drop(source, target).perform()

    @allure.step("Получить значение счётчика")
    def get_counter_value(self):
        """Ожидает появления счётчика и возвращает его текущее значение."""
        self.wait.until(EC.visibility_of_element_located(COUNTER_NUMBER))
        return self.get_text(COUNTER_NUMBER)

    @allure.step("Клик по кнопке 'Оформить заказ'")
    def click_order_button(self):
        """Кликает по кнопке 'Оформить заказ'."""
        self.click(ORDER_BUTTON)
