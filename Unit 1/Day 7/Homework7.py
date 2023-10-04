import math
# Question 1
value = math.pi
print(f"{value:.3f}")

# Question 2
price = float(29.991119)
print(f"${price:.2f}")

# Question 1 percentages with decimal places
tax_rate = 0.075
print(f"{tax_rate:.2%}")

# Question 2 percentages with decimal places
discount = .25
print(f"{discount:.1%}")

# Question 1 Width
city = "New York"
print(f"{city:<15}")

#Question 2 Width
temperature = 72.5
print(f"{temperature:^10}")

#Creating a table 
#data
item = "Product"
price = 25.99
quantity = 3
total = price*quantity

#Right aligned
print(f"Item     Price  Quantity  Total")
print(f"{item}{price:>7}{quantity:>10}{total:>7}")

# Left aligned
city = "City"
population = "Population"
area = "Area (sq Km)"
new_york = "New York"
population_n = "8,398,748"
area_n = "468.19"
los_angeles = "Los Angeles"
population_l = "3,990,456"
area_l = "503.79"
c = "Chicago"
population_c = "2,693,976"
area_c = "227.63"

print(f"{city:<13}{population:<12}{area}")
print(f"{new_york:<13}{population_n:<12}{area_n}")
print(f"{los_angeles:<13}{population_l:<12}{area_l}")
print(f"{c:<13}{population_c:<12}{area_c}")
