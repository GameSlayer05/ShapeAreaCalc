from shapes.calculate_area import circle_calculator

if __name__ == '__main__':
    radius = float(input("Input the radius: "))
    area = circle_calculator(radius)
    print(f"The area of the circle with radius {radius} is: {area:.2f}")