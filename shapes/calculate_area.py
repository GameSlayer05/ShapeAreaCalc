import math

def circle_calculator (radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    area = math.pi * (radius ** 2)
    return area

def rectangle_calculator (length, width):
    if length < 0:
        raise ValueError("Length cannot be negative.")
    elif width < 0:
        raise ValueError("Width cannot be negative.")
    area = length * width
    return area