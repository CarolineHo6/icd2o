import math

# Write a Python program using a while loop to find the sum of all even numbers from 1 to 10.
def sum_even():
    sum = 0
    total = -11
    while sum <= 10:
        sum += 2
        total += sum
    print(total)

# Print * in triangle
def triangle():
    for i in range(1, 6):
        print('*' * i)

# Print the factorial of a number
def factorial_num():
    num = int(input("Enter a number: "))
    for i in range(num -1, 0, -1):
        num *= i
    print(num)

factorial_num()

# Print the area of a circle when given the radius
def area_of_circle():
    radius = float(input("Enter the radius of a circle: "))
    area = math.pi * radius**2
    return area

area_of_circle()