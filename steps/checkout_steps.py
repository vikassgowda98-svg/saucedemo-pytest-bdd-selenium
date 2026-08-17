from pytest_bdd import when, then

from pages.checkout_page import CheckoutPage


@when("user enters valid checkout information")
def enter_valid_checkout_information(driver):
    checkout_page = CheckoutPage(driver)
    checkout_page.enter_customer_details("Vikas","Gowda","560001")

@when("user enters valid first name")
def enter_first_name(driver):
    checkout_page = CheckoutPage(driver)
    checkout_page.enter_first_name("Vikas")


@when("user enters valid last name")
def enter_last_name(driver):
    checkout_page = CheckoutPage(driver)
    checkout_page.enter_last_name("Gowda")


@when("user enters valid postal code")
def enter_postal_code(driver):
    checkout_page = CheckoutPage(driver)
    checkout_page.enter_postal_code("560001")


@when("user clicks continue")
def click_continue(driver):
    checkout_page = CheckoutPage(driver)
    checkout_page.click_continue()


@when("user clicks finish")
def click_finish(driver):
    checkout_page = CheckoutPage(driver)
    checkout_page.click_finish()

@then("checkout error message should be displayed")
def verify_checkout_error(driver):
    checkout_page = CheckoutPage(driver)
    assert (checkout_page.get_error_message()!= "")

@then("order confirmation should be displayed")
def verify_order_confirmation(driver):
    checkout_page = CheckoutPage(driver)
    assert ("Thank you" in checkout_page.get_confirmation_message())