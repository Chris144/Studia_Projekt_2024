from selenium.webdriver.common.by import By


class AccountLocators:
    # Registration locators
    ACCOUNT_LOCATOR = (By.CLASS_NAME, 'top-account')
    REGISTER_EMAIL = (By.ID, 'reg_email')
    REGISTER_PASSWORD = (By.ID, 'reg_password')
    REGISTER_BUTTON = (By.XPATH, '//input[@name="register"]')
    REGISTER_OUT_CLICK = (By.XPATH, '//label[@for="reg_password"]')
    STRONG_OF_PASSWORD = (By.XPATH, '//div[@aria-live="polite"]')

