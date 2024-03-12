import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException

from pages.login_page import LoginPage
from pages.app_launcher import AppLauncher
from pages.opportunities_page import OpportunitiesPage
from pages.global_search import GlobalSearch
from tests.test import Test


class TestOpportunity(Test):
    base_url = "https://efficiency-customization-c2-dev-ed.scratch.my.salesforce.com/"
    username = "test-g47godb2ia5t@example.com"
    password = "&9qNxuqiipgbu"

    def test_nav_to_opportunities(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login_page = LoginPage(self.driver)
        self.app_launcher = AppLauncher(self.driver)
        self.opportunities_page = OpportunitiesPage(self.driver)

        self.login_page.log_in(self.username, self.password)
        self.app_launcher.click_app_launcher_button()
        # Search for "oppo" in app launcher search bar to access the "Opportunities" listing page
        self.app_launcher.enter_and_click_search_term(search_term="oppo")
        # Verify the correct page was loaded by checking for the presence of the "New" button at the upper right
        try:
            self.driver.find_element(By.XPATH, self.opportunities_page.new_button)
            assert True
        except NoSuchElementException:
            assert False

    def test_create_and_update_new_opportunity(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login_page = LoginPage(self.driver)
        self.app_launcher = AppLauncher(self.driver)
        self.opportunities_page = OpportunitiesPage(self.driver)
        self.global_search = GlobalSearch(self.driver)

        self.login_page.log_in(self.username, self.password)
        self.driver.implicitly_wait(5)
        self.opportunities_page.nav_to_opportunities_page()
        self.opportunities_page.click_new_button()
        time.sleep(2)
        unique_name = self.opportunities_page.fill_required_fields()
        self.opportunities_page.click_save_button()
        time.sleep(5)
        # After creating new opportunity, check for the presence of the success alert at the top
        try:
            if self.driver.find_element(By.XPATH, self.opportunities_page.successful_opportunity_creation_message.format(unique_name)):
                assert True
        except InvalidSelectorException:
            assert False, "Failure: Creation of new opportunity failed"
        assert self.driver.find_element(By.XPATH, self.opportunities_page.opportunity_name).text == unique_name, "Failure: New opportunity name does not match expected name"
        self.global_search.click_search_bar()
        try:
            if self.global_search.enter_and_click_search_term(search_term=unique_name):
                assert True
        except NoSuchElementException:
            assert False, "Failure: Newly created opportunity not found in search results"
        time.sleep(3)
        self.opportunities_page.click_edit_button()
        time.sleep(2)
        new_stage_value = "Value Proposition"
        self.opportunities_page.select_stage_dropdown_value(new_stage_value)
        self.opportunities_page.click_save_button()
        time.sleep(3)
        self.driver.refresh()
        assert self.driver.find_element(By.XPATH,
                                        self.opportunities_page.opportunity_name).text == unique_name, "Failure: Actual page does not match expected opportunity detail page"
        self.driver.execute_script('window.scrollBy(0, 1000)')
        assert self.driver.find_element(By.XPATH, self.opportunities_page.stage_history_latest_stage).text == new_stage_value, "Failure: Stage field does not reflect new stage that was set"
