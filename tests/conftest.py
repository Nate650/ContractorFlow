from selenium import webdriver
import pytest


@pytest.fixture
def setup(browser):
    if browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
