import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from tests.test import Test
from actions.login_action import LoginAction


class TestLogin(Test):
    def test_home_page_title(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        actual_title = self.driver.title

        expected_title = "Login | Salesforce"
        if actual_title == expected_title:
            assert True
        else:
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login_action = LoginAction(self.driver)
        self.login_page = self.login_action.page
        self.login_action.fill_username(username=self.username)
        self.login_action.fill_password(password=self.password)
        self.login_page.login_button().click()
        actual_title = self.driver.title

        """
        Upon successful login, the page title takes on one value and then changes to another after a
        few seconds.  To check the second value, we wait for the "Setup Home" element to load in the 
        left nav.
        """
        expected_initial_title = "Lightning Experience"
        expected_title_after_full_page_load = "Home | Salesforce"
        if actual_title == expected_initial_title:
            assert True
        else:
            assert False

        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, '//li[@aria-label="Setup Home"]')))
        actual_title = self.driver.title

        if actual_title == expected_title_after_full_page_load:
            assert True
        else:
            assert False
