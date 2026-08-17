@regression
Feature: Products Regression Tests

  Background:
    Given user is logged in with valid credentials

  Scenario: Verify products page title
    Then products page title should be "Products"

  Scenario: Verify product list is displayed
    Then product items should be displayed

  Scenario: Verify product images are displayed
    Then product images should be displayed

  Scenario: Verify product names are displayed
    Then product names should be displayed

  Scenario: Verify product prices are displayed
    Then product prices should be displayed

  Scenario: Verify add to cart buttons are displayed
    Then add to cart buttons should be displayed

  Scenario: Sort products by name A to Z
    When user sorts products by name A to Z
    Then products should be sorted alphabetically

  Scenario: Sort products by name Z to A
    When user sorts products by name Z to A
    Then products should be sorted in reverse alphabetical order

  Scenario: Sort products by price low to high
    When user sorts products by price low to high
    Then products should be sorted by price ascending

  Scenario: Sort products by price high to low
    When user sorts products by price high to low
    Then products should be sorted by price descending

  Scenario: Add first product to cart
    When user adds the first product to the cart
    Then cart count should be "1"

  Scenario: Add second product to cart
    When user adds the second product to the cart
    Then cart count should be "1"

  Scenario: Add multiple products to cart
    When user adds multiple products to the cart
    Then cart count should show the selected product count
    Then shopping cart icon should be displayed
    Then navigation menu should be displayed