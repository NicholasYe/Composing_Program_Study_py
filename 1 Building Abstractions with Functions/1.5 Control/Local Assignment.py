# "difference" in func is a local assignment but not global
def percent_difference(x,y):
    difference = abs(x-y)
    return 100 * difference / x

result = percent_difference(40, 50)
print(result)