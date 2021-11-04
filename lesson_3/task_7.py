from random import randint


lst = [randint(1, 1000) for i in range(100)]

min1 = 1000
min2 = 1000

for num in lst:
    if num <= min1:
        min1, min2 = num, min1
    elif num < min2:
        min2 = num

print(f"First min number: {min1}\nSecond min number: {min2}")
# print(sorted(lst)) for test
