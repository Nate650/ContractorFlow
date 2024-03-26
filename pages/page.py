from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Page:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator_type, locator):
        return WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((locator_type, locator))
        )

    def wait_until_disappears(self, element):
        return WebDriverWait(self.driver, 10).until(
            ec.invisibility_of_element(element)
        )
