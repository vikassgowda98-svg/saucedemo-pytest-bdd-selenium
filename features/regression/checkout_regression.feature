
@regression
Feature: Checkout Regression Tests

  Background:
    Given user is logged in with valid credentials
    And user has a product in the cart

  Scenario: Open checkout page
    When user opens the shopping cart
    And user clicks checkout
    Then checkout information page should be displayed

  Scenario: Checkout with valid information
    When user enters valid first name
    And user enters valid last name
    And user enters valid postal code
    And user clicks continue
    Then checkout overview page should be displayed

  Scenario: Checkout with empty first name
    When user enters empty first name
    And user enters valid last name
    And user enters valid postal code
    And user clicks continue
    Then checkout error message should be displayed

  Scenario: Checkout with empty last name
    When user enters valid first name
    And user enters empty last name
    And user enters valid postal code
    And user clicks continue
    Then checkout error message should be displayed

  Scenario: Checkout with empty postal code
    When user enters valid first name
    And user enters valid last name
    And user enters empty postal code
    And user clicks continue
    Then checkout error message should be displayed

  Scenario: Checkout with all fields empty
    When user clicks continue
    Then checkout error message should be displayed

  Scenario: Cancel checkout
    When user opens the shopping cart
    And user clicks checkout
    And user clicks cancel
    Then products page should be displayed

  Scenario: Verify checkout overview
    When user enters valid checkout information
    And user clicks continue
    Then checkout overview page should be displayed

  Scenario: Verify total price
    When user enters valid checkout information
    And user clicks continue
    Then total price should be displayed

  Scenario: Complete order successfully
    When user enters valid checkout information
    And user clicks continue
    And user clicks finish
    Then order confirmation should be displayed

  Scenario: Verify order confirmation message
    When user enters valid checkout information
    And user clicks continue
    And user clicks finish
    Then order confirmation message should be displayed