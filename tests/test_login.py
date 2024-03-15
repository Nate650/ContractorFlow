from tests.test import Test
from pages.login_page import LoginPage


class TestLogin(Test):
    base_url = "https://efficiency-customization-c2-dev-ed.scratch.my.salesforce.com/"
    username = "test-g47godb2ia5t@example.com"
    password = "&9qNxuqiipgbu"

    def test_home_page_title(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        actual_title = self.driver.title
        self.driver.close()

        expected_title = "Login | Salesforce"
        if actual_title == expected_title:
            assert True
        else:
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(username=self.username)
        self.login_page.set_password(password=self.password)
        self.login_page.click_login_button()
        actual_title = self.driver.title

        """
        Upon successful login, the page title takes on one value and then changes to another after a
        few seconds.  To check the second value, we wait for the "Setup Home" element to load in the 
        left nav.
        """
        expected_initial_title = "Lightning Experience"
        expected_title_after_full_page_load = "Home | Salesforce"
        if actual_title == expected_initial_title:
            assert True
        else:
            assert False

        setup_home_link_xpath = '//a[@class="slds-tree__item-label" and contains(@href, "/SetupOneHome/")]'
        self.wait(setup_home_link_xpath, setup)
        actual_title = self.driver.title
        self.driver.close()

        if actual_title == expected_title_after_full_page_load:
            assert True
        else:
            assert False
