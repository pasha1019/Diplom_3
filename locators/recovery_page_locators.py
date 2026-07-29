from selenium.webdriver.common.by import By

HEADING = (By.CSS_SELECTOR, "h2")
EMAIL_INPUT = (By.CSS_SELECTOR, "input[type='text']")
SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Восстановить')]")
LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")

PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='Введите новый пароль']")
PASSWORD_CONTAINER = (By.CSS_SELECTOR, ".input_type_password")
PASSWORD_ICON = (By.CSS_SELECTOR, ".input__icon.input__icon-action")
CODE_INPUT = (By.CSS_SELECTOR, "input[name='name']")
SAVE_BUTTON = (By.XPATH, "//button[contains(text(), 'Сохранить')]")
ACTIVE_PASSWORD_CONTAINER = (By.CSS_SELECTOR, ".input_status_active")
