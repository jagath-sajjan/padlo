# Algorithm:
# 1. Define a function `fact(n)` that calculates the factorial of `n`.
# 2. If `n` is 1, return 1 (base case).
# 3. Otherwise, return `n` multiplied by the factorial of `n-1` (recursive case).
# 4. Print the factorial of 5.

def fact(n):
    return 1 if n == 1 else n * fact(n - 1)  # Recursive factorial calculation

print(fact(5))
