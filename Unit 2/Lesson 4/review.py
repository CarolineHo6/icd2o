print(5/2) #divides
print(5//2) #gives powers
print(5%2) #gives remainder
print(5**2) #gives power

def round_down(x,y):
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        return x // y

x = 1
y = 2
print(f"{round_down}")
