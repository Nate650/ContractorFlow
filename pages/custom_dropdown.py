from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class CustomDropdown:
    def __init__(self, element: WebElement):
        self.element = element

    def select_value(self, value):
        options = self.element.find_elements(By.XPATH, './/lightning-base-combobox-item')
        for option_element in options:
            if option_element.text == value:
                return option_element

    def click(self):
        self.element.click()
