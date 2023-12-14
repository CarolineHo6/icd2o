# print the numbers from 1 to 5
def example_one():
    for counter in range(1,6):
        print(counter)

# print the numbers from 0,9
def example_one_a():
    for counter in range(10):
        print(counter)

# add the numbes from start to finish and return the total
def example_two(start,finish):
    total = 0
    for i in range(start, finish+1):
        total += i

    return total

# prints number from 20 to 1 and goes down by 2s
def example_three():
    for i in range(20, 0, -2): 
        # the -1 tells it to count down
        # if there was nothing it would try to count up but the finishing thing would be a number less that the starting number 
        # so it can't go up so it doesn't print anything
        print(i)    

# print a string backwards
def example_four(str):
    result = "" # make the variable empty
    for i in range(len(str)-1, -1, -1):
        result += str[i]
        print(result) # To show string being built
    print(result)

# grab substrings of length n and print them to the screen
def example_five(str, n):
    for i in range(0, len(str)-n+1):
        print(str[i:i+n])

# count how many times the second word appears in the first word
def example_six(str1, str2):
    if len(str2) > len(str1):
        return 0
    
    result = 0 # counter says result is 0

    for i in range(0, len(str1) - len(str2) + 1): # - len(str2) so it doesn't go to an empty spot and blow up code 
        # but add 1 so that it returns the ending
        if str1[i: i+len(str2)] == str2:
            result += 1
    
    return result
    

#example_one()
#example_one_a()
answer = example_two(1, 10)
print(answer)
#example_three()
#example_four("Taylor Swift")
#example_five("Taylor Swift", 3)
#print(example_six("abcdabcd", "ab"))

