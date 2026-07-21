from selenium.webdriver.common.by import By

HEADING = (By.CSS_SELECTOR, "h2")
EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='name']")
PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='Пароль']")
SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
REGISTER_LINK = (By.XPATH, "//a[contains(text(), 'Зарегистрироваться')]")
RECOVERY_LINK = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")
