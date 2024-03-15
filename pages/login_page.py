from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def username(self) -> WebElement:
        return self.driver.find_element(By.ID, 'username')

    def password(self) -> WebElement:
        return self.driver.find_element(By.ID, 'password')

    def login_button(self) -> WebElement:
        return self.driver.find_element(By.ID, 'Login')

    def most_recently_used_span(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//span[text()="Most Recently Used"]')
