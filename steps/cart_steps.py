from pytest_bdd import when, then

from pages.cart_page import CartPage


@then("shopping cart page should be displayed")
def verify_cart_page(driver):
    cart_page = CartPage(driver)
    assert (cart_page.get_title()== "Your Cart")


@then("selected product should be displayed")
def verify_product_in_cart(driver):
    cart_page = CartPage(driver)
    items = cart_page.get_cart_items()
    assert len(items) > 0


@when("user clicks checkout")
def click_checkout(driver):
    cart_page = CartPage(driver)
    cart_page.click_checkout()


@when("user clicks continue shopping")
def continue_shopping(driver):
    cart_page = CartPage(driver)
    cart_page.click_continue_shopping()


@when("user removes the product")
def remove_product(driver):
    cart_page = CartPage(driver)
    cart_page.remove_first_product()