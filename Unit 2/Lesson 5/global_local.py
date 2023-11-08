global_book = "Science Encyclopedia" #golbal_book is decalred OUTSIDE all functions

def section_book():
    local_book = "Chemistry Handbook" + global_book
    #print(f"In the section: We have the {global_book} and the {local_book}")
    return local_book

#When you call the function then it makes a "copy"
print(section_book())

global_book = " I tore the cover off"

print(section_book())

