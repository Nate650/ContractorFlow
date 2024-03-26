from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from .page import Page


class GlobalSearch(Page):
    def search_bar_button(self) -> WebElement:
        return self.find_element(By.XPATH, '//button[@aria-label="Search"]')

    def search_bar_field(self) -> WebElement:
        return self.find_element(By.XPATH, '//input[@placeholder="Search..."]')

    def search_term_item_match(self, search_term) -> WebElement:
        return self.find_element(By.XPATH, '//span[@title="{}"]'.format(search_term))
