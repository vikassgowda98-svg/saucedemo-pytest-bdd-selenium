@regression
Feature: Login Regression Tests

  Scenario: Login with valid credentials
    Given user opens the SauceDemo application
    When user logs in with valid credentials
    Then user should be redirected to the products page

  Scenario: Login with invalid username
    Given user opens the SauceDemo application
    When user logs in with invalid username
    Then login error message should be displayed

  Scenario: Login with invalid password
    Given user opens the SauceDemo application
    When user logs in with invalid password
    Then login error message should be displayed

  Scenario: Login with invalid username and password
    Given user opens the SauceDemo application
    When user logs in with invalid username and invalid password
    Then login error message should be displayed

  Scenario: Login with empty username
    Given user opens the SauceDemo application
    When user enters empty username
    And user enters valid password
    And user clicks the login button
    Then login error message should be displayed

  Scenario: Login with empty password
    Given user opens the SauceDemo application
    When user enters valid username
    And user enters empty password
    And user clicks the login button
    Then login error message should be displayed

  Scenario: Login with both fields empty
    Given user opens the SauceDemo application
    When user clicks the login button
    Then login error message should be displayed

  Scenario: Locked user cannot login
    Given user opens the SauceDemo application
    When user logs in with locked user credentials
    Then login error message should be displayed

  Scenario: Login using uppercase username
    Given user opens the SauceDemo application
    When user logs in with uppercase username
    Then login error message should be displayed

  Scenario: Login using invalid special characters
    Given user opens the SauceDemo application
    When user logs in with special character credentials
    Then login error message should be displayed

  Scenario: Verify password is masked
    Given user opens the SauceDemo application
    When user enters password
    Then password should be masked

  Scenario: Verify login button is displayed
    Given user opens the SauceDemo application
    Then login button should be displayed

  Scenario: Verify username field is displayed
    Given user opens the SauceDemo application
    Then username field should be displayed

  Scenario: Verify password field is displayed
    Given user opens the SauceDemo application
    Then password field should be displayed