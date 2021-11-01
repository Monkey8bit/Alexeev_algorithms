def calc(n1, n2, operator):
    if operator == "+":
        return n1 + n2
    elif operator == "-":
        return n1 - n2
    elif operator == "*":
        return n1 * n2
    else:
        if b == 0:
            return "Zero division error."
        return a / b


while True:
    a, b = map(int, input("Input two numbers, separated by space: ").split())
    op = input("Input operator: ")
    while op not in "+-*/0":
        op = input("Please enter correct operator (+, -, *, or /).\n"
                   "or enter 0 for exit: ")
    if op == "0":
        print("Goodbye.")
        break
    else:
        res = calc(a, b, op)
        print(res)
