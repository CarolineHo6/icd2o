# Print the number from 1-100 inclusive
def while_loop_1():
    integer = 0
    while integer < 100:
        integer += 1
        print(integer)

def for_loop_1():
    for i in range(1, 101):
        print(i)

# Print the even numbers from 1 to 500 inclusive
def while_loop_2():
    integer = 0
    while integer < 500:
        integer += 1
        print(integer)

def for_loop_2():
    for i in range(0,501,2):
        print(i)

# Print the odd numbers from 1 to 500 inclusive
def while_loop_3():
    integer = 1
    while integer < 499:
        integer += 2
        print(integer)

def for_loop_3():
    for i in range(1, 500, 2):
        print(i)

# Print the numbers from 100 to 1 inclusive (i.e. count backwards)
def while_loop_4():
    integer = 100
    while integer > 0:
        integer -= 1
        print(integer)

def for_loop_4():
    for i in range(100, 0, -1):
        print(i)

# Print the even numbers from 500 to 1 inclusive
def while_loop_5():
    integer = 0
    while integer < 500:
        integer += 2
        print(integer)

def for_loop_5():
    for i in range(500, 0, -2):
        print(i)

# Print the odd numbers from 500 to 1 inclusive
def while_loop_6():
    integer = 1
    while integer < 499:
        integer += 2
        print(integer)

def for_loop_6():
    for i in range(499, 1, -2):
        print(i)

# Calculate and print the sum of all the odd numbers from 1 to 100 inclusive
def while_loop_7():
    integer = 1
    num = 0
    while integer <= 100:
        num += integer
        integer += 2
    print(num)

def for_loop_7():
    count = 0
    for i in range(1, 101, 2):
        count += i
    print(count)

# Takes in a string and prints the string in reverse order
def while_loop_8():
    string1 = str(input("Enter a word: "))
    j = len(string1) - 1
    result = ''
    while j >= 0:
        result += string1[j]
        j -= 1
    print(result)

def for_loop_8():
    str = input("Enter a word: ")
    result = ''
    for i in range(len(str)-1, -1, -1):
        result += str[i]
    print(result)

# Takes in an integer and calculates and prints the factorial of that number
def while_loop9():
    int1 = int(input("Enter a number: "))
    result = 1
    counter = 1
    while counter <= int1:
        result *= counter
        counter += 1
    print(result)

def for_loop_9():
    int1 = int(input("Enter a number: "))
    result = int1
    for i in range(int1 - 1, 0, -1):
        result *= i
    print(result)

# loop through all the number then use the % to get the remainder, or make it go up by 2 instead

