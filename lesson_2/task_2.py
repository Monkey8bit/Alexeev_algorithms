def even_check(num):
    odd = 0
    even = 0
    for n in str(num):
        if int(n) % 2 == 0:
            even += 1
        else:
            odd += 1
    return f"Even digits count in {num}: {even}\nOdd digits count in {num}: {odd}"


number = input("Input number: ")
res = even_check(number)
print(res)
