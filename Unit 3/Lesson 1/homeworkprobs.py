#quetion 1
def caught_speeding(speed, is_birthday):
    if (speed <= 65) and (is_birthday == True):
        return "You can drive 5 mph faster"
    if speed <= 60:
        return "Not Ticket"
    if speed >= 61 or speed <= 80 and is_birthday == False:
        return "Small Ticket"
    else:
        return "Big Ticket"

#question 2
def not_string(s):
    if s == "not":
        return s
    else:
        return "not"+s

#Question 3
def squirrel_play(temp, is_summer):
    if temp >= 60 or temp <= 90 and is_summer == True:
        return True
    else:
        return False

#Question 4
def in1020(a, b):
    if a >=10 or a <=20 or b >=10 or b <=20:
        return True
    else:
        return False

#Question 5
def theEnd(str, front):
    if front == True:
        return str[:1]
    if front == False:
        return str[(len(str)-1):len(str)]
    else:
        return "Empty"

print(theEnd("Hello", False))
print(theEnd("", True))