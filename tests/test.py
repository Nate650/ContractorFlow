import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage


class Test:
    def wait(self, locator, setup):
        WebDriverWait(setup, 10).until(EC.visibility_of_element_located
                                             ((By.XPATH, locator)))
