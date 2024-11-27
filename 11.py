# Algorithm:
# 1. Define a function `fib(n)` that takes an integer `n` as input.
# 2. Initialize variables `a` and `b` to the first two Fibonacci numbers (0, 1).
# 3. Print the first two Fibonacci numbers.
# 4. Use a while loop to generate the next Fibonacci numbers until `n` terms are printed:
#    - Update `a` and `b` to the next Fibonacci numbers.
# 5. Print each Fibonacci number.

def fib(n):
    a, b = 0, 1
    print(a, b, end=" ")  # Print the first two numbers
    while n > 2:
        c = a + b
        a, b = b, c
        print(c, end=" ")
        n -= 1

fib(6)
