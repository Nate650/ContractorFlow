import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class AppLauncher:
    app_launcher_button = 'slds-icon-waffle'
    app_launcher_search_bar = '//input[@type="search" and @placeholder="Search apps and items..."]'

    def __init__(self, driver):
        self.driver = driver

    def click_app_launcher_button(self):
        self.driver.find_element(By.CLASS_NAME, self.app_launcher_button).click()

    def enter_and_click_search_term(self, search_term):
        search_term_link_xpath = '//p[@class="slds-truncate"]'
        self.driver.find_element(By.XPATH, self.app_launcher_search_bar).clear()
        self.driver.find_element(By.XPATH, self.app_launcher_search_bar).send_keys(search_term)
        self.driver.find_element(By.XPATH, search_term_link_xpath).click()
