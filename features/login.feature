Feature: Login to SauceDemo

  @smoke @TC001
  Scenario: Successful login with valid credentials
    Given I am on the SauceDemo login page
    When I login with username "standard_user" and password "secret_sauce"
    Then I should see the products page

  @TC002
  Scenario Outline: Unsuccessful login with invalid credentials
    Given I am on the SauceDemo login page
    When I login with username "<username>" and password "<password>"
    Then I should see an error message "<error>"

    Examples:
      | username      | password    | error                                                      |
      | locked_out_user | secret_sauce | Epic sadface: Sorry, this user has been locked out.      |
      | standard_user | wrong_pass  | Epic sadface: Username and password do not match any user |
