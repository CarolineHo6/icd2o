import math
#Problem 1: Word Length Average
string_list = ["apple", "kiwi", "banana", "strawberry", "blueberry"]
total = 0
for i in range(len(string_list)):
    total += len(string_list[i])
total /= len(string_list)
print(f"Average length of word is: {total}")

#Problem 2: Palindrome Count
list = ["level", "python", "radar", "civic", "list"]
p=0
def isPalindrome(s):
    return s == s[::-1]

for i in range(len(list)):
    s = list[i]
    ans = isPalindrome(s)
 
    if ans:
        p +=1
print(p)

#Problem 3: Concatenate String
starting_list = ["Hello", "world", "of", "Python", "programming"]
result = ""
for i in range(len(list)):
    result += starting_list[i]
    result += " "
print(result)

#Problem 4: Vowel Count
vowels = 0
for i in range(len(string_list)):
    y = string_list[i]
    for i in range(len(y)):
        if y[i:i+1] == 'a' or y[i:i+1] == 'e' or y[i:i+1] == 'i' or y[i:i+1] == 'o' or y[i:i+1] == 'u':
            vowels += 1
print(vowels)

#Problem 5: Alternate Uppercase
#listing = ["python", "programming", "list", "iteration"]
#for i in range(len(listing)):
#    t = listing[i]
#    for z in range(0, len(t), 2):
#        listing[z] += t[z].upper()
#print(listing)

#List of numbers problems
# Problem 1: Positive Negatives
num1 = [2,5,8,10,3,7,1,6]
positive = []
negative = []
for i in range(len(num1)):
    if num1[i] % 2 == 0:
        positive.append(num1[i])
    else:
        negative.append(num1[i])
positive.sort()
negative.sort()
print(f"Positive List: {positive}. Negative List: {negative}")

# Problem 2: Fibonacci Check
num2 = [0,1,1,2,3,5,8,13,21]
yes = True
for i in range(2, len(num2)):
    if num2[i] != num2[i-1] + num2[i-2]:
        yes = False
print(yes)

# Problem 3: Square roots
num3 = [1,4,9,16,25]
for i in range(len(num3)):
    num3[i] = math.sqrt(num3[i])
    num3.append(round(num3[i]))
print(num3)

# Problem 4: Running Average
num4 = [5,10,15,20,25]
number = 1
for i in range(len(num4)):
    num4[i] = num4[i]/number
    number +=1
print(num4)

# Problem 5: Consecutive Pairs
num5 = [3,5,7,9,10,11,15]
hi = False
for i in range(1, len(num5)-1):
    if num5[i] == num5[i+1] - 1:
        hi = True
print(hi)

