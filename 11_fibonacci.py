# This file contains various implementations of a Fibonacci function.
# The Fibonacci suite starts with 0 and 1.
# After that the next elements are the sum of the 2 previous ones.
# Here is the beginning of the Fibonacci suite:
# 0 1 1 2 3 5 8 13 21 34 55 89 …

# A Fibonacci function returns the nth element in the Fibonacci suite.
# Fibonacci(0) = 0
# Fibonacci(1) = 1
# Fibonacci(2) = 1
# Fibonacci(3) = 2
# 

def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci (n -1)

for i in range(20):
    print("Fibonacci({})={}".format(i, fibonacci(i)))
