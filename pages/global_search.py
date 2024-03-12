import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class GlobalSearch:
    search_bar_button = '//button[@aria-label="Search"]'
    search_bar_field = '//input[@placeholder="Search..."]'
    search_term_item_match = '//span[@title="{}"]'

    def __init__(self, driver):
        self.driver = driver

    def click_search_bar(self):
        self.driver.find_element(By.XPATH, self.search_bar_button).click()

    def enter_and_click_search_term(self, search_term):
        self.driver.find_element(By.XPATH, self.search_bar_field).clear()
        self.driver.find_element(By.XPATH, self.search_bar_field).send_keys(search_term)
        self.driver.find_element(By.XPATH, self.search_term_item_match.format(search_term)).click()
