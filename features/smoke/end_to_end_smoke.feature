@smoke
Feature: End to End Shopping

  Scenario: User completes a purchase successfully

    Given user opens the SauceDemo application
    When user logs in with valid credentials
    And user adds a product to the cart
    And user opens the shopping cart
    And user clicks checkout
    And user enters valid checkout information
    And user clicks continue
    And user clicks finish
    Then order confirmation should be displayed