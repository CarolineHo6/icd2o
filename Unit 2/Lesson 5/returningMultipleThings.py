'''print("= "*10)
print("Hello"*4)
print("-"*45)'''

def simple_function():
    x=7
    y=8
    z=9
    return x, y, z
# Once you put a return statement you exit the function

print(simple_function())

# x goes into a, y goes into b, z goes into c
a,b,c = simple_function()

print(a)
print(b)
print(c)
    
'''q,r = simple_function()
print(q,r)'''

d = simple_function()
