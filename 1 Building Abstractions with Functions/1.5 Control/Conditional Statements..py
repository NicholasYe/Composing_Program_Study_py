# we can define a func with different condition
def absolute_value(x):
    """Compute abs(x)."""
    if x > 0:
        return x
    elif x == 0:
        return 0
    else:
        return -x

result = absolute_value(-10)
print(result)