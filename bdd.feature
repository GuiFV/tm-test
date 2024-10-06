Feature: Have an endpoint to retrieve policies

  Scenario: The user hits an endpoint with the policy id and gets policy details back
    Given the user has the policy ID
    When they visit the /policy endpoint
    And send the policy ID on the get request
    Then the user receives a json object with policy details