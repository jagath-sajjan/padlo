# Algorithm:
# 1. Take three numbers as input from the user.
# 2. Use conditional statements to compare the numbers and determine the median.
# 3. Print the median.

a, b, c = float(input("1st number: ")), float(input("2nd number: ")), float(input("3rd number: "))

if (b < a < c) or (c < a < b):
    median = a
elif (a < b < c) or (c < b < a):
    median = b
else:
    median = c

print(median)