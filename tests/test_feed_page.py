import allure

from data.api_client import register_user
from data.test_data import generate_email, generate_name, generate_password
from pages.feed_page import FeedPage


@allure.epic("Лента заказов")
class TestFeedPage:
    """Тесты раздела 'Лента заказов'."""

    @allure.feature("Детали заказа")
    @allure.story("Клик по заказу открывает модальное окно")
    @allure.title("Клик по заказу в ленте открывает модальное окно с деталями")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("feed")
    def test_order_click_opens_modal(self, driver):
        """Проверяет открытие модального окна с деталями при клике на заказ."""
        feed_page = FeedPage(driver)
        feed_page.open()
        feed_page.wait_for_feed_loaded()

        feed_page.click_first_order()
        assert feed_page.is_order_modal_open()

    @allure.feature("Лента заказов")
    @allure.story("Заказы пользователя отображаются в ленте")
    @allure.title("Заказы пользователя из 'История заказов' отображаются на 'Лента заказов'")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("feed")
    def test_user_orders_appear_in_feed(self, driver, order_created):
        """Проверяет, что созданный заказ отображается в ленте заказов."""
        feed_page = FeedPage(driver)
        feed_page.open()

        feed_numbers = feed_page.get_feed_order_numbers()
        assert len(feed_numbers) > 0

    @allure.feature("Счётчики")
    @allure.story("Счётчик 'Выполнено за всё время'")
    @allure.title("При создании заказа счётчик 'Выполнено за всё время' увеличивается")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("feed")
    def test_total_counter_increases(self, driver):
        """Проверяет увеличение счётчика 'Выполнено за всё время' после создания заказа."""
        from pages.login_page import LoginPage
        from pages.main_page import MainPage

        feed_page = FeedPage(driver)
        feed_page.open()
        total_before = feed_page.get_total_completed_count()

        email = generate_email()
        password = generate_password()
        name = generate_name()

        with allure.step("Зарегистрировать пользователя через API"):
            register_user(email, password, name)

        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_email(email)
        login_page.enter_password(password)
        login_page.click_submit()
        login_page.wait_for_url_not_contains("/login")

        main_page = MainPage(driver)
        main_page.open()
        main_page.drag_ingredient_to_constructor()
        main_page.get_counter_value()
        main_page.click_order_button()

        feed_page.open()
        total_after = feed_page.get_total_completed_count()

        assert int(total_after) > int(total_before)

    @allure.feature("Счётчики")
    @allure.story("Счётчик 'Выполнено за сегодня'")
    @allure.title("При создании заказа счётчик 'Выполнено за сегодня' увеличивается")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("feed")
    def test_today_counter_increases(self, driver):
        """Проверяет увеличение счётчика 'Выполнено за сегодня' после создания заказа."""
        from pages.login_page import LoginPage
        from pages.main_page import MainPage

        feed_page = FeedPage(driver)
        feed_page.open()
        today_before = feed_page.get_today_completed_count()

        email = generate_email()
        password = generate_password()
        name = generate_name()

        with allure.step("Зарегистрировать пользователя через API"):
            register_user(email, password, name)

        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_email(email)
        login_page.enter_password(password)
        login_page.click_submit()
        login_page.wait_for_url_not_contains("/login")

        main_page = MainPage(driver)
        main_page.open()
        main_page.drag_ingredient_to_constructor()
        main_page.get_counter_value()
        main_page.click_order_button()

        feed_page.open()
        today_after = feed_page.get_today_completed_count()

        assert int(today_after) > int(today_before)

    @allure.feature("В работе")
    @allure.story("Номер заказа появляется в 'В работе'")
    @allure.title("После оформления заказа его номер появляется в разделе 'В работе'")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("feed")
    def test_order_appears_in_work(self, driver, order_created):
        """Проверяет, что номер заказа появляется в разделе 'В работе'."""
        feed_page = FeedPage(driver)
        feed_page.open()

        in_work = feed_page.get_in_work_orders()
        assert len(in_work) > 0
