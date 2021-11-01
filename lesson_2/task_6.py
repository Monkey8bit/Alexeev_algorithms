import random


r_num = random.randint(0, 100)
i = 10

while i > 0:
    user_n = input("Guess number from 0 to 100: ")
    if int(user_n) == r_num:
        print("Correct answer.")
        break
    i -= 1
    print("Wrong number, try again.")
else:
    print(f"Attempts ran out, correct answer: {r_num}. ")
