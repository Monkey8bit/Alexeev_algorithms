a, b, c = map(int, input("Input three sides of triangle, separated by space: ").split())

if a + b < c or b + c < a or a + c < b:
    print("Impossible triangle.")
elif a == b:
    if b == c:
        print("Equilateral triangle.")
    else:
        print("Isosceles triangle.")
elif a != b:
    if b == c:
        print("Isosceles triangle")
    else:
        print("Versatile triangle.")
