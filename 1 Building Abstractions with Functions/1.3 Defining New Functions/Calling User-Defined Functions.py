from operator import mul
def square(x):
    return mul(x,x)
print(square(2))

# func(operant,operant) but operant can also be the function
from operator import mul,add
def square(x):
    return mul(x,x)

def sum_square(x,y):
    return add(square(x),square(y))

result = sum_square(5, 12)
print(result)