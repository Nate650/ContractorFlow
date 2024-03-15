from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page import LoginPage


class LoginAction:
    def __init__(self, driver):
        self.driver = driver
        self.page = LoginPage(self.driver)

    def fill_username(self, username):
        self.page.username().clear()
        self.page.username().send_keys(username)

    def fill_password(self, password):
        self.page.password().clear()
        self.page.password().send_keys(password)

    def log_in(self, username, password):
        self.fill_username(username)
        self.fill_password(password)
        self.page.login_button().click()
        # After logging in, wait until "Most Recently Used" element is present before taking further action
        WebDriverWait(self.driver, 7).until(
            lambda x: self.page.most_recently_used_span(),
            "Failure: Expected element not found after login")
