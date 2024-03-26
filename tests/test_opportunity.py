import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException
from pages.app_launcher import AppLauncher
from actions.login_action import LoginAction
from actions.app_launcher_action import AppLauncherAction
from actions.opportunity_action import OpportunityAction
from actions.global_search_action import GlobalSearchAction
from tests.test import Test


class TestOpportunity(Test):
    def test_nav_to_opportunity_listing_page(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login_action = LoginAction(self.driver)
        self.login_page = self.login_action.page
        self.app_launcher_action = AppLauncherAction(self.driver)
        self.app_launcher = AppLauncher(self.driver)
        self.opportunity_action = OpportunityAction(self.driver)
        self.opportunity_page = self.opportunity_action.page

        self.login_action.log_in(self.username, self.password)
        self.opportunity_action.nav_to_listing()
        # Verify the correct page was loaded by checking for the presence of the "New" button at the upper right
        try:
            if self.opportunity_page.new_button():
                assert True
        except NoSuchElementException:
            assert False, 'Failure: "New" button not found'

    def test_create_and_update_new_opportunity(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login_action = LoginAction(self.driver)
        self.login_page = self.login_action.page
        self.app_launcher = AppLauncher(self.driver)
        self.opportunity_action = OpportunityAction(self.driver)
        self.opportunity_page = self.opportunity_action.page
        self.global_search_action = GlobalSearchAction(self.driver)
        self.global_search = self.global_search_action.page

        self.login_action.log_in(self.username, self.password)
        self.opportunity_action.nav_to_listing()
        self.opportunity_page.new_button().click()
        unique_name = self.opportunity_action.fill_required_fields()
        self.opportunity_page.save_button().click()
        # After creating new opportunity, check for the presence of the success alert at the top
        try:
            if self.opportunity_page.successful_opportunity_creation_message(value=unique_name):
                assert True
        except InvalidSelectorException:
            assert False, "Failure: Creation of new opportunity failed"
        assert self.opportunity_page.opportunity_name().text == unique_name, "Failure: New opportunity name does not match expected name"
        # Allow some time for newly created opportunity to populate in search
        time.sleep(5)
        self.global_search.search_bar_button().click()
        self.global_search_action.enter_and_click_search_term(search_term=unique_name)
        self.opportunity_action.click_edit_button()
        new_stage_value = "Value Proposition"
        self.opportunity_action.select_stage_dropdown_value(new_stage_value)
        self.opportunity_action.save()
        self.driver.refresh()
        time.sleep(5)
        assert self.opportunity_page.opportunity_name().text == unique_name, "Failure: Actual page does not match expected opportunity detail page"
        self.driver.execute_script('window.scrollBy(0, 1000)')
        assert self.opportunity_page.stage_history_latest_stage().text == new_stage_value, "Failure: Stage field does not reflect new stage that was set"
