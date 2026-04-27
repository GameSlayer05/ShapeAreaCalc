from shapes.calculate_area import circle_calculator, rectangle_calculator

if __name__ == '__main__':
    radius = float(input("Input the radius: "))
    length = float(input("Input the length: "))
    width = float(input("Input the width: "))
    circle_area = circle_calculator(radius)
    rectangle_area = rectangle_calculator(length, width)
    print(f"The area of the circle with radius {radius} is: {circle_area:.2f}")
    print(f"The area of the rectangle with length {length} and width {width} is: {rectangle_area:.2f}")