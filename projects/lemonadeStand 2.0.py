# Import random
import random

# Weather
weather = ["HOT AND SUNNY", "SUNNY", "CLOUDY", "RAINY"]
weather_for_day = random.choice(weather)

# Customers
def weather_customers():
    if weather in "HOT AND SUNNY":
        customers = random.randint(15, 50)
    elif weather in "SUNNY":
        customers = random.randint(10, 30)
    elif weather in "CLOUDY":
        customers = random.randint(5, 15)
    elif weather in "RAINY":
        customers = random.randint(0, 7)
    else:
        customers = 0

# Price
def price(weather, price):
    if weather == "HOT AND SUNNY":
        if price < 4:
            return "OK"
        else:
            return "TOO MUCH MONEY"
    if weather == "SUNNY":
        if price < 3:
            return "OK"
        else:
            return "TOO MUCH MONEY"
    if weather == "CLOUDY":
        if price < 2:
            return "OK"
        else:
            return "TOO MUCH MONEY"
    if weather == "RAINY":
        if price < 1:
            return "OK"
        else:
            return "TOO MUCH MONEY"

# Money problems
def money_problems(advertisement, lemonade, total):
    if advertisement * 0.15 + lemonade * 0.02 > total:
        return "YOU DON'T HAVE ENOUGH MONEY"
    else:
        return "OK"

# Intro
go_or_end = input("TYPE YES TO START: ")
day = 1
print("WECOME TO LEMONSVILLE, CANADA")
print("YOU MUST MAKE MONEY BY RUNNING YOUR CITY'S LEMONADE STAND")
print("YOUR PARENTS HAS GIVEN YOU $2 TO START UP YOUR BUSINESS")
total = 2
profit = 0
print("IT COSTS $0.02 TO MAKE 1 GLASS OF LEMONADE")

# While the game is decided to go
while go_or_end != "end":
    print("DAY " + str(day))

    customer, weather = weather_customers()
    print("THE WEATHER TODAY IS: " + weather)

    yes = False

    while yes == False:
        advertisement = int(input("ENTER THE NUMBER OF ADVERTISEMENTS YOU WOULD LIKE TO MAKE: "))
        num_customer = customer + customer * advertisement / 10
        lemonade = int(input("ENTER THE NUMBER OF GLASSES OF LEMONADES YOU WOULD LIKE TO MAKE: "))
        price = float(input("ENTER THE PRICE YOU WANT TO SELL YOUR LEMONADE: "))

        if money_problems(advertisement, lemonade, total) == "YOU DON'T HAVE ENOUGH MONEY":
            print("YOU DON'T HAVE ENOUGH MONEY")
        else:
            yes == True
    
    if customer > lemonade:
        profit = lemonade * price - advertisement * 0.15 - lemonade * 0.02
    elif customer < lemonade:
        profit = round((customer * price) - advertisement * 0.15 - lemonade * 0.02, 2)
    
    total = total + profit

    print("PROFIT: " + str(profit))
    print("ASSETS: " + str(total))
    go_or_end = input("TYPE YES TO START: ")

    day += 1
