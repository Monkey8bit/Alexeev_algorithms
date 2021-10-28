x1, y1 = map(int, input("Input first coordinates, separated by space: ").split())
x2, y2 = map(int, input("Input second coordinates, separated by space: ").split())

k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2

print(f"y = {k}x + {b}")
