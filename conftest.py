import pytest
from selenium import webdriver


def pytest_addoption(parser):
    print("Registering command line options")
    parser.addoption("--browser", action="store", default="firefox", help="Browser to run tests")


@pytest.fixture(scope="module")
def driver(request):
    browser_choice = request.config.getoption("--browser")
    if browser_choice == "chrome":
        driver = webdriver.Chrome()
    elif browser_choice == "firefox":
        driver = webdriver.Firefox()
    elif browser_choice == "edge":
        driver = webdriver.Edge()
    elif browser_choice == "safari":
        driver = webdriver.Safari()
    elif browser_choice == "opera":
        driver = webdriver.Opera()
    else:
        raise ValueError(f"Unsupported browser: {browser_choice}")

    yield driver
    driver.quit()
