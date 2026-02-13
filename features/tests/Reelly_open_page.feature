
Feature: Test case for web opening
  Scenario: User can open the community page
    Given Open Sign in page
    When log in to page
    And Click on the setting option
    And Click on the Community option
    And Verify the right page open
    Then Verify the "Support" button is available and clickable