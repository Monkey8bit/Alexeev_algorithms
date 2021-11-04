from random import randint


lst = [randint(-100, 100) for i in range(100)]
print(lst)

max_neg = -100
for num in lst:
    if num >= 0:
        continue
    else:
        if num > max_neg:
            max_neg = num

print(f"Maximum negative number: {max_neg}.\nIndex of {max_neg}: {lst.index(max_neg)}")
