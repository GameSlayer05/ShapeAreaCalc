from behave import *
from shapes.calculate_area import circle_calculator
import math

@given('Radius of "{radius}"')
def step_impl(context, radius):
    context.radius = float(radius)

@when('I need the area of a circle')
def step_impl(context):
    context.calculated_area = round(circle_calculator(context.radius), 2)

@then('I get the circle area of "{area}"')
def step_impl(context, area):
    expected_area = float(area)
    assert context.calculated_area == expected_area, f"Expected area {expected_area} based on the radius of {context.radius} but got {context.calculated_area}"