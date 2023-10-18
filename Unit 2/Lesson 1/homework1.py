import math
# Question 1
def area_of_rectangle(length, width):
    if isinstance(length, (int, float)) and isinstance(width, (int, float)):
        return length*width
    else:
        return "Invalid input. Please enter a numeric value."
length = float(input("Enter a number: "))
width = float(input("Enter another number: "))
answer = area_of_rectangle(length, width)
print(f"The area of the rectangle is {answer:.2f} square units.")


# Question 2
def contains_substring(string, substring):
    if isinstance(string, str) and isinstance(substring, str):
        return bool(substring in string)
    else:
        return "Invalid input. Please enter a numeric value"
string = input("Enter a word: ")
substring = input("Enter another word that is within the first word: ")
print(f"Substring {substring} is present in the string: {contains_substring(string, substring)}")

# Question 3
def average_of_three_floats(d1, d2, d3):
    if all(isinstance (x, float) for x in [d1, d2, d3]):
        return (d1+d2+d3)/3.0
    else:
        return "Invalid input. Please enter a numeric value."
d1 = float(input("Enter a number: "))
d2 = float(input("Enter a number: "))
d3 = float(input("Enter a number: "))
print(f"The average is {average_of_three_floats(d1, d2, d3)}")

#Question 4
def concatenate_strings(string1, string2):
    if all (isinstance (x, str) for x in [string1, string2]):
        return string1 + string2
    else:
        return "Invalid Input. Please enter a word."
string1 = input("Enter a word: ")
string2 = input("Enter another word: ")
print(f"{concatenate_strings(string1, string2)}")

#Question 5
def volume_of_cube(length):
    if isinstance(length, (int, float)):
        return length**3
length = float(input("Enter a number: "))
print(f"The volume of the cube is {volume_of_cube(length):.2f}")

# Question 6
def check_number_status(number):
    if isinstance(number (int, float)):
        if number>0:
            return "Positive"
    elif number<0:
        return "Negative"
    else:
        return "Zero"
number = float(input("Enter a number: "))
print(f"Your number is {check_number_status(number)}")

# Question 7
def circumference_of_circle(radius):
    if isinstance(radius, (int, float)):
        return 2 * math.pi * radius
    else:
        return "Invalid Input. Please enter a numeric value."
radius = float(input("Enter a radius: "))
print(f"The circumference of your circle is {circumference_of_circle(radius):.2f}")

# Question 8
def count_char_occurrences(string, char):
    if isinstance(string, str) and isinstance(char, str) and len(char)==1:
        return string.count(char)
    else:
        return "Invalid input. Please enter a word and letter"
string = input("Enter a word: ")
char = input("Enter a letter: ")
print(f"The character {char} occurs {count_char_occurrences(string, char)} in the string.")

# Question 9
def calculate_percentage(num, percent):
    if all(isinstance (x, (int, float)) for x in [num, percent]):
        return (percent/100)*num
    else:
        return "Invalid input. Please enter a numeric value."
num = float(input("Enter a number: "))
percent = float(input("Enter a percentage: "))
print(f"{percent}% of the number is {calculate_percentage(num, percent):.2f}")
    
# Question 10
def absolute_difference(number, number2):
    if isinstance(number, (int, float)) and isinstance(number2, (int, float)):
        return number - number2
    else:
        return "Invalid input. Please enter a numeric value."
number = float(input("Enter a number: "))
number2 = float(input("Enter another number: "))
print(f"The absolute difference is {absolute_difference(number, number2):.2f}")