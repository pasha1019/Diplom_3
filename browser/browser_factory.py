import allure
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service


class BrowserFactory:
    """Фабрика создания WebDriver для Chrome и Firefox."""

    @staticmethod
    @allure.step("Создать WebDriver для браузера '{browser_name}'")
    def create_driver(browser_name: str) -> webdriver.Remote:
        """Создаёт WebDriver для указанного браузера (Chrome/Firefox) в headless-режиме."""
        if browser_name.lower() == "chrome":
            return BrowserFactory._create_chrome()
        elif browser_name.lower() == "firefox":
            return BrowserFactory._create_firefox()
        else:
            raise ValueError(f"Неподдерживаемый браузер: {browser_name}")

    @staticmethod
    def _create_chrome() -> webdriver.Chrome:
        """Создаёт headless Chrome с разрешением 1920x1080."""
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-blink-features=AutomationControlled")
        return webdriver.Chrome(options=options)

    @staticmethod
    def _create_firefox() -> webdriver.Firefox:
        """Создаёт headless Firefox с разрешением 1920x1080."""
        options = Options()
        options.add_argument("-headless")

        options.binary_location = "/usr/bin/firefox"

        options.add_argument("--width=1920")
        options.add_argument("--height=1080")

        options.set_preference("dom.webdriver.enabled", False)
        options.set_preference("useAutomationExtension", False)

        # Ускорение загрузки страниц
        options.page_load_strategy = "eager"

        # Блокировка шрифт и кеш для ускорения
        options.set_preference("font.system.whitelist", "")
        options.set_preference("browser.cache.disk.enable", False)
        options.set_preference("browser.cache.memory.enable", False)

        # Таймауты
        options.timeouts = {"pageLoad": 10000, "script": 5000}

        service = Service()
        return webdriver.Firefox(service=service, options=options)
