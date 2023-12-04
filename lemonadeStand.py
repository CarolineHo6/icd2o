import random

# Game intro
def game_intro():
    playing_game = input("TYPE YOUR ANSWER AND HIT RETURN --> ")
    print("HI! WELCOME TO LEMONSVILLE, CANADA!")
    print(" ")
    print("IN THIS SMALL TOWN, YOU ARE IN CHARGE OF RUNNING YOUR OWN LEMONADE STAND.")
    print("MAKE AS MUCH MONEY AS POSSIBLE.")
    print("IF YOU MAKE MONEY YOU WIN!")
    print(" ")
    print("ARE YOU STARTING A NEW GAME? (YES OR NO)")
    print(f"{playing_game}")
    
    if playing_game in "no".lower():
        return game_intro
    elif playing_game in "yes".lower():
        return game_instructions
    
# Game instructions
def game_instructions():
    print("TO MANAGE YOUR LEMONADE STAND, YOU NEED TO MAKE THESE DECISIONS EVERY DAY:")
    print(" ")
    print("1. HOW MANY GLASSES OF LEMONADE TO MAKE (ONLY ONE BATCH IS MADE EACH MORNING)")
    print("2. HOW MANY ADVERTISING SIGNS TO MAKE (THE SIGNS COST FIFTEEN CENTS EACH)")
    print("3. WHAT PRICE TO CHARGE FOR EACH GLASS")
    print(" ")
    print("YOU WILL BEGIN WITH $2.00 CASH (ASSETS).")
    print("BECAUSE YOUR MOTHER GAVE YOU SOME SUGAR, YOUR COST TO MAKE LEMONADE IS TWO CENTS A GLASS (THIS MAY CHANGE IN THE FUTURE)")
    end_or_continue = input("PRESS SPACE TO CONTINUE, 'Q' TO END.... ")
    if end_or_continue in "Q":
        return game_intro
    if end_or_continue in " ":
        return "KEEP TRACK OF YOUR ASSETS, BECAUES YOU CAN'T SPEND MORE MONEY THAN YOU HAVE!"

# Money you start off with in cents
initial_assets = 200

# Weather conditions random setting and num of customers
def weather():
    weather = random.randint(1, 5)

    # Number of customers depending on weather
    if weather() == 1:
        print("HOT AND SUNNY")
        customers = random.randint(20, 30)
    elif weather() == 2:
        print("SUNNY")
        customers = random.randint(15, 20)
    elif weather() == 3:
        print("CLOUDY")
        customers = random.randint(10, 15)
    elif weather():
        print("LIGHT RAIN")
        customers = random.randint(7, 10)
    else:
        print("THUNDERSTORMS")
        customers = random.randint(0, 3)

# Price to sell lemonade
def price():
    price = int(input("Enter the price you want to sell the lemonade (in cents): "))
    if price < 0:
        print("We aren't a charity! You are almost broke!")

# Amount of lemonades to make for the day
def amount_lemonade():
    num_lemonade_made = int(input("Enter the amount of lemonades you want to make: "))
    price_lemonade = 2
    if num_lemonade_made * price_lemonade < initial_assets:
        print("You don't have enough money!")
        return amount_lemonade
    else:
        return num_lemonade_made*2

# Advertisements to make
def amount_advertisement():
    num_advertisement_made = int(input("Enter the amount of advertisements you want to make: "))
    price_advertisements = 15
    if num_advertisement_made * price_advertisements < earnings:
        print("YOU DON'T HAVE ENOUGH MONEY. CHOOSE ANOTHER AMOUNT OF ADVERTISEMENTS MADE")
        return amount_advertisement
    else:
        return num_advertisement_made * price_advertisements

# Earnings
def earnings():
    lemonade_left = amount_lemonade - weather
    lemonade_sold = amount_lemonade - lemonade_left
    money_made_from_lemonade = lemonade_sold*price
    expenses = amount_lemonade + amount_advertisement
    money_made = money_made_from_lemonade - expenses
    current_assets = money_made + initial_assets
    return money_made, current_assets

# Earning returns split
money_made, current_assets = earnings()

# Days going up
def days():
    i = 0
    for i in range():
        print("DAY " + (i + 1))

# Day
def day():
    # The day printed
    days()
    
    # Weather for the day
    print("THE WEATHER FOR TODAY IS: " + weather())

    # The cost of lemonade
    print("THE PRICE OF LEMONADE IS $0.02")

    # The name and assets
    print(f"LEMONADE STAND 1               ASSETS: {current_assets}")

    # Amount of lemonade to make
    amount_lemonade()

    # Amount of advertisements
    amount_advertisement()

    # Price to sell it at
    price()

    # Total earning for the day
    total_earnings()

# Total earnings for the day
def total_earnings():
    print(f"TOTAL EARNINGS")
    
