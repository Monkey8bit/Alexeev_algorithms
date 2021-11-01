def check_eq(n):
    sum_n = 0
    i = 1
    n2 = n * (n + 1) / 2
    while i <= n:
        sum_n += i
        i += 1
    return sum_n == n2


user_n = int(input("Input number for check: "))
res = check_eq(user_n)

print(res)
