from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class GlobalSearchResults:
    def __init__(self, element: WebElement):
        self.element = element

    def click_search_result(self, value):
        results = self.element.find_elements(By.XPATH, './/search_dialog-instant-result-item')
        for result in results:
            if result.find_element(By.XPATH, './/span').get_attribute('title') == value:
                result.click()
