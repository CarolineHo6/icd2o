yes = False
assests = 200

while yes != True:
    lemonade = int(input("Enter the number of lemonades you would like to make: "))
    if lemonade > assests:
        print("You have no money!")
    else:
        yes = True


