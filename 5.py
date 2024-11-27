# Algorithm:
# 1. Initialize variables x and y to the first two Fibonacci numbers (0, 1).
# 2. Use a while loop to generate numbers until y is less than 50:
#    - Print the current value of y.
#    - Update x and y to the next two Fibonacci numbers.
# 3. End loop when y reaches or exceeds 50.

x, y = 0, 1
while y < 50:
    print(y)
    x, y = y, x + y