from operator import truediv,floordiv,mod

def divide_exact(n,d):
    return truediv(n,d), floordiv(n,d)

quotient,remaindeer = divide_exact(2013, 10)
print('quotient:', quotient)
print('remaindeer', remaindeer)