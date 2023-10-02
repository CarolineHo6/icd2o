#Greeting Message
user_input = input("Enter your name: ")
print("Hello, " +user_input+ "!")

#Simple Math
x = input("Enter a number: ")
y = input("Enter second number: ")
z = int(x) + int(y)
print(f"This adds up to {z}")

#Temperature Converter
temp_celsius = float(input("Enter temperature in Celsius: "))
temp_fahrenheit = temp_celsius * 9/5 + 32
print(f"{temp_celsius} degrees celsius is equal to {temp_fahrenheit} degrees Fahrenheit.")

#Personal Inforation
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
print("Your name is " +name+ ", your age is " +age+ ", and you live in " +city+ ".")

#Area Calculator
length = input("Enter a number: ")
width = input("Enter a number: ")
area = int(length) * int(width)
print(f"The area is {area}")

#Currency Converter
Canadian_Dollars = float(input("Enter Canadian Dollars: "))
USA_Dollars = Canadian_Dollars * 1.34
print(f"You have {USA_Dollars} USD")

#String Concatenation
user_first_name = input("Enter first name: ")
user_last_name = input("Enter last name: ")
full_name = str.upper(user_first_name) + " " + str.upper(user_last_name)
print(f"Full Name:  {full_name}")

#Shopping List Total
grocery1 = input("Enter your first grocery item price: ")
grocery2 = input("Enter your second grocery item price: ")
grocery3 = input("Enter your third grocery item price: ")
total = float(grocery1) + float(grocery2) + float(grocery3)
print(f"Your total is ${total}")

#Convert Days to Hours
users_days = int(input("Enter number of days: "))
hours = users_days * 24
print (f"Days: {users_days}, Hours: {hours}.")

#Speed Calculation
user_km = float(input("Enter the amount of kilometers you drove: "))
user_hours = float(input("Enter the amount of hours it took: "))
average_speed = user_km / user_hours
print(f"Average Speed: {average_speed}km/h")
