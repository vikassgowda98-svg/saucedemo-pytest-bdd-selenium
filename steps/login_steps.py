import allure
from pytest_bdd import given, when, then, parsers

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


@given("I am on the SauceDemo login page")
@given("user opens the SauceDemo application")
def open_application(driver, config):
    with allure.step("Given I am on the SauceDemo login page"):
        login_page = LoginPage(driver)
        login_page.open(config["base_url"])


@given("user is logged in with valid credentials")
def login_user(driver, config, credentials):
    with allure.step("Given user is logged in with valid credentials"):
        login_page = LoginPage(driver)
        login_page.open(config["base_url"])
        login_page.login(credentials["username"], credentials["password"])


@when("user logs in with valid credentials")
def login_with_valid_credentials(driver, credentials):
    with allure.step("When user logs in with valid credentials"):
        login_page = LoginPage(driver)
        login_page.login(credentials["username"], credentials["password"])


@when(parsers.parse('I login with username "{username}" and password "{password}"'))
def login_with_username_password(driver, username, password):
    with allure.step(f'When I login with username "{username}" and password "{password}"'):
        login_page = LoginPage(driver)
        login_page.login(username, password)


@when("user logs in with invalid username")
def login_with_invalid_username(driver):
    with allure.step("When user logs in with invalid username"):
        login_page = LoginPage(driver)
        login_page.login("invalid_user", "secret_sauce")


@when("user logs in with invalid password")
def login_with_invalid_password(driver):
    with allure.step("When user logs in with invalid password"):
        login_page = LoginPage(driver)
        login_page.login("standard_user", "wrong_pass")


@when("user logs in with invalid username and invalid password")
def login_with_invalid_username_and_password(driver):
    with allure.step("When user logs in with invalid username and invalid password"):
        login_page = LoginPage(driver)
        login_page.login("invalid_user", "wrong_pass")


@when("user enters empty username")
def enter_empty_username(driver):
    with allure.step("When user enters empty username"):
        login_page = LoginPage(driver)
        login_page.enter_username("")


@when("user enters valid password")
def enter_valid_password(driver, credentials):
    with allure.step("When user enters valid password"):
        login_page = LoginPage(driver)
        login_page.enter_password(credentials["password"])


@when("user clicks the login button")
def click_login_button(driver):
    with allure.step("When user clicks the login button"):
        login_page = LoginPage(driver)
        login_page.click_login()


@when("user enters valid username")
def enter_valid_username(driver, credentials):
    with allure.step("When user enters valid username"):
        login_page = LoginPage(driver)
        login_page.enter_username(credentials["username"])


@when("user enters empty password")
def enter_empty_password(driver):
    with allure.step("When user enters empty password"):
        login_page = LoginPage(driver)
        login_page.enter_password("")


@when("user logs in with locked user credentials")
def login_with_locked_user(driver):
    with allure.step("When user logs in with locked user credentials"):
        login_page = LoginPage(driver)
        login_page.login("locked_out_user", "secret_sauce")


@when("user logs in with uppercase username")
def login_with_uppercase_username(driver):
    with allure.step("When user logs in with uppercase username"):
        login_page = LoginPage(driver)
        login_page.login("STANDARD_USER", "secret_sauce")


@when("user logs in with special character credentials")
def login_with_special_character_credentials(driver):
    with allure.step("When user logs in with special character credentials"):
        login_page = LoginPage(driver)
        login_page.login("!@#", "secret_sauce")


@when("user enters password")
def enter_password(driver):
    with allure.step("When user enters password"):
        login_page = LoginPage(driver)
        login_page.enter_password("secret_sauce")


@then("I should see the products page")
@then("user should be redirected to the products page")
@then("products page should be displayed")
def verify_products_page(driver):
    with allure.step("Then I should see the products page"):
        products_page = ProductsPage(driver)
        assert products_page.get_title() == "Products"


@then("Your Cart page should be displayed")
def verify_your_cart_page(driver):
    with allure.step("Then I should see the Your Cart page"):
        cart_page = CartPage(driver)
        assert cart_page.get_title() == "Your Cart"

@then("login page should be displayed")
def verify_login_page(driver):
    with allure.step("Then login page should be displayed"):
        login_page = LoginPage(driver)
        assert login_page.is_login_button_displayed() is True


@then("user should be redirected to the login page")
def verify_login_redirect(driver):
    with allure.step("Then user should be redirected to the login page"):
        assert "saucedemo.com" in driver.current_url
        login_page = LoginPage(driver)
        assert login_page.is_login_button_displayed() is True


@then(parsers.parse('I should see an error message "{error}"'))
def verify_error_message(driver, error):
    with allure.step(f'Then I should see an error message "{error}"'):
        login_page = LoginPage(driver)
        actual_error = login_page.get_error_message()
        assert actual_error == error


@then("login error message should be displayed")
def verify_login_error_message(driver):
    with allure.step("Then login error message should be displayed"):
        login_page = LoginPage(driver)
        assert login_page.get_error_message() != ""


@then("password should be masked")
def verify_password_is_masked(driver):
    with allure.step("Then password should be masked"):
        password_field = driver.find_element("id", "password")
        assert password_field.get_attribute("type") == "password"


@then("login button should be displayed")
def verify_login_button_displayed(driver):
    with allure.step("Then login button should be displayed"):
        login_page = LoginPage(driver)
        assert login_page.is_login_button_displayed() is True


@then("username field should be displayed")
def verify_username_field_displayed(driver):
    with allure.step("Then username field should be displayed"):
        assert driver.find_element("id", "user-name").is_displayed() is True


@then("password field should be displayed")
def verify_password_field_displayed(driver):
    with allure.step("Then password field should be displayed"):
        assert driver.find_element("id", "password").is_displayed() is True


@when("user logs out")
def logout(driver):
    with allure.step("When user logs out"):
        products_page = ProductsPage(driver)
        products_page.open_menu()
        products_page.logout()


@when("user opens the navigation menu")
def open_navigation_menu(driver):
    with allure.step("When user opens the navigation menu"):
        products_page = ProductsPage(driver)
        products_page.open_menu()


@when("user navigates to the products page")
def navigate_to_products_page(driver, config):
    with allure.step("When user navigates to the products page"):
        driver.get(config["base_url"] + "inventory.html")