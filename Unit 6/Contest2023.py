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

#Problem J3: Special Event
def special_event():
    n = int(input())
    day1 = 0
    day2 = 0
    day3 = 0
    day4 = 0
    day5 = 0
    for i in range(n):
        a = input()
        if a[0] == "Y":
            day1 += 1
        if a[1] == "Y":
            day2 += 1
        if a[2] == "Y":
            day3 += 1
        if a[3] == "Y":
            day4 += 1
        if a[4] == "Y":
            day5 += 1
    if day1 == n:
        print(1)
    if day2 == n:
        print(2)
    if day3 == n:
        print(3)
    if day4 == n:
        print(4)
    if day5 == n:
        print(5)
    
special_event()


