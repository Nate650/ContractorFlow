import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.app_launcher import AppLauncher
from options.opportunity_options import OpportunityOptions


class OpportunitiesPage:
    new_button = '//a[@title="New"]'
    opportunity_name_field = '//input[@name="Name"]'
    opportunity_close_date = '//input[@name="CloseDate"]'
    opportunity_stage_dropdown = '//*[@field-label="Stage"]//button[@role="combobox"]'
    opportunity_stage_dropdown_value = '//lightning-base-combobox-item[@data-value="{}"]'
    save_button = '//button[@name="SaveEdit"]'
    successful_opportunity_creation_message = '//div[@title="{}"]'
    opportunity_name = '//lightning-formatted-text[@slot="primaryField"]'
    edit_button = '//button[@name="Edit"]'
    stage_history_latest_stage = '//article[@aria-label="Stage History"]//div[@title="Stage:"]/..//span'

    def __init__(self, driver):
        self.driver = driver

    def click_new_button(self):
        self.driver.find_element(By.XPATH, self.new_button).click()

    def nav_to_opportunities_page(self):
        app_launcher = AppLauncher(self.driver)
        app_launcher.click_app_launcher_button()
        app_launcher.enter_and_click_search_term("opportunities")

    def select_stage_dropdown_value(self, value):
        self.driver.find_element(By.XPATH, self.opportunity_stage_dropdown).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.opportunity_stage_dropdown_value.format(value)).click()

    def fill_required_fields(self) -> str:
        options = OpportunityOptions()
        curr_time = str(time.time())
        unique_name = options.stage + " " + curr_time
        self.driver.find_element(By.XPATH, self.opportunity_name_field).send_keys(unique_name)
        self.driver.find_element(By.XPATH, self.opportunity_close_date).send_keys(options.close_date)
        self.select_stage_dropdown_value(value=options.stage)
        return unique_name

    def click_save_button(self):
        self.driver.find_element(By.XPATH, self.save_button).click()

    def click_edit_button(self):
        self.driver.find_element(By.XPATH, self.edit_button).click()