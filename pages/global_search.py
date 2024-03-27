from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from .page import Page
from .global_search_results import GlobalSearchResults


class GlobalSearch(Page):
    def search_bar_button(self) -> WebElement:
        return self.find_element(By.XPATH, '//button[@aria-label="Search"]')

    def search_bar_field(self) -> WebElement:
        return self.find_element(By.XPATH, '//input[@placeholder="Search..."]')

    def search_results(self) -> GlobalSearchResults:
        return GlobalSearchResults(self.find_element(By.XPATH, '//div[contains(@class, "saDialogPaneContainer")]'))
