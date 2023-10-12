# Question 1
print("*")
print("**")
print("***")
print("****")

# Question 4
import math
pie = math.pi
print(f"{pie:.5f}")
dog = "Luna"
print(f"{dog:^11}")

# Question 10
price = "Price"
product = "Product"
discount = "Discount"
apple = "Apple"
banana = "Banana"
orange = "Orange"
apple_p = 0.99
banana_p = 0.49
orange_p = 1.29
print(f"{price:<10}{product:12}{discount}")
print("=================================")
print(f"{apple:<10}{apple_p:<12}{apple_p:10%}")
print(f"{banana:<10}{banana_p:<12}{banana_p:5%}")
print(f"{orange:<10}{orange_p:<8}{orange_p:15%}")
print("=================================")