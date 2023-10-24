# Print a triangle
def print_triangle(char, size):
    for _ in range(size):
        print(char*size)
        size=size-1

c = input("Please enter a character: ")
i = int(input("Please enter an integer number: "))
print_triangle(c, i)

#Print a square
def print_square(char, size):
    for _ in range(size):
        print(char*size)

character = input("Please enter a character: ")
integer = int(input("Please enter an integer number: "))
print_square(character, integer)

#Print name
def greeting(name):
    return "Hello " +name + "!"

def howOld(age):
    if age > 19:
        return"You are no longer a teenager."
    else:
        return "You are still young"
    
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
print(greeting(name))
print(howOld(age))