# Algorithm:
# 1. Take an integer input `n` from the user.
# 2. Use a nested loop:
#    - Outer loop runs from 1 to `n` (inclusive).
#    - Inner loop runs from 1 to the current outer loop value (`i`).
#    - Print numbers from 1 to `i` on the same line.
# 3. Move to the next line after each inner loop iteration.

n = int(input("Input a Number: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()