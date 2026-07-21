from selenium.webdriver.common.by import By

MAIN_HEADER = (By.CSS_SELECTOR, ".AppHeader_header__link__3D_hX")
LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
CONSTRUCTOR_LINK = (By.XPATH, "//a[.//p[contains(text(), 'Конструктор')]]")
ORDER_FEED_LINK = (By.XPATH, "//a[.//p[contains(text(), 'Лента Заказов')]]")
PERSONAL_ACCOUNT_LINK = (By.XPATH, "//a[.//p[contains(text(), 'Личный Кабинет')]]")

INGREDIENT_CARD = (By.CSS_SELECTOR, "a[class*='BurgerIngredient_ingredient']")
CONSTRUCTOR_BASKET = (By.CSS_SELECTOR, "[class*='BurgerConstructor_basket__29Cd7']")
COUNTER_NUMBER = (By.CSS_SELECTOR, "[class*='counter_counter__num']")
MODAL_OVERLAY = (By.CSS_SELECTOR, "[class*='Modal_modal_overlay']")
MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "button[class*='Modal_modal__close']")
MODAL_INGREDIENT_TITLE = (By.CSS_SELECTOR, "h2[class*='Modal_modal__title_modified']")
ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
