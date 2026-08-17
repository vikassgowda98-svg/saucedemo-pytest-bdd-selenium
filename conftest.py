import pytest
from steps import login_steps
from steps import products_steps
from steps import cart_steps
from steps import checkout_steps
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


import pytest
import allure

from utils.config_reader import ConfigReader
from utils.browsers import DriverClass


def pytest_addoption(parser):

    parser.addoption(
        "--browser",
        action="store",
        default="chrome"
    )


@pytest.fixture
def config():

    return ConfigReader.load()


@pytest.fixture
def credentials():

    return {
        "username": "standard_user",
        "password": "secret_sauce"
    }


@pytest.fixture
def driver(request, config):

    browser = request.config.getoption("--browser")

    driver = DriverClass.create_driver(browser,config["headless"]
    )

    driver.implicitly_wait(
        config["implicit_wait"]
    )

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):

    outcome = yield

    report = outcome.get_result()

    if (report.when == "call" and report.failed):
        driver = item.funcargs.get("driver")

        if driver:
            allure.attach(driver.get_screenshot_as_png(), name="Failure Screenshot", attachment_type=allure.attachment_type.PNG)