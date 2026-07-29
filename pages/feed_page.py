import allure
from selenium.webdriver.support import expected_conditions as EC

from data.test_data import FEED_URL
from locators.feed_page_locators import (
    FEED_IN_WORK_LIST,
    FEED_MODAL_ORDER_NUMBER,
    FEED_NUMBER,
    FEED_ORDER_LINK,
)
from pages.base_page import BasePage


class FeedPage(BasePage):
    """Page Object страницы 'Лента заказов'."""

    def __init__(self, driver):
        super().__init__(driver, FEED_URL)

    @allure.step("Дождаться загрузки ленты заказов")
    def wait_for_feed_loaded(self):
        """Ожидает появления хотя бы одного заказа в ленте."""
        self.wait.until(EC.visibility_of_element_located(FEED_ORDER_LINK))

    @allure.step("Клик по заказу в ленте")
    def click_first_order(self):
        """Кликает по первому заказу в ленте для открытия модального окна."""
        self.click(FEED_ORDER_LINK)

    @allure.step("Проверить, что открыто модальное окно с деталями заказа")
    def is_order_modal_open(self):
        """Возвращает True, если модальное окно заказа отображается."""
        return self.is_element_visible(FEED_MODAL_ORDER_NUMBER)

    @allure.step("Получить номер заказа из модального окна")
    def get_modal_order_number(self):
        """Возвращает текст номера заказа из модального окна."""
        return self.get_text(FEED_MODAL_ORDER_NUMBER)

    @allure.step("Получить номер первого заказа в ленте")
    def get_first_feed_order_number(self):
        """Возвращает номер первого заказа из ленты (первая строка текста ссылки)."""
        return self.get_text(FEED_ORDER_LINK).split("\n")[0]

    @allure.step("Получить значение счётчика 'Выполнено за всё время'")
    def get_total_completed_count(self):
        """Ожидает загрузки счётчиков и возвращает значение 'Выполнено за всё время'."""
        self.wait.until(EC.visibility_of_all_elements_located(FEED_NUMBER))
        elements = self.find_elements(FEED_NUMBER)
        return elements[0].text if elements else "0"

    @allure.step("Получить значение счётчика 'Выполнено за сегодня'")
    def get_today_completed_count(self):
        """Ожидает загрузки счётчиков и возвращает значение 'Выполнено за сегодня'."""
        self.wait.until(EC.visibility_of_all_elements_located(FEED_NUMBER))
        elements = self.find_elements(FEED_NUMBER)
        return elements[1].text if len(elements) > 1 else "0"

    @allure.step("Получить список номеров в разделе 'В работе'")
    def get_in_work_orders(self):
        """Ожидает загрузки списка 'В работе' и возвращает тексты заказов."""
        self.wait.until(EC.visibility_of_all_elements_located(FEED_IN_WORK_LIST))
        items = self.find_elements(FEED_IN_WORK_LIST)
        return [item.text for item in items]

    @allure.step("Проверить, что заказ отображается в 'В работе'")
    def is_order_in_work(self, order_number):
        """Проверяет, содержится ли номер заказа в списке 'В работе'."""
        in_work = self.get_in_work_orders()
        return any(order_number in num for num in in_work)

    @allure.step("Получить список номеров заказов из ленты")
    def get_feed_order_numbers(self):
        """Ожидает загрузки ленты и возвращает список номеров заказов (#XXXXX)."""
        self.wait_for_feed_loaded()
        links = self.find_elements(FEED_ORDER_LINK)
        numbers = []
        for link in links:
            text = link.text.split("\n")[0]
            if text.startswith("#"):
                numbers.append(text)
        return numbers
