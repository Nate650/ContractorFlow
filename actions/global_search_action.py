import time

from pages.global_search import GlobalSearch


class GlobalSearchAction:
    def __init__(self, driver):
        self.driver = driver
        self.page = GlobalSearch(self.driver)

    def enter_and_click_search_term(self, search_term):
        self.page.search_bar_field().clear()
        self.page.search_bar_field().send_keys(search_term)
        time.sleep(3)
        self.page.search_term_item_match(search_term).click()
