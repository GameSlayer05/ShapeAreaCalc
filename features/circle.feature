Feature: Calculating the area of a circle

Scenario: Calculate the area of a circle
    Given Radius of "2"
    When I need the area of a circle
    Then I get the circle area of "12.57"

Scenario: Calculate the area of a circle
    Given Radius of "3"
    When I need the area of a circle
    Then I get the circle area of "28.27"