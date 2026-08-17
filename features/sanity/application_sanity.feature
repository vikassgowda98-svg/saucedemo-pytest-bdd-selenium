@sanity
Feature: Application Sanity Tests

  Scenario: Application launches successfully
    Given user opens the SauceDemo application
    Then login page should be displayed

  Scenario: User can login
    Given user opens the SauceDemo application
    When user logs in with valid credentials
    Then products page should be displayed

  Scenario: Products are available
    Given user is logged in with valid credentials
    Then product items should be displayed

  Scenario: User can add product to cart
    Given user is logged in with valid credentials
    When user adds the first product to the cart
    Then cart count should be "1"

  Scenario: User can open cart
    Given user is logged in with valid credentials
    When user opens the shopping cart
    Then shopping cart page should be displayed