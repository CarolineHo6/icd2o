#Integer ('int') used for whole numbers, example
age = 25
print(age)

#Float ('float') example
temperature = 98.6
print(temperature)

#String ('str') used for words, example
name = "Alice"
print (name)

#Boolean (bool) are used to represent True and False (used for logic)
# true and false must loook like this -> (True and False) not this ->(true and false)
right = True
wrong = False

print ("1+1=2 = " +str(right)+ "?")


#Try
age = 25
age = age + 5
name = "Jack"
shoe_size = 9.8

#print(name +"is " +age+ " years old. " +name + " wears a size " +shoe_size+ " shoe.")
print(name +" is " +str(age)+ " years old. " +name + " wears a size " +str(shoe_size)+ " shoe.")
# this code above won't work, add str (___) for the integers
print(name + " is " +str(age)+ ", " +name+ "'s shoe size is " +str(shoe_size)+ ".")

# Calculate the area of a circle

rad = 4.5
ar = 2 * 3.14 * rad

print("The area of a circle with radius " +str(rad)+ " is " +str(ar))