import math
# Question 1
def multiply(x, y):
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        return x * y

answer = multiply(2,4)
print(answer)

# Question 2
def calculate_cylinder_volume(radius, height):
    if isinstance(radius, (int, float)) and isinstance(height, (int, float)):
        return math.pi*radius**2*height

answer = calculate_cylinder_volume(3, 8)
print(f"{answer:.2f}")

# Question 3
def print_triangle(count, char, num):
    if isinstance(char, str) and isinstance (count, (int, float)) and isinstance(num, (int, float)):
        while count<=num:
            print(count*char)
            count = count+1
'''
        for item in range (1,height+1):
            print(char*num)
'''

count = 1
char = "*"
num = 2
answer = print_triangle(count, char, num)
print(answer)

#Question 4
def say_hello(name):
    if isinstance(name, str):
        print(f"Hello, {name}! Try to have a good day!")

greet = say_hello("Caroline")
print(greet)

# Question 5
def calculate_circle_area(radius):
    if isinstance(radius, (int, float)):
        print(math.pi*radius**2)

area = calculate_circle_area(2)
print(area)

#Question 6
def print_square(length):
    if isinstance(length, (int, float)):
        print(". "*length)
        for _ in range(length-2):
            print(". " + " " * (length + 1) + ".")
        print(". "*length)

square_shape = print_square(5)
print(square_shape)
        
# Question 7
def calculate_power(num1):
    if isinstance(num1, (int, float)):
        print(num1*num1)

power = calculate_power(2)
print(power)

# Question 8
def calculate_triangle_area(base, height):
    if isinstance(base, (int, float)) and isinstance(height, (int, float)):
        print(base*height/2)

traingle_area = calculate_triangle_area(3, 2)
print(traingle_area)
