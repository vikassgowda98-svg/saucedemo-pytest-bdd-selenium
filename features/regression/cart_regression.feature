@regression
Feature: Shopping Cart Regression Tests

  Background:
    Given user is logged in with valid credentials

  Scenario: Open empty shopping cart
    When user opens the shopping cart
    Then cart should be empty

  Scenario: Add one product to cart
    When user adds the first product to the cart
    And user opens the shopping cart
    Then selected product should be displayed

  Scenario: Add multiple products to cart
    When user adds multiple products to the cart
    And user opens the shopping cart
    Then all selected products should be displayed

  Scenario: Remove product from cart
    Given user has a product in the cart
    When user opens the shopping cart
    And user removes the product
    Then cart should be empty

  Scenario: Verify product name in cart
    Given user has a product in the cart
    When user opens the shopping cart
    Then product name should be displayed

  Scenario: Verify product price in cart
    Given user has a product in the cart
    When user opens the shopping cart
    Then product price should be displayed

  Scenario: Verify product quantity in cart
    Given user has a product in the cart
    When user opens the shopping cart
    Then product quantity should be displayed

  Scenario: Continue shopping from cart
    Given user has a product in the cart
    When user opens the shopping cart
    And user clicks continue shopping
    Then products page should be displayed

  Scenario: Cart count is updated after adding product
    When user adds the first product to the cart
    Then cart count should be "1"

  Scenario: Cart count is updated after removing product
    Given user has a product in the cart
    When user opens the shopping cart
    And user removes the product
    Then cart count should not be displayed