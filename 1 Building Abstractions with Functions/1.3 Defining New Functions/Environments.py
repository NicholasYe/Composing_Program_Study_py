from math import pi
tau = 2 * pi

# the template of func:
# def func(x):
#     return x
from operator import mul
def square(x):
    return mul(x,x)

# you can define original function into other but you can't use it after redefine
f = max
max = 3
print(f(2,3,4))
# print(max(2,3,4))  # this is not allowed!