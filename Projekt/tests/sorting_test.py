import time
from selenium.webdriver.support.select import Select
from Projekt.tests.base_test import BaseTest
from Projekt.utils.locators import SortLocators
from selenium.webdriver import ActionChains


class SortingTest(BaseTest):
    def setUp(self):
        super().setUp()

    def screenshot(self):
        super().screenshot()

    """
        Test checking sorting 
    """

    def test_checking_sorting_by(self):
        # 1. Checking whether the Hoover is visible when you hover the mouse over it
        element_menu = self.driver.find_element(*SortLocators.MENU_ITEM)
        action = ActionChains(self.driver)
        action.move_to_element(element_menu).perform()
        self.screenshot()
        # 2. Chose from menu - "Most wanted"
        self.driver.find_element(*SortLocators.MENU_ITEM).click()
        # 3. Click an element to choose sorting
        form = self.driver.find_element(*SortLocators.FORM)
        form.click()
        # 4.Taking a screenshot
        self.screenshot()
        # 5. Select sorting by popularity
        select = Select(self.driver.find_element(*SortLocators.ORDER_BY))
        select.select_by_value('popularity')
        # 6. Checking expected effects using assertions
        sort_popularity = self.driver.find_element(*SortLocators.OPTION_POPULARITY)
        self.assertEqual("Sort by popularity", sort_popularity.text)
        print(sort_popularity.text)
        time.sleep(3)
        # 7.Taking a screenshot
        self.screenshot()
        # 8. Select sorting by newness
        select = Select(self.driver.find_element(*SortLocators.ORDER_BY))
        select.select_by_value('date')
        time.sleep(3)
        # 9.Taking a screenshot
        self.screenshot()
        # 10. Checking expected effects using assertions
        sort_newness = self.driver.find_element(*SortLocators.OPTION_NEWNESS)
        self.assertEqual("Sort by newness", sort_newness.text)
        print(sort_newness.text)
        # 11. Select sorting by average rating
        select = Select(self.driver.find_element(*SortLocators.ORDER_BY))
        select.select_by_value('rating')
        time.sleep(3)
        # 12.Taking a screenshot
        self.screenshot()
        # 13. Checking expected effects using assertions
        sort_average = self.driver.find_element(*SortLocators.OPTION_AVERAGE)
        self.assertEqual("Sort by newness", sort_average.text)
        print(sort_average.text)
