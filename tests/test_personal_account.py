import allure

from pages.account_page import AccountPage
from pages.main_page import MainPage


@allure.epic("Личный кабинет")
class TestPersonalAccount:
    """Тесты раздела 'Личный кабинет'."""

    @allure.feature("Переход в личный кабинет")
    @allure.story("Клик по кнопке 'Личный кабинет'")
    @allure.title("Переход в личный кабинет по кнопке 'Личный кабинет'")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("personal_account")
    def test_navigate_to_personal_account(self, driver, registered_user):
        """Проверяет переход в личный кабинет по клику на 'Личный кабинет'."""
        main_page = MainPage(driver)
        main_page.click_personal_account()

        account_page = AccountPage(driver)
        account_page.wait_for_account_page()
        assert account_page.is_account_page()

    @allure.feature("Личный кабинет")
    @allure.story("Переход в историю заказов")
    @allure.title("Переход в раздел 'История заказов'")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("personal_account")
    def test_navigate_to_order_history(self, driver, registered_user):
        """Проверяет переход в раздел 'История заказов'."""
        main_page = MainPage(driver)
        main_page.click_personal_account()

        account_page = AccountPage(driver)
        account_page.wait_for_account_page()
        account_page.click_order_history()
        assert account_page.is_order_history_page()

    @allure.feature("Личный кабинет")
    @allure.story("Выход из аккаунта")
    @allure.title("Выход из аккаунта")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("personal_account")
    def test_logout(self, driver, registered_user):
        """Проверяет выход из аккаунта по кнопке 'Выход'."""
        main_page = MainPage(driver)
        main_page.click_personal_account()

        account_page = AccountPage(driver)
        account_page.wait_for_account_page()
        account_page.click_logout()
        assert account_page.is_redirected_to_login()
