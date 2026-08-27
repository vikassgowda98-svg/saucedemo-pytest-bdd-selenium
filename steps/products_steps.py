from pytest_bdd import given, when, then

from pages.login_page import LoginPage
from pages.products_page import ProductsPage


@then('products page title should be "Products"')
def verify_products_title(driver):
    products_page = ProductsPage(driver)
    assert (products_page.get_title()== "Products")


@then("product items should be displayed")
def verify_products_are_displayed(driver):
    products_page = ProductsPage(driver)
    products = (products_page.get_product_items())
    assert len(products) > 0


@then("product names should be displayed")
def verify_product_names(driver):
    products_page = ProductsPage(driver)
    names = (products_page.get_product_names())
    assert len(names) > 0


@then("product prices should be displayed")
def verify_product_prices(driver):
    products_page = ProductsPage(driver)
    prices = (products_page.get_product_prices())
    assert len(prices) > 0


@when("user adds the first product to the cart")
def add_first_product(driver):
    products_page = ProductsPage(driver)
    products_page.add_first_product_to_cart()


@then('cart count should be "1"')
def verify_cart_count(driver):
    products_page = ProductsPage(driver)
    assert (products_page.get_cart_count()== "1")


@when("user opens the shopping cart")
def open_cart(driver):
    products_page = ProductsPage(driver)
    products_page.open_cart()


@when("user sorts products by price low to high")
def sort_products_low_to_high(driver):
    products_page = ProductsPage(driver)
    products_page.sort_products("lohi")