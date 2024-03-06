from selenium.webdriver.common.by import By

from Projekt.tests.base_test import BaseTest
from Projekt.utils.locators import AccountLocators
from Projekt.test_data.registration_data import AccountData


class LoginTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.test_data = AccountData()

    def screenshot(self):
        super().screenshot()

    """
    Test checking user login - positive
    """

    def test_login_positive(self):
        # 1. CLick the button to go to the login page
        element_to_account = self.driver.find_element(*AccountLocators.ACCOUNT_LOCATOR)
        element_to_account.click()
        # 2. Enter the correct email
        self.driver.find_element(*AccountLocators.LOGIN_EMAIL).send_keys('jaimechapman@example.net')
        # 3. Enter the correct password
        self.driver.find_element(*AccountLocators.LOGIN_PASSWORD).send_keys('Qwerty144[])')
        self.screenshot()
        # 4. Select checkbox "Remember me"
        checkbox_remember_me = self.driver.find_element(*AccountLocators.LOGIN_REMEMBER_ME)
        checkbox_remember_me.click()
        # 5. Checking if checkbox is selected
        checkbox_remember_me.is_selected()
        print(checkbox_remember_me.is_selected())
        # 6. Click Login button
        self.driver.find_element(*AccountLocators.LOGIN_BUTTON).click()
        self.screenshot()

    """
        Test checking user login - empty field email
    """

    def test_login_no_email(self):
        # 1. CLick the button to go to the login page
        element_to_account = self.driver.find_element(*AccountLocators.ACCOUNT_LOCATOR)
        element_to_account.click()
        # 2. Do not provide an e-mail or username address
        self.driver.find_element(*AccountLocators.LOGIN_EMAIL).send_keys()
        # 3. Enter the correct password
        self.driver.find_element(*AccountLocators.LOGIN_PASSWORD).send_keys(self.test_data.registration_password)
        # 4. Click the "Login" button
        self.screenshot()
        self.driver.find_element(*AccountLocators.LOGIN_BUTTON).click()
        # 5. Taking a screenshot
        self.screenshot()
        # 6. Checking the expected effect
        error_mail = self.driver.find_element(By.CLASS_NAME, 'woocommerce-error')
        self.assertEqual("Error: Username is required.", error_mail.text)
        print(error_mail.text)

    """
           Test checking user login - empty field password
    """

    def test_login_no_password(self):
        # 1. CLick the button to go to the login page
        element_to_account = self.driver.find_element(*AccountLocators.ACCOUNT_LOCATOR)
        element_to_account.click()
        # 2. Enter the correct email
        self.driver.find_element(*AccountLocators.LOGIN_EMAIL).send_keys('jaimechapman@example.net')
        # 3.  Do not provide a password
        self.driver.find_element(*AccountLocators.LOGIN_PASSWORD).send_keys()
        # 4. Click the "Login" button
        self.screenshot()
        self.driver.find_element(*AccountLocators.LOGIN_BUTTON).click()
        # 5. Taking a screenshot
        self.screenshot()
        # 6. Checking the expected effect
        error_password = self.driver.find_element(By.CLASS_NAME, 'woocommerce-error')
        self.assertEqual("Error: The password field is empty.", error_password.text)
        print(error_password.text)

    """
        Test checking user login - user_not_registered - enter username
    """

    def test_login_username_not_registered_1(self):
        # 1. CLick the button to go to the login page
        element_to_account = self.driver.find_element(*AccountLocators.ACCOUNT_LOCATOR)
        element_to_account.click()
        # 2. Enter the username who is not registered
        self.driver.find_element(*AccountLocators.LOGIN_EMAIL).send_keys('waldemar231')
        # 3. Enter the password user who is not registered
        self.driver.find_element(*AccountLocators.LOGIN_PASSWORD).send_keys(self.test_data.registration_password)
        # 4. Taking a first screenshot
        self.screenshot()
        # 5. Click the "Login" button
        self.driver.find_element(*AccountLocators.LOGIN_BUTTON).click()
        # 5. Taking a second screenshot
        self.screenshot()
        # 6. Checking the expected effect
        error_no_registered = self.driver.find_element(By.CLASS_NAME, 'woocommerce-error')
        error_no_registered_username = self.driver.find_element(By.CSS_SELECTOR,
                                                                'ul.woocommerce-error>li>strong:nth-child(2)')
        self.assertEqual(
            f"Error: The username {error_no_registered_username.text} is not registered on this site."
            f" If you are unsure of your username, try your email address instead.",
            error_no_registered.text)
        print(error_no_registered.text)

    """
        Test checking user login - user_not_registered - enter email
    """

    def test_login_username_not_registered_2(self):
        # 1. CLick the button to go to the login page
        element_to_account = self.driver.find_element(*AccountLocators.ACCOUNT_LOCATOR)
        element_to_account.click()
        # 2. Enter the username who is not registered
        self.driver.find_element(*AccountLocators.LOGIN_EMAIL).send_keys(self.test_data.registration_email)
        # 3. Enter the password user who is not registered
        self.driver.find_element(*AccountLocators.LOGIN_PASSWORD).send_keys(self.test_data.registration_password)
        # 4. Taking a first screenshot
        self.screenshot()
        # 5. Click the "Login" button
        self.driver.find_element(*AccountLocators.LOGIN_BUTTON).click()
        # 5. Taking a second screenshot
        self.screenshot()
        # 6. Checking the expected effect
        error_no_registered = self.driver.find_element(By.CLASS_NAME, 'woocommerce-error')
        self.assertEqual("Error: A user could not be found with this email address.", error_no_registered.text)
        print(error_no_registered.text)

    def test_login_incorrect_password(self):
        # 1. CLick the button to go to the login page
        element_to_account = self.driver.find_element(*AccountLocators.ACCOUNT_LOCATOR)
        element_to_account.click()
        # 2. Enter the correct email
        self.driver.find_element(*AccountLocators.LOGIN_EMAIL).send_keys('jaimechapman@example.net')
        # 3. Enter the incorrect password
        self.driver.find_element(*AccountLocators.LOGIN_PASSWORD).send_keys(self.test_data.registration_password)
        # 4. Taking a first screenshot
        self.screenshot()
        # 5. Click the "Login" button
        self.driver.find_element(*AccountLocators.LOGIN_BUTTON).click()
        # 5. Taking a second screenshot
        self.screenshot()
        # 6. Checking the expected effect
        error_wrong_password = self.driver.find_element(By.CLASS_NAME, 'woocommerce-error')
        error_wrong_password_username = self.driver.find_element(By.CSS_SELECTOR,
                                                                 'ul.woocommerce-error>li>strong:nth-child(2)')
        self.assertEqual(
            f"Error: The password you entered for the username {error_wrong_password_username.text} is incorrect."
            f" Lost your password?", error_wrong_password.text)
        print(error_wrong_password.text)
