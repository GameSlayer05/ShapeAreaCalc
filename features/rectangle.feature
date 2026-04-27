Feature: Calculating the area of a rectangle

Scenario: Calculate the area of a rectangle
    Given Length of "2" and Width of "2"
    When I need the area of a rectangle
    Then I get the rectangle area of "4"

Scenario: Calculate the area of a rectangle
    Given Length of "3" and Width of "2"
    When I need the area of a rectangle
    Then I get the rectangle area of "6"