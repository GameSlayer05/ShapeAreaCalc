import math

def calculator (radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    area = math.pi * (radius ** 2)
    return area

if __name__ == '__main__':
    radius = float(input("Input the radius: "))
    area = calculator(radius)
    print(f"The area of the circle with radius {radius} is: {area:.2f}")
