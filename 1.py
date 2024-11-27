# Program To Demonstarte Operators

# Algorithm:
# 1. Initialize variables a, b, c, d with given values.
# 2. Calculate and print results of different arithmetic expressions with parentheses.
# 3. Use parentheses to alter operation order where required.

a, b, c, d = 20, 10, 15, 5

print((a + b) * c / d)    # First expression
print((a + b) * c / d)    # Second expression (same as first due to order of operations)
print((a + b) * (c / d))  # Third expression
print(a + b * c / d)      # Fourth expression
