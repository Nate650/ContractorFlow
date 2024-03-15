from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class GlobalSearch:
    def __init__(self, driver):
        self.driver = driver

    def search_bar_button(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//button[@aria-label="Search"]')

    def search_bar_field(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//input[@placeholder="Search..."]')

    def search_term_item_match(self, search_term) -> WebElement:
        return self.driver.find_element(By.XPATH, '//span[@title="{}"]'.format(search_term))
