from pytest_bdd import given, when, then

from pages.login_page import LoginPage
from pages.products_page import ProductsPage


@given("user opens the SauceDemo application")
def open_application(driver,config):
    login_page = LoginPage(driver)
    login_page.open(config["base_url"])

@when("user logs in with valid credentials")
def login_with_valid_credentials(driver,credentials):
    login_page = LoginPage(driver)
    login_page.login(credentials["username"],credentials["password"])

@then("products page should be displayed")
def verify_products_page(driver):
    products_page = (ProductsPage(driver))
    assert (products_page.get_title()== "Products")