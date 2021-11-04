matrix = [[int(input("Input number:")) for i in range(3)] for sub in range(5)]

for sub in matrix:
    row_sum = 0
    for num in sub:
        row_sum += num
    sub.append(row_sum)

print(matrix)
