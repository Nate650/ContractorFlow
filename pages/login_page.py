from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from .page import Page


class LoginPage(Page):
    def username(self) -> WebElement:
        return self.find_element(By.ID, 'username')

    def password(self) -> WebElement:
        return self.find_element(By.ID, 'password')

    def login_button(self) -> WebElement:
        return self.find_element(By.ID, 'Login')

    def most_recently_used_span(self) -> WebElement:
        return self.find_element(By.XPATH, '//span[text()="Most Recently Used"]')
