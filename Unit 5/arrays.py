# Empty list
lists = []
print(f"This is my list: {lists}")

# List of integers
nums = [10, 20, 30]
print(f"This is my integer list: {nums}")

# List of strings
strings = ["Hello", "Goodbye", "Hello"]
print(f"This is my list of strings: {strings}")

# Try something (Doesn't work)
list = ["1000", "99", "100"]
list.sort()
print(list)

# Input
arr = []
for i in range(1, 6):
    num = int(input("Please enter a number: "))
    arr.append(num)
    print(arr)
arr.sort()
print(arr)

# Arrays are a box that contains a specific data type
# WHen 2D array list = [[2, 3], [x, y]] to call the 2 the say list = [0][1]

# Doing the magic square thing
list = [[],[],[],[]]
for i in range(1,5):
    for x in range(1,5):
        list.append("user input")

