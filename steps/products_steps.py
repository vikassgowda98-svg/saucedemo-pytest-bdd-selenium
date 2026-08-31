import allure
from pytest_bdd import when, then

from pages.products_page import ProductsPage


@then('products page title should be "Products"')
def verify_products_title(driver):
    with allure.step('Then products page title should be "Products"'):
        products_page = ProductsPage(driver)
        assert products_page.get_title() == "Products"


@then("product items should be displayed")
def verify_products_are_displayed(driver):
    with allure.step("Then product items should be displayed"):
        products_page = ProductsPage(driver)
        products = products_page.get_product_items()
        assert len(products) > 0


@then("product names should be displayed")
def verify_product_names(driver):
    with allure.step("Then product names should be displayed"):
        products_page = ProductsPage(driver)
        names = products_page.get_product_names()
        assert len(names) > 0


@then("product prices should be displayed")
def verify_product_prices(driver):
    with allure.step("Then product prices should be displayed"):
        products_page = ProductsPage(driver)
        prices = products_page.get_product_prices()
        assert len(prices) > 0


@when("user adds the first product to the cart")
def add_first_product(driver):
    with allure.step("When user adds the first product to the cart"):
        products_page = ProductsPage(driver)
        products_page.add_first_product_to_cart()


@when("user adds a product to the cart")
def add_product(driver):
    with allure.step("When user adds a product to the cart"):
        products_page = ProductsPage(driver)
        products_page.add_first_product_to_cart()


@then('cart count should be "1"')
def verify_cart_count(driver):
    with allure.step('Then cart count should be "1"'):
        products_page = ProductsPage(driver)
        assert products_page.get_cart_count() == "1"


@then("product images should be displayed")
def verify_product_images(driver):
    with allure.step("Then product images should be displayed"):
        images = driver.find_elements("css selector", ".inventory_item_img")
        assert len(images) > 0


@then("add to cart buttons should be displayed")
def verify_add_to_cart_buttons(driver):
    with allure.step("Then add to cart buttons should be displayed"):
        buttons = driver.find_elements("css selector", "button.btn_inventory")
        assert len(buttons) > 0


@when("user adds the second product to the cart")
def add_second_product(driver):
    with allure.step("When user adds the second product to the cart"):
        products_page = ProductsPage(driver)
        products_page.add_product_by_index(1)


@when("user adds multiple products to the cart")
def add_multiple_products(driver):
    with allure.step("When user adds multiple products to the cart"):
        products_page = ProductsPage(driver)
        products_page.add_first_product_to_cart()
        products_page.add_product_by_index(1)


@then('cart count should show the selected product count')
def verify_cart_count_matches_selection(driver):
    with allure.step('Then cart count should show the selected product count'):
        products_page = ProductsPage(driver)
        assert products_page.get_cart_count() in {"1", "2"}


@then("shopping cart icon should be displayed")
def verify_shopping_cart_icon_displayed(driver):
    with allure.step("Then shopping cart icon should be displayed"):
        assert driver.find_element("class name", "shopping_cart_link").is_displayed() is True


@then("navigation menu should be displayed")
def verify_navigation_menu_displayed(driver):
    with allure.step("Then navigation menu should be displayed"):
        assert driver.find_element("id", "react-burger-menu-btn").is_displayed() is True


@when("user opens the shopping cart")
def open_cart(driver):
    with allure.step("When user opens the shopping cart"):
        products_page = ProductsPage(driver)
        products_page.open_cart()


@when("user sorts products by name A to Z")
def sort_products_name_asc(driver):
    with allure.step("When user sorts products by name A to Z"):
        products_page = ProductsPage(driver)
        products_page.sort_products("az")


@when("user sorts products by name Z to A")
def sort_products_name_desc(driver):
    with allure.step("When user sorts products by name Z to A"):
        products_page = ProductsPage(driver)
        products_page.sort_products("za")


@when("user sorts products by price low to high")
def sort_products_low_to_high(driver):
    with allure.step("When user sorts products by price low to high"):
        products_page = ProductsPage(driver)
        products_page.sort_products("lohi")


@when("user sorts products by price high to low")
def sort_products_high_to_low(driver):
    with allure.step("When user sorts products by price high to low"):
        products_page = ProductsPage(driver)
        products_page.sort_products("hilo")


@then("products should be sorted alphabetically")
def verify_products_sorted_alphabetically(driver):
    with allure.step("Then products should be sorted alphabetically"):
        names = [n.text for n in driver.find_elements("css selector", ".inventory_item_name")]
        assert names == sorted(names)


@then("products should be sorted in reverse alphabetical order")
def verify_products_sorted_reverse_alphabetically(driver):
    with allure.step("Then products should be sorted in reverse alphabetical order"):
        names = [n.text for n in driver.find_elements("css selector", ".inventory_item_name")]
        assert names == sorted(names, reverse=True)


@then("products should be sorted by price ascending")
def verify_products_sorted_by_price_asc(driver):
    with allure.step("Then products should be sorted by price ascending"):
        prices = [float(p.text.replace('$', '')) for p in driver.find_elements("css selector", ".inventory_item_price")]
        assert prices == sorted(prices)


@then("products should be sorted by price descending")
def verify_products_sorted_by_price_desc(driver):
    with allure.step("Then products should be sorted by price descending"):
        prices = [float(p.text.replace('$', '')) for p in driver.find_elements("css selector", ".inventory_item_price")]
        assert prices == sorted(prices, reverse=True)


@then("cart count should not be displayed")
def verify_cart_count_not_displayed(driver):
    with allure.step("Then cart count should not be displayed"):
        badges = driver.find_elements("class name", "shopping_cart_badge")
        assert len(badges) == 0

@then("logout option should be displayed")
def verify_logout_option_displayed(driver):
    with allure.step("Then logout option should be displayed"):
        products_page = ProductsPage(driver)
        assert products_page.is_logout_button_displayed() is True