a, b, c = map(int, input("Input three numbers to calculate average: ").split())
if a > b:
    if a < c:
        print(f"Average number is {a}")
    else:
        if b < c:
            print(f"Average number is {b}")
        else:
            print(f"Average number is {c}")
else:
    if a > c:
        print(f"Average number is {a}")
    else:
        if b < c:
            print(f"Average number is {b}")
        else:
            print(f"Average number is {c}")
