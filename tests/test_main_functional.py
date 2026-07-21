import allure

from data.test_data import MAIN_PAGE_URL
from pages.main_page import MainPage


@allure.epic("Основной функционал")
class TestMainFunctional:
    """Тесты основного функционала: навигация, ингредиенты, оформление заказа."""

    @allure.feature("Навигация")
    @allure.story("Переход по клику на 'Конструктор'")
    @allure.title("Переход по клику на 'Конструктор'")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("constructor")
    def test_navigate_to_constructor(self, driver):
        """Проверяет переход на главную по клику 'Конструктор' после перехода в 'Лента заказов'."""
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_order_feed()
        main_page.wait_for_url("/feed")

        main_page.click_constructor()
        main_page.wait_for_url_equals(MAIN_PAGE_URL)
        assert main_page.get_current_url() == MAIN_PAGE_URL

    @allure.feature("Навигация")
    @allure.story("Переход по клику на 'Лента заказов'")
    @allure.title("Переход по клику на 'Лента заказов'")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("feed")
    def test_navigate_to_order_feed(self, driver):
        """Проверяет переход на страницу 'Лента заказов' по клику."""
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_order_feed()
        main_page.wait_for_url("/feed")
        assert "/feed" in main_page.get_current_url()

    @allure.feature("Ингредиенты")
    @allure.story("Клик по ингредиенту открывает модальное окно")
    @allure.title("Клик по ингредиенту открывает модальное окно с деталями")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("ingredient")
    def test_ingredient_opens_modal(self, driver):
        """Проверяет, что клик по ингредиенту открывает модальное окно с деталями."""
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_ingredient()
        assert main_page.is_ingredient_modal_open()

    @allure.feature("Ингредиенты")
    @allure.story("Закрытие модального окна по крестику")
    @allure.title("Модальное окно закрывается кликом по крестику")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("ingredient")
    def test_modal_closes_by_close_button(self, driver):
        """Проверяет закрытие модального окна кликом по крестику."""
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_ingredient()
        main_page.close_modal()
        assert main_page.is_modal_closed()

    @allure.feature("Ингредиенты")
    @allure.story("Счётчик ингредиента")
    @allure.title("При добавлении ингредиента увеличивается счётчик")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("ingredient")
    def test_ingredient_counter_increases(self, driver):
        """Проверяет увеличение счётчика при drag-and-drop ингредиента в конструктор."""
        main_page = MainPage(driver)
        main_page.open()
        main_page.drag_ingredient_to_constructor()
        counter = main_page.get_counter_value()
        assert counter != "0"

    @allure.feature("Оформление заказа")
    @allure.story("Залогиненный пользователь может оформить заказ")
    @allure.title("Залогиненный пользователь может оформить заказ")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("order")
    def test_logged_in_user_can_place_order(self, driver, registered_user):
        """Проверяет, что залогиненный пользователь может оформить заказ."""
        main_page = MainPage(driver)
        main_page.open()
        main_page.drag_ingredient_to_constructor()
        main_page.get_counter_value()
        main_page.click_order_button()
        main_page.wait_for_url_equals(MAIN_PAGE_URL)
        assert main_page.get_current_url() == MAIN_PAGE_URL
