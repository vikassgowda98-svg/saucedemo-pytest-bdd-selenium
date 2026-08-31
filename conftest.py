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

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        print(">>> TEST FAILED - SCREENSHOT HOOK CALLED")

        driver = None

        try:
            driver = item.funcargs.get("driver")
        except Exception:
            driver = None

        if driver is None:
            try:
                driver = item._request.getfixturevalue("driver")
            except Exception:
                driver = None

        if driver:
            #print(">>> DRIVER FOUND")

            try:
                screenshot = driver.get_screenshot_as_png()
                #print(">>> SCREENSHOT CAPTURED")

                allure.attach(
                    screenshot,
                    name="Failure Screenshot",
                    attachment_type=allure.attachment_type.PNG,
                )

                #print(">>> SCREENSHOT ATTACHED")

            except Exception as e:
                print(f">>> SCREENSHOT ERROR: {e}")
        else:
            print(">>> DRIVER NOT FOUND FOR FAILURE HOOK")


@pytest.hookimpl(hookwrapper=False)
def pytest_bdd_before_scenario(request, feature, scenario):
    """
    Captures BDD feature and scenario names for Allure reporting
    """
    allure.dynamic.feature(feature.name)
    allure.dynamic.title(scenario.name)


@pytest.hookimpl(hookwrapper=False)
def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
    """
    Captures screenshots for all 'then' (assertion/verification) steps
    """
    # Check if this is a 'then' step (verification step)
    if step.type == 'then':
        try:
            driver = None
            
            # Try to get driver from request
            if hasattr(request, 'getfixturevalue'):
                try:
                    driver = request.getfixturevalue('driver')
                except Exception:
                    pass
            
            # Try to get driver from funcargs
            if driver is None and hasattr(request, 'funcargs'):
                driver = request.funcargs.get('driver')
            
            if driver:
                screenshot = driver.get_screenshot_as_png()
                allure.attach(
                    screenshot,
                    name=f"Step - {step.name}",
                    attachment_type=allure.attachment_type.PNG,
                )
        except Exception as e:
            print(f">>> ERROR capturing screenshot for then step: {e}")

