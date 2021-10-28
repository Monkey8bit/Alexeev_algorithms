import random


a, b = map(int, input("Input two numbers, separated by space: ").split())
l_1, l_2 = input("Input two symbols from alphabet, separated by space: ").split()

print(f"Random int: {random.randint(a, b)}")
print(f"Random float: {round(random.uniform(a, b), 3)}")
print(f"Random symbol between {l_1} and {l_2}: {chr(random.randint(ord(l_1), ord(l_2)))}")
