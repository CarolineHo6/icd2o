#Find the minimum nember and type of coins needed to create the following dollar values (what aperators with be needed here)
#a)
dollars = float(input("Please enter a dollar amount: "))
t = dollars//2
total = dollars%2
l = total//1
total = total%1
q = total//0.25
total = total%0.25
d = total//0.1
total = total%0.05
n = total//0.05
total = total%0.01
p = total//0.01
print(f"There are {t} toonies, {l} loonies, {q} quarters, {d} dimes, {n} nickels, and {p} pennys in ${dollars}")