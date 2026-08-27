import pytest
import allure
# from steps import login_steps
# from steps import products_steps
# from steps import cart_steps
# from steps import checkout_steps
from utils.config_reader import ConfigReader
from utils.browsers import DriverClass

pytest_plugins = [
    "steps.login_steps",
    "steps.products_steps",
    "steps.cart_steps",
    "steps.checkout_steps",
]

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests on"
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

    driver = DriverClass.create_driver(browser,config["headless"])

    driver.implicitly_wait(config["implicit_wait"])

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )