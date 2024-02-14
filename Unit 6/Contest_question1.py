#Deliv-e-droid: Problem J1
def deliv_e_droid():
    points = 0
    p = int(input("Enter num of packages: "))
    c = int(input("Enter num of collisions: "))

    if p > c:
        points += 500

    points += 50 * p
    points -= 10 * c

    print(points)

#Problem J2: Chili Peppers
def chili_peppers():
    heat = 0
    peppers = ["Poblano", "Mirasol", "Serrano", "Cayenne", "Thai", "Habanero"]
    n = int(input("Enter the number of peppers Ron adds: "))
    for i in range(n):
        pepper = input("Enter the pepper name: ")
        if pepper == "Poblano":
            heat += 1500
        elif pepper == "Mirasol":
            heat += 6000
        elif pepper == "Serrano":
            heat += 15500
        elif pepper == "Cayenne":
            heat += 40000
        elif pepper == "Thai":
            heat += 75000
        elif pepper == "Habanero":
            heat += 125000
    
    print(heat)

#Problem J1: Cupcake Party
def cupcake_party():
    r = int(input("Enter the number of regular boxes: "))
    s = int(input("Enter the number of small boxes: "))
    t = r*8+s*3
    t -= 28
    print(t)

#Proble J2: Fergusonball Ratings
def fergusonball_ratings():
    over = 0
    p = int(input())
    for i in range(p):
        ps = int(input())
        f = int(input())
        star = ps*5 - f*3
        if star > 40:
            over +=1
    if over == p:
        print(f"{over}+")
    else:
        print(over)

#Problem J1: Boiling Water
def boiling_water():
    b = int(input())
    p = 5*b-400
    if p < 100:
        above = 1
    if p > 100:
        above = -1
    if p == 100:
        above = 0
    print(p)
    print(above)

#Problem J2: Silent Auction
def silent_auction():
    max_bid = -1
    p = int(input())
    for i in range(p):
        name = input()
        current_bid = int(input())
        if max_bid < current_bid:
            winner = name
            max_bid = current_bid
    print(winner)
silent_auction()

