from behave import *
from shapes.calculate_area import circle_calculator
import math

@given('Radius of "{radius}"')
def step_impl(context, radius):
    context.radius = radius

@when('I need the area of a circle')
def step_impl(context):
    context.calculated_area = circle_calculator(context.radius)

@then('I am able to find the area with the radius')
def step_impl(context):
    expected_area = math.pi * (context.radius ** 2)
    assert context.calculated_area == expected_area, f"Expected area {expected_area} based on the radius of {context.radius} but got {context.calculated_area}"