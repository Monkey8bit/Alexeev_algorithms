START_NUM = 2
END_NUM = 99
START_DIVIDER = 2
END_DIVIDER = 9

result = ""
for divider in range(START_DIVIDER, END_DIVIDER + 1):
    result += f"Count of multiple for number {divider}: "
    count = 0
    for num in range(START_NUM, END_NUM + 1):
        if num % divider == 0:
            count += 1
    result += f"{count}\n"

print(result)
