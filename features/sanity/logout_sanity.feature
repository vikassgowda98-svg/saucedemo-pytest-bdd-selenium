@sanity
Feature: Logout Tests

  Background:
    Given user is logged in with valid credentials

  Scenario: Logout successfully
    When user logs out
    Then login page should be displayed

  Scenario: Verify logout menu
    When user opens the navigation menu
    Then logout option should be displayed

  Scenario: Verify user cannot access products after logout
    When user logs out
    And user navigates to the products page
    Then user should be redirected to the login page