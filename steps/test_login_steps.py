import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

scenarios("../features/login.feature")


@pytest.fixture
def login_page(browser):
    return LoginPage(browser)

@pytest.fixture
def products_page(browser):
    return ProductsPage(browser)


@given("I am on the SauceDemo login page")
def open_login_page(login_page):
    login_page.open_login_page()


@when(parsers.parse('I login with username "{username}" and password "{password}"'))
def login_with_params(login_page, username, password):
    login_page.login(username, password)


@when('I login with username "standard_user" and password "secret_sauce"')
def login_with_valid_user(login_page):
    login_page.login("standard_user", "secret_sauce")


@then("I should see the products page")
def verify_products_page(products_page):
    assert products_page.get_title() == "Products"


@then(parsers.parse('I should see an error message "{error}"'))
def verify_error_message(login_page, error):
    assert error in login_page.get_error_message()
