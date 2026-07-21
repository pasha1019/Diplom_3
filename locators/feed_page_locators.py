from selenium.webdriver.common.by import By

FEED_ORDER_LINK = (By.CSS_SELECTOR, "[class*='OrderFeed'] a")
FEED_NUMBER = (By.CSS_SELECTOR, "[class*='OrderFeed_number']")
FEED_STATUS_BOX = (By.CSS_SELECTOR, "[class*='OrderFeed_orderStatusBox']")
FEED_IN_WORK_LIST = (By.CSS_SELECTOR, "[class*='OrderFeed_orderStatusBox'] li")
FEED_MODAL_ORDER_NUMBER = (By.CSS_SELECTOR, "[class*='Modal'] p[class*='text_type_digits-default']")
FEED_MODAL_ORDER_STATUS = (By.XPATH, "//div[contains(@class,'Modal')]//p[contains(text(),'Выполнен')]")
FEED_MODAL_INGREDIENT_NAME = (By.CSS_SELECTOR, "[class*='Modal'] p[class*='text_type_main-default']")
