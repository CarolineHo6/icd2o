global_book = "Science Encyclopedia" #golbal_book is decalred OUTSIDE all functions

def section_book():
    local_book = "Chemistry Handbook"
    #print(f"In the section: We have the {global_book} and the {local_book}")
    return local_book

#When you call the function then it makes a "copy"
myBook = section_book()

print(f"In the library we still have {global_book}")

print(f"We do not have: {myBook}")
print(global_book)
#myBook = myBook + " Hello"
#myBook = global_book
#myBook = myBook + " I wrote in this"
global_book = global_book + " I wrote something"
print(myBook)
print(section_book())
print(global_book)


# This is in the main program so it will print
x=-2
if x>0:
    inside_if = "This was created in the 'if' block"
    print(inside_if)
else:
    inside_if = "The variable is empty"
# if is for if this part is true then run this piece of code

#local scope doesn't include anything except for functions so inside_if is still visable
print(inside_if)
#Visable means it is still visable in the program. Whereas a function is invisable unless you call on it


