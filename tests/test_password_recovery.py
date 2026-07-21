import allure
import pytest

from data.test_data import generate_email
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.recovery_page import RecoveryPage


@allure.epic("Восстановление пароля")
class TestPasswordRecovery:
    """Тесты восстановления пароля."""

    @allure.feature("Переход на страницу восстановления")
    @allure.story("Переход по кнопке 'Восстановить пароль'")
    @allure.title("Переход на страницу восстановления пароля по кнопке 'Восстановить пароль'")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("password_recovery")
    @pytest.mark.password_recovery
    def test_navigate_to_recovery_page(self, driver):
        """Проверяет переход на страницу восстановления пароля через 'Забыл пароль'."""
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_login_button()

        login_page = LoginPage(driver)
        login_page.click_recovery()

        recovery_page = RecoveryPage(driver)
        assert recovery_page.is_forgot_password_page()

    @allure.feature("Восстановление пароля")
    @allure.story("Ввод почты и клик 'Восстановить'")
    @allure.title("Ввод почты и клик по кнопке 'Восстановить' открывает страницу сброса пароля")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("password_recovery")
    @pytest.mark.password_recovery
    def test_enter_email_and_click_recovery(self, driver):
        """Проверяет переход на страницу сброса после ввода почты и клика 'Восстановить'."""
        recovery_page = RecoveryPage(driver)
        recovery_page.open()
        recovery_page.enter_email(generate_email())
        recovery_page.click_submit()
        assert recovery_page.is_reset_password_page()

    @allure.feature("Восстановление пароля")
    @allure.story("Показать/скрыть пароль")
    @allure.title("Кнопка показать/скрыть пароль делает поле активным и подсвечивает его")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("password_recovery")
    @pytest.mark.password_recovery
    def test_show_hide_password_highlights_field(self, driver):
        """Проверяет переключение типа поля и подсветку после клика по иконке пароля."""
        recovery_page = RecoveryPage(driver)
        recovery_page.open()
        recovery_page.enter_email(generate_email())
        recovery_page.click_submit()

        recovery_page.click_password_icon()

        assert recovery_page.get_password_input_type() == "text"
        assert recovery_page.is_password_field_active()
