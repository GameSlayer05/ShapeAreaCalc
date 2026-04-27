from behave import *
from shapes.calculate_area import rectangle_calculator
import math

@given('Length of "{length}" and Width of "{width}"')
def step_impl(context, length, width):
    context.length = float(length)
    context.width = float(width)

@when('I need the area of a rectangle')
def step_impl(context):
    context.calculated_area = round(rectangle_calculator(context.length, context.width), 2)

@then('I get the area of "{area}"')
def step_impl(context, area):
    expected_area = float(area)
    assert context.calculated_area == expected_area, f"Expected area {expected_area} based on the length of {context.length} and width of {context.width} but got {context.calculated_area}"