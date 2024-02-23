import time

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from Projekt.tests.base_test import BaseTest
from Projekt.utils.locators import AccountLocators
from Projekt.test_data.registration_data import AccountData


class RegistrationTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.test_data = AccountData()

    def screenshot(self):
        super().screenshot()

    """
    Test checking user registration - positive
    """

    def test_registration_positive(self):
        # 1. Checking whether the Hoover is visible when you hover the mouse over it
        element_to_account = self.driver.find_element(*AccountLocators.ACCOUNT_LOCATOR)
        action = ActionChains(self.driver)
        action.move_to_element(element_to_account).perform()
        # 2. Use the button to go to the registration page
        element_to_account.click()
        # 3. Enter the correct email
        self.driver.find_element(*AccountLocators.REGISTER_EMAIL).send_keys(self.test_data.registration_email)
        # 4. Enter the correct password
        self.driver.find_element(*AccountLocators.REGISTER_PASSWORD).send_keys(self.test_data.registration_password)
        time.sleep(5)
        # 5 Click again in the anywhere for the Register button to activate
        self.driver.find_element(*AccountLocators.REGISTER_OUT_CLICK).click()
        # 6. Click the "Register" button
        self.driver.find_element(*AccountLocators.REGISTER_BUTTON).click()
        # 7. Taking a screenshot
        self.screenshot()

    """
        Test checking user registration - no email
    """

    def test_registration_no_email(self):
        # 1. CLick the button to go to the registration page
        element_to_account = self.driver.find_element(*AccountLocators.ACCOUNT_LOCATOR)
        element_to_account.click()
        # 2. Do not provide an e-mail address
        # 3. Enter the correct password
        self.driver.find_element(*AccountLocators.REGISTER_PASSWORD).send_keys(self.test_data.registration_password)
        # 5 Click again in the anywhere for the Register button to activate
        time.sleep(3)
        self.driver.find_element(*AccountLocators.REGISTER_OUT_CLICK).click()
        # 6. Click the "Register" button
        self.driver.find_element(*AccountLocators.REGISTER_BUTTON).click()
        # 7. Taking a screenshot
        self.screenshot()
        # 8. Checking the expected effect
        error_mail = self.driver.find_element(By.CLASS_NAME, 'woocommerce-error')
        self.assertEqual("Error: Please provide a valid email address.", error_mail.text)
        print(error_mail.text)

    """
        Test checking user registration - no password
    """

    def test_registration_no_password(self):
        # 1. Click the button to go to the registration page
        element_to_account = self.driver.find_element(*AccountLocators.ACCOUNT_LOCATOR)
        element_to_account.click()
        # 2. Enter the correct email
        self.driver.find_element(*AccountLocators.REGISTER_EMAIL).send_keys(self.test_data.registration_email)
        time.sleep(3)
        # 3. Do not provide a password
        # 4 Click again in the anywhere for the Register button to activate
        self.driver.find_element(*AccountLocators.REGISTER_OUT_CLICK).click()
        # 5. Click the "Register" button
        self.driver.find_element(*AccountLocators.REGISTER_BUTTON).click()
        # 7. Taking a screenshot
        self.screenshot()
        # 8. Checking the expected effect
        error_password = self.driver.find_element(By.CLASS_NAME, 'woocommerce-error')
        self.assertEqual("Error: Please enter an account password.", error_password.text)
        print(error_password.text)

    """
          A test checking if the button is active or not depending on strength password
          1. Very_Week_Password - Button register should be Disabled
          2. Week_Password - Button register should be Disabled
          3. Medium - Button register should be Enabled
          4. Strong - Button register should be Enabled
    """

    def test_registration_button_enabled_or_disabled(self):
        # 1. Click the button to go to the registration page
        element_to_account = self.driver.find_element(*AccountLocators.ACCOUNT_LOCATOR)
        element_to_account.click()
        # 2. Enter appropriate length password to check button
        self.driver.find_element(*AccountLocators.REGISTER_PASSWORD).send_keys('123')
        time.sleep(3)
        # 3. Click again in the anywhere for the Register button to activate
        self.driver.find_element(*AccountLocators.REGISTER_OUT_CLICK).click()
        # 4. Locating password strength information
        if self.driver.find_element(*AccountLocators.STRONG_OF_PASSWORD).text:
            # 5. Checking if the button is active or not - FALSE or TRUE
            self.driver.find_element(*AccountLocators.REGISTER_BUTTON).is_enabled()
            # 6. Printing whether the button is active or not
            print(self.driver.find_element(*AccountLocators.REGISTER_BUTTON).is_enabled())
        # 7. Taking a screenshot
        self.screenshot()
