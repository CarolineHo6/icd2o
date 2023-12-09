import random

# Weather conditions random setting and num of customers
def weather():
    weather = random.randint(1, 5)

    # Number of customers depending on weather
    if weather == 1:
        weather_of_day = "HOT AND SUNNY"
        customers = random.randint(20, 30)
    elif weather == 2:
        weather_of_day = "SUNNY"
        customers = random.randint(15, 20)
    elif weather == 3:
        weather_of_day = "CLOUDY"
        customers = random.randint(10, 15)
    elif weather:
        weather_of_day = "LIGHT RAIN"
        customers = random.randint(7, 10)
    else:
        weather_of_day = "THUNDERSTORMS"
        customers = random.randint(0, 3)
    return weather_of_day, customers

# no money
def money_problems(num_advertisements_made, num_lemonade_made, initial_assets):
    if num_advertisements_made * 0.15 + num_lemonade_made * 0.02 > initial_assets:
        return "YOU DON'T HAVE ENOUGH MONEY"
    else:
        return "YOU'RE GOOD"

# Game intro
def game_intro():   
    print("HI! WELCOME TO LEMONSVILLE, CANADA!")
    print(" ")
    print("IN THIS SMALL TOWN, YOU ARE IN CHARGE OF RUNNING YOUR OWN LEMONADE STAND.")
    print("MAKE AS MUCH MONEY AS POSSIBLE.")
    print("IF YOU MAKE MONEY YOU WIN!")
    
# Game instructions
def game_instructions():
    print("TO MANAGE YOUR LEMONADE STAND, YOU NEED TO MAKE THESE DECISIONS EVERY DAY:")
    print(" ")
    print("1. HOW MANY GLASSES OF LEMONADE TO MAKE (ONLY ONE BATCH IS MADE EACH MORNING)")
    print("2. HOW MANY ADVERTISING SIGNS TO MAKE (THE SIGNS COST FIFTEEN CENTS EACH)")
    print("3. WHAT PRICE TO CHARGE FOR EACH GLASS")
    print(" ")
    print("YOU WILL BEGIN WITH $2.00 CASH (ASSETS).")
    print("BECAUSE YOUR MOTHER GAVE YOU SOME SUGAR, YOUR COST TO MAKE LEMONADE IS TWO CENTS A GLASS")

# Price to sell lemonade
def price():
    price = int(input("Enter the price you want to sell the lemonade (in cents): "))
    while price < 0:
        print("We aren't a charity! You are almost broke!")
        price = int(input("Enter the price you want to sell the lemonade (in cents): "))
    return price

# Days
day_num = 1

# Game intro
# If they want to start the game
go_or_stop = input("TYPE 'yes' TO START: ")
game_intro()
game_instructions()
# Money you start off with
initial_assets = 2
profit = 0
# Separating weather function stuff
weather_of_day, customers = weather()

# Day
while go_or_stop.lower != "end":
    # Printing the day
    print("DAY " + str(day_num))

    # Weather for the day
    print("THE WEATHER TODAY IS: " + str(weather_of_day))

    yes = False

    # Determining the price and amount of stuff to be made
    while yes != True:
        lemonade = int(input("ENTER THE AMOUNT OF GLASSES OF LEMONADE YOU WANT TO MAKE: "))
        advertisement = int(input("ENTER THE AMOUNT OF ADVERTISEMENTS YOU WANT TO MAKE: "))
        # Separating price
        price_ = price()
        num_customers = customers + customers * advertisement / 10
    
        # If no money
        if money_problems(advertisement, lemonade, initial_assets) == "YOU DON'T HAVE ENOUGH MONEY":
            print("YOU DON'T HAVE ENOUGH MONEY!")
        else:
            yes = True

    # If there aren't the same amount of customers and lemonades made
    if customers < lemonade:
        profit = customers * price_ - advertisement * 0.15 - lemonade * 0.02
    elif customers > lemonade:
        profit = round((lemonade * price_) - advertisement * 0.15 - lemonade * 0.02)
    
    # Assets
    total = initial_assets + profit

    # The daily money summary
    print("YOUR DAILY PROFIT SUMMARY")
    print("DAY: " + str(day_num))
    print(f"PROFIT (IN CENTS): {profit}")
    print(f"ASSETS (IN CENTS): {total}")
    go_or_stop = input("TYPE 'yes' TO START: ")

    # Adding the number to the day
    day_num +=1

