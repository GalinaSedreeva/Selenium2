import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--base_url", default="http://10.0.108.38:8081")

@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("browser")
    base_url = request.config.getoption("base_url")
    driver = None

    if browser_name in ["ch", "chrome"]:
        driver = webdriver.Chrome()
    elif browser_name in ["ff", "firefox"]:
        driver = webdriver.Firefox()
    elif browser_name in ["ed", "edge"]:
        driver = webdriver.Edge()

    driver.base_url = base_url

    yield driver

    driver.quit()        
