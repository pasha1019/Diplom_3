from selenium.webdriver.common.by import By

ACCOUNT_TITLE = (By.XPATH, "//h1[contains(text(), 'Личный кабинет')]")
ORDER_HISTORY_LINK = (By.XPATH, "//a[contains(text(), 'История заказов')]")
LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")
