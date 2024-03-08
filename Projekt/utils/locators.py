from selenium.webdriver.common.by import By


class AccountLocators:
    # Registration locators
    ACCOUNT_LOCATOR = (By.CLASS_NAME, 'top-account')
    REGISTER_EMAIL = (By.ID, 'reg_email')
    REGISTER_PASSWORD = (By.ID, 'reg_password')
    REGISTER_BUTTON = (By.XPATH, '//input[@name="register"]')
    REGISTER_OUT_CLICK = (By.XPATH, '//label[@for="reg_password"]')
    STRONG_OF_PASSWORD = (By.XPATH, '//div[@aria-live="polite"]')
    LOGIN_EMAIL = (By.ID, 'username')
    LOGIN_PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'input[value=Login]')
    LOGIN_REMEMBER_ME = (By.ID, 'rememberme')


class SortLocators:
    # Sorting locators
    MENU_ITEM = (By.ID, 'menu-item-128')
    ORDER_BY = (By.CLASS_NAME, 'orderby')
    FORM = (By.CLASS_NAME, 'woocommerce-ordering')
    OPTION_POPULARITY = (By.CSS_SELECTOR, 'select.orderby>option:nth-child(2)')
    OPTION_NEWNESS = (By.CSS_SELECTOR, 'select.orderby>option:nth-child(4)')
    OPTION_AVERAGE = (By.CSS_SELECTOR, 'select.orderby>option:nth-child(3)')