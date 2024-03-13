import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage:
    username_id = "username"
    password_id = "password"
    log_in_button_id = "Login"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.ID, self.username_id).clear()
        self.driver.find_element(By.ID, self.username_id).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.ID, self.password_id).clear()
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.ID, self.log_in_button_id).click()

    def log_in(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_login_button()
        most_recently_used_span = '//span[text()="Most Recently Used"]'
        WebDriverWait(self.driver, 7).until(
            ec.presence_of_element_located((By.XPATH, most_recently_used_span)), "Failure: Expected element not found after login")
