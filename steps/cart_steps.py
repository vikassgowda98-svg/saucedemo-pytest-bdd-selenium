import allure
from pytest_bdd import when, then, given

from pages.cart_page import CartPage


@given("user has a product in the cart")
def user_has_product_in_cart(driver):
    with allure.step("Given user has a product in the cart"):
        driver.find_element("css selector", "button.btn_inventory").click()


@then("shopping cart page should be displayed")
def verify_cart_page(driver):
    with allure.step("Then shopping cart page should be displayed"):
        cart_page = CartPage(driver)
        assert cart_page.get_title() == "Your Cart"


@then("selected product should be displayed")
def verify_product_in_cart(driver):
    with allure.step("Then selected product should be displayed"):
        cart_page = CartPage(driver)
        items = cart_page.get_cart_items()
        assert len(items) > 0


@then("all selected products should be displayed")
def verify_all_selected_products_in_cart(driver):
    with allure.step("Then all selected products should be displayed"):
        items = driver.find_elements("css selector", ".cart_item")
        assert len(items) > 0


@then("cart should be empty")
def verify_cart_is_empty(driver):
    with allure.step("Then cart should be empty"):
        cart_page = CartPage(driver)
        assert len(cart_page.get_cart_items()) == 0


@then("product name should be displayed")
def verify_product_name_displayed(driver):
    with allure.step("Then product name should be displayed"):
        assert len(driver.find_elements("css selector", ".inventory_item_name")) > 0


@then("product price should be displayed")
def verify_product_price_displayed(driver):
    with allure.step("Then product price should be displayed"):
        assert len(driver.find_elements("css selector", ".inventory_item_price")) > 0


@then("product quantity should be displayed")
def verify_product_quantity_displayed(driver):
    with allure.step("Then product quantity should be displayed"):
        assert len(driver.find_elements("css selector", ".cart_quantity")) > 0


@when("user clicks checkout")
def click_checkout(driver):
    with allure.step("When user clicks checkout"):
        cart_page = CartPage(driver)
        cart_page.click_checkout()


@when("user clicks continue shopping")
def continue_shopping(driver):
    with allure.step("When user clicks continue shopping"):
        cart_page = CartPage(driver)
        cart_page.click_continue_shopping()


@when("user removes the product")
def remove_product(driver):
    with allure.step("When user removes the product"):
        cart_page = CartPage(driver)
        cart_page.remove_first_product()