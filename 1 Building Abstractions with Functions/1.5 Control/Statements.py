from operator import mul

# this call will not return a value
def square_1(x):
    mul(x,x)

# return the value
def square_2(x):
    return mul(x,x)

# not return but print the value
def square_3(x):
    print(mul(x,x))

print(square_1(3))
print(square_2(4))
square_3(5)