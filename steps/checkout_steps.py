import allure
from pytest_bdd import when, then

from pages.checkout_page import CheckoutPage


@when("user enters valid checkout information")
def enter_valid_checkout_information(driver):
    with allure.step("When user enters valid checkout information"):
        checkout_page = CheckoutPage(driver)
        checkout_page.enter_customer_details("Vikas", "Gowda", "560001")


@when("user enters valid first name")
def enter_first_name(driver):
    with allure.step("When user enters valid first name"):
        checkout_page = CheckoutPage(driver)
        checkout_page.enter_first_name("Vikas")


@when("user enters empty first name")
def enter_empty_first_name(driver):
    with allure.step("When user enters empty first name"):
        checkout_page = CheckoutPage(driver)
        checkout_page.enter_first_name("")


@when("user enters valid last name")
def enter_last_name(driver):
    with allure.step("When user enters valid last name"):
        checkout_page = CheckoutPage(driver)
        checkout_page.enter_last_name("Gowda")


@when("user enters empty last name")
def enter_empty_last_name(driver):
    with allure.step("When user enters empty last name"):
        checkout_page = CheckoutPage(driver)
        checkout_page.enter_last_name("")


@when("user enters valid postal code")
def enter_postal_code(driver):
    with allure.step("When user enters valid postal code"):
        checkout_page = CheckoutPage(driver)
        checkout_page.enter_postal_code("560001")


@when("user enters empty postal code")
def enter_empty_postal_code(driver):
    with allure.step("When user enters empty postal code"):
        checkout_page = CheckoutPage(driver)
        checkout_page.enter_postal_code("")


@when("user clicks continue")
def click_continue(driver):
    with allure.step("When user clicks continue"):
        checkout_page = CheckoutPage(driver)
        checkout_page.click_continue()


@when("user clicks cancel")
def click_cancel(driver):
    with allure.step("When user clicks cancel"):
        checkout_page = CheckoutPage(driver)
        checkout_page.click_cancel()


@when("user clicks finish")
def click_finish(driver):
    with allure.step("When user clicks finish"):
        checkout_page = CheckoutPage(driver)
        checkout_page.click_finish()


@then("checkout information page should be displayed")
def verify_checkout_information_page(driver):
    with allure.step("Then checkout information page should be displayed"):
        assert "checkout-step-one" in driver.current_url


@then("checkout overview page should be displayed")
def verify_checkout_overview_page(driver):
    with allure.step("Then checkout overview page should be displayed"):
        assert "checkout-step-two" in driver.current_url


@then("total price should be displayed")
def verify_total_price_displayed(driver):
    with allure.step("Then total price should be displayed"):
        total = driver.find_element("css selector", ".summary_total_label")
        assert total.is_displayed() is True


@then("checkout error message should be displayed")
def verify_checkout_error(driver):
    with allure.step("Then checkout error message should be displayed"):
        checkout_page = CheckoutPage(driver)
        assert checkout_page.get_error_message() != ""


@then("order confirmation should be displayed")
def verify_order_confirmation(driver):
    with allure.step("Then order confirmation should be displayed"):
        checkout_page = CheckoutPage(driver)
        assert "Thank you" in checkout_page.get_confirmation_message()


@then("order confirmation message should be displayed")
def verify_order_confirmation_message(driver):
    with allure.step("Then order confirmation message should be displayed"):
        checkout_page = CheckoutPage(driver)
        assert "Thank you" in checkout_page.get_confirmation_message()