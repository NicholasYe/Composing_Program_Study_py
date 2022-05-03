# function with iteration
def fib(n):
    """Compute the nth Fibonacci number, for n >= 2."""
    pred, curr = 0, 1  # Fibonacci number 1 and 2
    k = 2              # which fib number is curr?
    while k < n:
        pred, curr = curr, pred+curr
        k = k + 1
    return curr

# test fib() is right or wrong
def fib_test():
    assert fib(2) == 1, 'The 2nd Fibonacci number should be 1'
    assert fib(8) == 13, 'The 8nd Fibonacci number should be 13'
    # assert fib(8) == 23, 'Error at the 8th Fibonacci number'
    
if __name__ == "__main__":
    fib_test()