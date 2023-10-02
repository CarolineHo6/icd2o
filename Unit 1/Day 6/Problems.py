#Problem 1
drink = float(input("Enter the cost of drink: "))
appetizer = float(input("Enter the cost of the appetizer: "))
entree = float(input("Enter the cost of your entree: "))
dessert = float(input("Enter the cost of your dessert: "))
tip_rate = float(input("Enter tip rate (as a percentage, e.g., 15%): "))
subtotal = drink+appetizer+entree+dessert
tip = (tip_rate/100)*subtotal
total_cost = subtotal+tip
print(f"Bill Summary: ")
print(f"Subtotal: $ {subtotal}")
print(f"Tip ({tip_rate}): {tip}")
print(f"Total Cost: ${total_cost}")

#Building a House
length = float(input("Enter length of one wall (in meters): "))
width = float(input("Enter Width of one wall (in meters) :"))
height = float(input("Enter the height of one wall: "))
cost = float(input("Enter cost per brick (in dollars): "))
dimensions_length = float(input("Enter the length of a standard brick: "))
dimensions_width = float(input("Enter the width of a standard bricks: "))
dimensions_height = float(input("Enter the height of a standard brick: "))
surface_area = (length*height+width*height)*2
bricks_required = surface_area/(dimensions_length*dimensions_width)
total_cost = bricks_required*cost
print("House Details: ")
print(f"- Wall Surface Area: {surface_area} square meters")
print(f"- Bricks Required: {bricks_required} bricks")
print(f"- Total Cost of Bricks: ${total_cost}")

#Road Trip
distance = float(input("Enter the distance you will travel: "))
fuel_efficiency = float(input("Enter the fuel efficiency of your bechicle in kilometers per litre: "))
price_of_fuel = float(input("Enter the price of fuel per litre: "))
num_passengers = float(input("Enter the number of passengers in the vehicle: "))
total_fuel = distance/fuel_efficiency
total_fuel_cost = total_fuel*price_of_fuel
split_cost = total_fuel_cost/num_passengers
print(f"The total amount of fuel needed for the trip is {total_fuel} litres. The total cost of fuel for the trip is $ {total_fuel_cost}. The cost of fuel per passenger is ${split_cost}.")
#sav