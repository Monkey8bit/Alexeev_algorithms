from collections import namedtuple


i = int(input("Input amount of companies: "))
Company = namedtuple("Company", "name, quarters")

comp_lst = []
for c in range(i):
    quarters = []
    comp_name = input(f"Name company number {c + 1}: ")
    quarters.append(int(input("First quarter profit: ")))
    quarters.append(int(input("Second quarter profit: ")))
    quarters.append(int(input("Third quarter profit: ")))
    quarters.append(int(input("Fourth quarter profit: ")))
    comp_lst.append(Company(comp_name, quarters))

average_profit = sum(sum(i.quarters) for i in comp_lst) / len(comp_lst)
print(f"Average profit for all companies for year: {average_profit}")

if any(sum(i.quarters) < average_profit for i in comp_lst):
    print(f"Companies with below average profit:"
          f" {','.join([i.name for i in comp_lst if sum(i.quarters) < average_profit])}")
if any(sum(i.quarters) > average_profit for i in comp_lst):
    print(f"Companies with above average profit: "
          f"{','.join([i.name for i in comp_lst if sum(i.quarters) > average_profit])}")
