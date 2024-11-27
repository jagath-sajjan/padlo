# Algorithm:
# 1. Use a for loop to iterate through numbers 0 to 5.
# 2. Skip printing if the number is 3 using `continue`.
# 3. Print each number followed by a newline.

for x in range(6):
    if x == 3:
        continue
    print(x, end="")
    print('\n')
