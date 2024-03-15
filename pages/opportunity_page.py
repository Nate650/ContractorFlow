from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class OpportunityPage:
    def __init__(self, driver):
        self.driver = driver

    def new_button(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//a[@title="New"]')

    def opportunity_stage_dropdown(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//*[@field-label="Stage"]//button[@role="combobox"]')

    def opportunity_stage_dropdown_value(self, value) -> WebElement:
        return self.driver.find_element(By.XPATH, '//lightning-base-combobox-item[@data-value="{}"]'.format(value))

    def opportunity_name_field(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//input[@name="Name"]')

    def opportunity_close_date(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//input[@name="CloseDate"]')

    def save_button(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//button[@name="SaveEdit"]')

    def successful_opportunity_creation_message(self, value) -> WebElement:
        return self.driver.find_element(By.XPATH, '//div[@title="{}"]'.format(value))

    def opportunity_name(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//lightning-formatted-text[@slot="primaryField"]')

    def edit_button(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//button[@name="Edit"]')

    def stage_history_latest_stage(self) -> WebElement:
        return WebDriverWait(self.driver, 7).until(
            ec.visibility_of_element_located((By.XPATH, '//article[@aria-label="Stage History"]//div[@title="Stage:"]/..//span')),
            'Failure: "Stage:" value not found in "Stage History" section')

    def recently_viewed_table(self) -> WebElement:
        return self.driver.find_element(By.XPATH, '//table[@aria-label="Recently Viewed"]')
