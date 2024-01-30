import math

figure = input()

if figure == "square":
    side = float(input())
    square_area = side * side
    print(f"{square_area :.3f}")
elif figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    square_area_1 = side_a * side_b
    print(f"{square_area_1 :.3f}")
elif figure == "circle":
    circuit = float(input())
    circle_circuit = math.pi * circuit ** 2
    print(f"{circle_circuit : .3f}")
elif figure == "triangle":
    side = float(input())
    height = float(input())
    area_triangle = side * height / 2
    print(f"{area_triangle :.3f}")
