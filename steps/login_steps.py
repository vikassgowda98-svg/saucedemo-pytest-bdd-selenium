from pytest_bdd import given, when, then, parsers

from pages.login_page import LoginPage
from pages.products_page import ProductsPage

@given("I am on the SauceDemo login page")
@given("user opens the SauceDemo application")
def open_application(driver,config):
    login_page = LoginPage(driver)
    login_page.open(config["base_url"])

@when("user logs in with valid credentials")
def login_with_valid_credentials(driver,credentials):
    login_page = LoginPage(driver)
    login_page.login(credentials["username"],credentials["password"])

@when(parsers.parse('I login with username "{username}" and password "{password}"'))
def login_with_username_password(driver, username, password):
    login_page = LoginPage(driver)
    login_page.login(username, password)


@when("user logs in with valid credentials")
def login_with_valid_credentials(driver, credentials):
    login_page = LoginPage(driver)
    login_page.login(credentials["username"],credentials["password"])

@then("I should see the products page")
@then("user should be redirected to the products page")
def verify_products_page(driver):
    products_page = ProductsPage(driver)
    assert products_page.get_title() == "Products"

@then(parsers.parse('I should see an error message "{error}"'))
def verify_error_message(driver, error):
    login_page = LoginPage(driver)
    actual_error = login_page.get_error_message()
    print(actual_error)
    assert actual_error == error