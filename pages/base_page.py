import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """Базовый класс Page Object — общие методы взаимодействия с элементами."""

    def __init__(self, driver, url=""):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """Открывает страницу по URL."""
        with allure.step(f"Открыть страницу {self.url}"):
            self.driver.get(self.url)
        return self

    def find_element(self, locator):
        """Ожидает и возвращает один элемент по локатору."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        """Возвращает список элементов по локатору."""
        return self.driver.find_elements(*locator)

    def click(self, locator):
        """Ожидает кликабельность и кликает по элементу."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return element

    def send_keys(self, locator, text):
        """Очищает поле и вводит текст."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)
        return element

    def get_current_url(self):
        """Возвращает текущий URL браузера."""
        return self.driver.current_url

    def get_element_attribute(self, locator, attribute):
        """Возвращает значение атрибута элемента."""
        return self.find_element(locator).get_attribute(attribute)

    def is_element_visible(self, locator, timeout=5):
        """Проверяет видимость элемента. Возвращает True/False."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def wait_for_element_not_visible(self, locator, timeout=10):
        """Ожидает, пока элемент станет невидимым."""
        WebDriverWait(self.driver, timeout).until_not(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_url(self, url_fragment, timeout=10):
        """Ожидает, пока URL будет содержать указанную подстроку."""
        WebDriverWait(self.driver, timeout).until(EC.url_contains(url_fragment))

    def wait_for_url_equals(self, expected_url, timeout=10):
        """Ожидает, пока URL точно совпадёт с ожидаемым."""
        WebDriverWait(self.driver, timeout).until(lambda d: d.current_url == expected_url)

    def get_text(self, locator):
        """Возвращает текст элемента."""
        return self.find_element(locator).text

    def wait_for_url_contains(self, url_fragment, timeout=10):
        """Ожидает, пока URL не будет содержать указанную подстроку."""
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(url_fragment)
        )

    def wait_for_url_not_contains(self, url_fragment, timeout=10):
        """Ожидает, пока URL перестанет содержать указанную подстроку."""
        WebDriverWait(self.driver, timeout).until_not(
            EC.url_contains(url_fragment)
        )
