from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from .page import Page


class AppLauncher(Page):
    def app_launcher_button(self) -> WebElement:
        return self.find_element(By.CLASS_NAME, 'slds-icon-waffle')

    def app_launcher_search_bar(self) -> WebElement:
        return self.find_element(By.XPATH, '//input[@type="search" and @placeholder="Search apps and items..."]')

    def search_term_link(self) -> WebElement:
        return self.find_element(By.XPATH, '//p[@class="slds-truncate"]')
