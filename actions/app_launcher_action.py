from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.app_launcher import AppLauncher


class AppLauncherAction:
    def __init__(self, driver):
        self.driver = driver
        self.page = AppLauncher(self.driver)

    def enter_and_click_search_term(self, search_term):
        WebDriverWait(self.driver, 5).until(
            lambda x: self.page.app_launcher_search_bar(),
            "Failure: App launcher search bar not found").clear()
        self.page.app_launcher_search_bar().send_keys(search_term)
        WebDriverWait(self.driver, 5).until(
            lambda x: self.page.search_term_link(),
            "Failure: Expected search term not found in search results").click()

    def click_app_launcher_button(self):
        self.page.app_launcher_button().click()
        WebDriverWait(self.driver, 7).until(
            ec.element_to_be_clickable(self.page.app_launcher_search_bar()),
            "Failure: App launcher search bar not clickable")
