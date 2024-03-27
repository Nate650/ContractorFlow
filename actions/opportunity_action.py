import time

from selenium.webdriver.support.wait import WebDriverWait
from actions.app_launcher_action import AppLauncherAction
from options.opportunity_options import OpportunityOptions
from pages.opportunity_page import OpportunityPage


class OpportunityAction:
    def __init__(self, driver):
        self.driver = driver
        self.page = OpportunityPage(self.driver)

    def nav_to_listing(self):
        app_launcher_action = AppLauncherAction(self.driver)
        app_launcher = app_launcher_action.page
        app_launcher.app_launcher_button().click()
        app_launcher_action.enter_and_click_search_term("opportunities")
        WebDriverWait(self.driver, 7).until(
            lambda driver: self.page.recently_viewed_table(),
            'Failure: "Recently Viewed" table not found after navigating to "Opportunities" listing page')

    def fill_name(self, name):
        self.page.opportunity_name_field().send_keys(name)

    def fill_date(self, date):
        self.page.opportunity_close_date().send_keys(date)

    def select_stage_dropdown_value(self, value):
        self.page.opportunity_stage_dropdown().click()
        self.page.opportunity_stage_dropdown().select_value(value).click()

    def fill_required_fields(self) -> str:
        options = OpportunityOptions()
        WebDriverWait(self.driver, 7).until(
            lambda driver: self.page.save_button(),
            'Failure: New opportunity dialog failed to appear')
        curr_time = str(time.time())
        unique_name = options.stage + " " + curr_time
        self.fill_name(unique_name)
        self.fill_date(options.close_date)
        self.select_stage_dropdown_value(value=options.stage)
        return unique_name

    def save(self):
        self.page.save_button().click()
        self.page.wait_until_disappears(self.page.save_button())

    def click_edit_button(self):
        self.page.edit_button().click()
        # Wait for "Save" button to appear in modal before taking further action
        self.page.save_button()
