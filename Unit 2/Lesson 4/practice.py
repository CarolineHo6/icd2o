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

