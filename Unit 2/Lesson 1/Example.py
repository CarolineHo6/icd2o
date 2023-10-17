import math
# Function to calculate the area of a rectangle
def area_of_rectangle(length, width):
    if isinstance(length, (int, float)) and isinstance(width, (int, float)):
    # If you put or instead of and you put a word it print the word the amount of times the number you put.
        return length * width
    else:
        return "inbalid input. Pease provide numeric values for length and width"
    



# Will give you 800. Can't put words in.
l = 400
w = 2
print(area_of_rectangle(l,w))


# Function to check if a string contains a specific substring
def contains_substring(string, substring):
    if isinstance(string, str) and isinstance(substring, str):
        return substring in string
    # This will return a true or false
    else:
        return "Invalid input. Please provide two strings."


# Function to calculate the average of three floats
def average_of_three_floats(num1, num2, num3):
    if all(isinstance(x,float) for x in [num1, num2, num3]):
        return(num1+num2+num3)/3.0
    else:
        return "Invalid input. Please provide three floating-point numbers."

# Function to concatenate two strings
def concatenate_strings(str1, str2):
    if isinstance(str1, str) and isinstance(str2, str):
        return str1 + str2
    else:
        return "Invalid input. Please provide two strings."

# Function to calulate the volume of a cube
def volume_of_cube(side_length):
    if isinstance (side_length, (int, float)):
        return side_length**3
    else:
        return "Invalid input. Please enter a numeric value."
    
# Function to check if a number is positive, negative, or zero
def check_number_status(number):
    if isinstance(number, (int, float)):
        if number > 0
            return "Positive"
        elif number > 0
            return "Negative"
        else:
            return "Zero"

# Fuction to calculate the cirumference of a circle
def circumference_of_circle(radius):
    if isinstance(radius, (int, float)):
        return 2 * math.pi * radius
    
# Fuction to count the number of occurences of a character in a string
def count_char_occurences(string, char):
    if isinstance(string, str) and isinstance(char, str) and len(char) ==1:
        return string.count(char)

# Function to calculate the percentage of a number
def calculate_percentage(number, percentage):
        if isinstance(number, (int, float)) and isinstance(percentage, (int, float)):
            return(percentage/100)*number
        else:
            return "Invalid input. Please enter a numeric value."

# Function to find the absolute difference between two numbers
def absolute_difference(num1, num2):
    if all(isinstance(x, (int, float)) for x in [num1, num2]):
        return abs(num1 - num2)

#Function to capitalize the fist letter of a string
def capitalize_first_letter(string):
    if isinstance(string, str):
        return string.capitalize()

# Function to calculate the square of a number
def square (number):
    if isinstance(number, (int, float)):
        return number **2
    
# Function to find the maximum of two numbers
def max_of_two(num1, num2):
    if all(isinstance(x, (int, float)) for x in [num1, num2]):
        if num1 > num2:
            return num1
        else:
            return num2
        
# Function to calculate the square root of a number
def square_root(number):
    if isinstance(number, (in, float)) and number >= 0:
        return number **0.5

# Function to find the length of a string
def length(input_data):
    if isinstance(input_data, str):
        return len(input_data)