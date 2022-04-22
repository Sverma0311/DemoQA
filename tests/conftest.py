import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope='class')
def setup(request):
    browser_name = request.config.getoption("--browser_name")

    playwright = sync_playwright().start()
    if browser_name == "chrome":
        browser = playwright.chromium.launch(channel="chrome", headless=False, slow_mo=50)

    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)

    elif browser_name == "edge":
        browser = playwright.chromium.launch(channel="msedge", headless=False)
    else:
        browser = playwright.chromium.launch(headless=False)

    new_page = browser.new_page()
    new_page.set_default_timeout(40000)
    request.cls.page = new_page
    new_page.goto("https://demoqa.com/")

    yield
    new_page.close()


def pytest_addoption(parser):
    parser.addoption("--browser_name")

