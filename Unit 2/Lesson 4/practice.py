# 3 middle letters
def middle_letters(str):
    start = (len(str)//2)-1
    end = start+3
    return print(str[start:end:1])


str1 = "Candy"
str2 = "and"
str3 = "Solving"

#string[start:end:step]
#step is how it works
#Start is the starting index of your string if it isn't there is is assumed as zero
#End is the end location if there isn't one it goes to the end of the string

print(middle_letters("Candy"))

def area_of_square(len):
    if isinstance(len, (int, float)):
        return len**2
    
length = 4
print(area_of_square(length))

def volume_of_a_cube(len):
    if isinstance(len, (int, float)):
        return len**3

height = 4
print(volume_of_a_cube(height))


#Given 2 strings, a and b, return a new string made of the first char of a and the last char of b
def last_chars(a, b):
    if all(isinstance(x, str) for x in [a, b]):
        a = a[:2:1]
        length = len(b) + 1
        end = length-1
        b = b[end:length:1]
        return a+b

a = "Hello"
b = "Bai"
print(last_chars(a,b))


#Given a string of any length
def last_two(str):
    length = len(str)
    front = str[:2]
    end = str[3:length+1]
    return end+front

str = "Hello"
print(last_two(str))

#4
def extraFront(str):
    length = len(str)
    front = str[:2]
    return front + front + front

str = "Hello"
print(extraFront(str))
