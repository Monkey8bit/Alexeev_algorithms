from random import randint


matrix = [[randint(-1000, 1000) for num in range(10)] for sub in range(10)]

matrix_min = []
for sub in zip(*matrix):
    min_ = 1000
    for num in sub:
        if num < min_:
            min_ = num
    matrix_min.append(min_)

max_min_column = -1000
for num in matrix_min:
    if num > max_min_column:
        max_min_column = num

print(f"Max num among min column numbers: {max_min_column}")
